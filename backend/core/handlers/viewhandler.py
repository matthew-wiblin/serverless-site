import json

from core.lib.awsfunctions import returnauthenticateduser
from core.lib.dbfunctions import createitem


def viewhandler(event, context):
    print('event = ', event)

    result, username = returnauthenticateduser(event)

    body = json.loads(event['body'])

    urlpath = event.get("pathParameters") or {}

    returnbody = {
        'message': "Users function successfully invoked !",
        'event': event,
        'body': body,
        'result username': str(result) + ' ' + username,
        'urlpath': urlpath
    }

    return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps(returnbody)}
