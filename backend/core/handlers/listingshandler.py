import json

from core.lib.awsfunctions import isauthenticated
from core.lib.dbfunctions import createitem


def listingshandler(event, context):
    print('event = ', event)

    body = json.loads(event['body'])
    x = createitem('USERS', body)

    auth = event['headers']['Authorization']
    decode = isauthenticated(auth)

    returnbody = {
        'message': "Users function successfully invoked !",
        'event': event,
        'body': body,
        'decode': decode,
        'createitem return': x
    }

    response = {
        "statusCode": 200, 
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
        },
        "body": json.dumps(returnbody)}

    return response

