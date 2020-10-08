import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    data = json.loads(event['body'])
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    response = table.delete_item(
        Key={
            'id': data['id']
        }
    )

    return response