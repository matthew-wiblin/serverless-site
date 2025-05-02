import os
import json
import boto3

def db_connect(tablename):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ[f"{tablename}"])
    return table


def create(event, context):
    pass

