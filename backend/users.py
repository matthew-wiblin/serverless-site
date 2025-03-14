import json


def users(event, context):
    body = {
        "message": "Users function successfully invoked !",
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
