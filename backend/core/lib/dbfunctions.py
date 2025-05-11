import os
import boto3
import uuid


def dbconnect(name):
    dynamodb = boto3.resource("dynamodb")
    tablename = 'DYNAMODB_TABLE_' + name
    table = dynamodb.Table(os.environ[f"{tablename}"])
    return table


def createitem(table, data): # reference model to check data
    table = dbconnect(table)

    id = str(uuid.uuid4())

    item = { 'userid': id } | data

    table.put_item(Item=item)

    return id

