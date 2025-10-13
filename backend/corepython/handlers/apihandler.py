import json


def apihandler(event, context):
    print('event = ', event)

    body = {"message": "Go Serverless v4.0! Your function executed successfully!"}

    return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps(body)}
 
 