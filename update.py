import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    response = table.update_item(
        Key={
            'id': data['id']
        },
        UpdateExpression="set info.firstName=:n, info.lastName=:l, info.email=:e, info.comments=:c",
        ExpressionAttributeValues={
            ':n': data['firstName'],
            ':l': data['lastName'],
            ':e': data['email'],
            ':c': data['comments']
        },
        ReturnValues="UPDATED_NEW"
    )
    return response