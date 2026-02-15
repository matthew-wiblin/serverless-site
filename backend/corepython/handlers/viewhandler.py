import json

from corepython.lib.functions.dbfunctions import getitems
from corepython.config.views import views
from corepython.config.model import model

from corepython.lib.classes.event import Event

def viewhandler(event, context):
    myevent = Event(event)

    if myevent.urllist[1] not in views:
        return {"statusCode": 400, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps('No view found')}
    
    view = views[myevent.urllist[1]]

    for key, value in view.items():
        if key == 'authenticated':
            if value == True and myevent.isloggedin == False:
                return {"statusCode": 401, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps('Not authenticated')}
        if key == 'title':
            pass
        if key == 'titlesize':
            pass
        if key == 'border':
            pass
        if key == 'components':
            view['components'] = handlecomponent(myevent, value)
    
    return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps(view)}

def handlecomponent(myevent, components):
    """Recursively handle all components. Reuses itself for nested components."""

    output = []
    for comp in components:
        # Handle nested components - eg in a list
        if not isinstance(comp, dict):
            output.append(handlecomponent(myevent, comp))
            continue

        type = comp.get('type')

        if type == 'divider':
            output.append({'type': 'divider'})

        elif type == 'card':
            output.append({'type': 'card', 'title': comp.get('title'), 'description': comp.get('description', [])})

        elif type == 'photo':
            output.append({'type': 'photo', 'where': comp.get('where'), 'location': comp.get('location')})

        elif type == 'grid':

            grid_output = {'type': 'grid'}

            # If grid has nested components - recurse
            if 'components' in comp:
                grid_output['components'] = handlecomponent(myevent, comp['components'])

            # If grid collects data from DynamoDB
            if 'data' in comp:

                data_config = comp['data']

                # -------- SINGLE DYNAMODB TABLE QUERY --------
                items = getitems(table=model['table'], pk=data_config['USER'].replace('<userid>', myevent.userid), sk_prefixes=data_config['SK'])
                # ---------------------------------------------

                grid_output['items'] = items

            output.append(grid_output)

        # ---- Unknown type ----
        else:
            output.append(comp)

    return output