import json
import os
import time
import uuid
import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'firstName': data['firstName'],
        'lastName': data['lastName'],
        'email': data['email'],
        'comments': data['comments'],
        'options': data['options'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "body": json.dumps(item),
        "headers": {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true"
        }
    }

    return response