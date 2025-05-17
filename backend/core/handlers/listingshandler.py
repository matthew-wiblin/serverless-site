import json

from core.lib.awsfunctions import isauthenticated
from core.lib.dbfunctions import createitem


def listingshandler(event, context):
    print('event = ', event)

    auth = event['headers']['Authorization']
    result, username = isauthenticated(auth)

    body = json.loads(event['body'])

    urlpath = event.get("pathParameters", {}).get("urlpath", "")

    urlpath2 = event['pathParameters']['urlpath']

    returnbody = {
        'message': "Users function successfully invoked !",
        'event': event,
        'body': body,
        'result username': result + ' ' + username,
        'urlpath': urlpath,
        'urlpath2': urlpath2
    }

    # response = {
    #     "statusCode": 200, 
    #     "headers": {
    #         "Access-Control-Allow-Origin": "*",
    #         "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    #         "Access-Control-Allow-Headers": "Content-Type, Authorization",
    #     },
    #     "body": json.dumps(returnbody)}
    # return response

    return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps(returnbody)}

