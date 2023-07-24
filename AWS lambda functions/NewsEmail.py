import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'Email'
table = dynamodb.Table(table_name)
# print(table)

def create_ses_subscription(email_id):
    try:
        sns_client = boto3.client('sns', region_name='ap-south-1')
        sns_topic_arn = 'arn:aws:sns:ap-south-1:543991822877:confirm_subscription'
        response = sns_client.subscribe(
            TopicArn=sns_topic_arn,
            Protocol='email',
            Endpoint=email_id
        )
        subscription_arn = response['SubscriptionArn']
        print(
            f"SNS subscription created successfully. Subscription ARN: {subscription_arn}")
    except Exception as e:
        print(f"Error creating SNS subscription: {e}")


def lambda_handler(event, context):
    try:
        print("event:", event)
        event_body = json.loads(event['body'])
        email_id = event_body['email_id']
        # email_id = '195514@nitk.com'

        print(f"Email id: {email_id}")

        # Create the item to be put into DynamoDB
        item = {
            'email_id': email_id
        }

        # Put the item into DynamoDB
        response = table.put_item(Item=item)
        create_ses_subscription(email_id)
        return {
            'statusCode': 200,
            'body': json.dumps('Email ID added to DynamoDB successfully.')
        }
    except Exception as e:
        print('Error adding email to DynamoDB:', e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error adding email to DynamoDB.')
        }
