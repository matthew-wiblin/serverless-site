import os
import boto3
import uuid


def dbconnect():
    dynamodb = boto3.resource("dynamodb")
    tablename = 'DYNAMODB_TABLE'
    table = dynamodb.Table(os.environ[f"{tablename}"])
    return table

table = dbconnect()

def createitem(table, data): # reference model to check data
    id = str(uuid.uuid4())

    item = { 'userid': id } | data

    table.put_item(Item=item)

    return id


def getitem():
    pass


def getitems():
    pass


def updateitem():
    pass


def deleteitem():
    pass
