import json


def apihandler(event, context):
    print('event = ', event)

    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!"
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
