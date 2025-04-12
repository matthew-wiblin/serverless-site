import os
import json
import boto3
import uuid

thing = None
try:
    from core.lib.is_authenticated import is_authenticated
except Exception as e:
    thing = str(e)

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
    decode = thing

    # try:
    #     decode = is_authenticated(auth)
    # except Exception as e:
    #     decode = str(e)
    

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
# token = "Bearer eyJraWQiOiJ5SGpmeGxNU2wzdklYdzJKRWordk5zMjExNXU2M3lqd0xKckN5cjF5UWpZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIzNjIyMTIzNC01MDMxLTcwYjMtMjJhZi0wMzFjODI2ZmE2NGIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtd2VzdC0yLmFtYXpvbmF3cy5jb21cL2V1LXdlc3QtMl9qMkFSWkRzWkwiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI2cTljMzZlYXFvZG8xZTYxMm1lbDlyZjNobyIsIm9yaWdpbl9qdGkiOiI5Y2IwZWU2Ni03MTExLTQyMWYtOTk5NS0wMzk0NGFiODVhNzEiLCJldmVudF9pZCI6IjM3YzM1NWJkLTA2YzYtNGQyOC05NDQ4LTQ0ZGQzNGJjZTRjOCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoicGhvbmUgb3BlbmlkIGVtYWlsIiwiYXV0aF90aW1lIjoxNzQ0NDQ3NDk2LCJleHAiOjE3NDQ0NTEwOTYsImlhdCI6MTc0NDQ0NzQ5NiwianRpIjoiNzJhN2I0Y2EtY2UxNS00YzVkLThmZDItZDljYWEyYzgzMTM0IiwidXNlcm5hbWUiOiJtYXR0aGV3d2libGluIn0.YcdcNBVGwqj9-BJiDYRRQH1NeWSPMWLErrATUSeo8xI_fTDIisfQT77jtbkeoVT-3dqq7m0lHbRaQbNpw3Y2RBiDazIMiGAtnq6Cch_La-UEWoPdddsYMJIcAmS_Edkztxd1awL48J4q5R7ltwXtOagAjJ_3KAWxFtB4LHLpkigOlYVJBJ-WhKTjo93mHWr0Allv_JXAK7F7lwmlOE_2CXP_QC0lQIy-WbNGzL28-63x85dYRAligDB4bP6RSWaR_AjD4C1aXfKV3oO0kqJs6F8ppsCkopMAxKqDN_bv5q9onmIvKR4uYwuGT5dV-A0VSVjsk6i9VMvKxNroJwDDEQ"
# print(is_authenticated(token))