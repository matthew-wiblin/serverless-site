import json

# from corepython.lib.dbfunctions import createitem
from corepython.config.views import views
from corepython.config.model import model

from corepython.lib.classes.event import Event

def viewhandler(event, context):
    print('event = ', event)

    method = event.get("httpMethod", None)
    myevent = Event(event)

    view = {}
    if method == 'GET' and myevent.urllist[0] == 'view':
        view = views[myevent.urllist[1]]
        for key, value in view.items():
            if key == 'title':
                pass
            if key == 'components':
                pass

    return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps(view)}
