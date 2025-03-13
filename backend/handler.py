import json


def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    response = {
        "statusCode": 200, 
        "headers": {
            "Access-Control-Allow-Origin": "*",  # Allow all origins or specify 'http://localhost:5173'
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
        },
        "body": json.dumps(body)}

    return response
