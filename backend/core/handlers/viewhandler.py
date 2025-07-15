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

    view = {}
    if method == 'GET' and urllist[0] == 'view':
        view = views[urllist[1]]
        for key, value in view.items():
            if key == 'title':
                pass
            if key == 'components':
                pass

    print(userresult, username, urllist, method, view)

    return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps(view)}
