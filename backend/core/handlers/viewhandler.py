import json

from core.lib.awsfunctions import getauthenticateduser, geturllist
from core.lib.dbfunctions import createitem
from core.config.views import views
from core.config.model import model

def viewhandler(event, context):
    print('event = ', event)

    userresult, username = getauthenticateduser(event)
    urllist = geturllist(event)
    method = event.get("httpMethod", None)

    returnview = {}

    if method == 'GET' and urllist[0] == 'view':
        view = views[urllist[1]]
        returnview['title'] == view['title']
        for key, value in view.items():
            pass




    print(userresult, username, urllist, method, returnview)

    return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps(returnview)}
