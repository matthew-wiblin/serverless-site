import os
import json
import boto3
import uuid

from core.lib.is_authenticated import is_authenticated

dynamodb = boto3.resource("dynamodb")

def create(event, context):

    data = json.loads(event['body'])['data']
    item = {
        'user_id': str(uuid.uuid4()),
        'data': data
    }

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_USERS'])
    error = None

    try:
        table.put_item(Item=item)
    except Exception as e:
        error = str(e)

    auth = event['headers']['Authorization']
    decode = None

    try:
        decode = is_authenticated(auth)
    except Exception as e:
        decode = str(e)
    

    body = {
        'message': "Users function successfully invoked !",
        'event': event,
        'data': data,
        'error': error,
        'auth': auth,
        'decode': decode
    }

    response = {
        "statusCode": 200, 
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
        },
        "body": json.dumps(body)}

    return response
