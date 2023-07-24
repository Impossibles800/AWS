document.addEventListener("DOMContentLoaded", function () {
    // Get the form element
    const form = document.querySelector("form");

    // Get the success message element
    const successMessage = document.querySelector(".success-message");

    // Add a submit event listener to the form
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        // Get the user's email address from the form
        const email = form.email.value.trim();
        console.log('email: ',email);

      


        fetch("https://0m0hdfrxfj.execute-api.ap-south-1.amazonaws.com/default/NewsEmail", {
            method: "POST",
            body: JSON.stringify({
                email_id: email
            })
        }).then((response) => {
            if (response.status === 200) {
                console.log("Response", response);
                form.style.display = "none";
                // Show the success message
                successMessage.style.display = "block";
            } else {
                alert("Subscription failed");
                console.error("Subscription failed. Status code: " + response.status);
            }
        })
            .catch((error) => {
                alert("Internal server error");
                console.error("Error occurred:", error);
            });
    });
});
