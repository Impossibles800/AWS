import boto3


def lambda_handler(event, context):
    print('event: ', event)
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    print('S3 Bucket Name: ', s3_bucket)
    s3_object_key = event['Records'][0]['s3']['object']['key']

    link1 = "https://www.nytimes.com/2023/07/23/us/politics/trump-investigations-jack-smith-justice-department.html"
    link2 = "https://sns.ap-south-1.amazonaws.com/confirmation.html?TopicArn=arn:aws:sns:ap-south-1:543991822877:confirm_subscription&Token=2336412f37fb687f5d51e6e2425c464de257e9a829aa2d84c5a7249b36788ba56c869181c0ce87095a7bbee98b8dd1521db0273dc922d0a9c5106efd403f1406c909dd4832983b20532f170a7c729fd1aa8556ed76f359d4a734d608ec03d3fb5fca823b4a6f1aac9c82f641f46bc4bb7879a6c2240a5183af704c59d786c00a&Endpoint=195514@nith.ac.in"
    email_subject = "New News update"
    email_body = f"News has been updated. To view the news, click the link {link1}. If you want to unsubscribe from the notification, click here {link2}"

    sns_client = boto3.client('sns', region_name='ap-south-1')

    try:
        response = sns_client.publish(
            TopicArn='arn:aws:sns:ap-south-1:543991822877:newsUpdates',
            Subject=email_subject,
            Message=email_body
        )
        print(f"Email sent successfully. Message ID: {response['MessageId']}")
    except Exception as e:
        print(f"Error sending email: {e}")
