model = {
    'user': {
        'primarykey': {'attributename': 'id', 'displayname': 'User ID', 'type': 'integer'},
        'attributes': [
            {'attributename': 'username', 'displayname': 'Username', 'type': 'string'},
            {'attributename': 'listingscreated', 'displayname': 'Listings Created', 'type': 'array'},
            {'attributename': 'requestssent', 'displayname': 'Requests Sent', 'type': 'array'},
            {'attributename': 'requestsrecieved', 'displayname': 'Requests Recieved', 'type': 'array'}
        ],
        'GSIs': []
    },
    'listing': {
        'primarykey': {'attributename': 'id', 'displayname': 'Listing ID', 'type': 'integer'},
        'attributes': [
            {'attributename': 'userid', 'displayname': 'Owner ID', 'type': 'integer'},
            {'attributename': 'imageurl', 'displayname': 'Image URL', 'type': 'string'},
            {'attributename': 'createdat', 'displayname': 'Created At', 'type': 'datetime'},
            {'attributename': 'listingstatus', 'displayname': 'Listing Status', 'type': 'lookup', 'lookupname': 'status'},
            {'attributename': 'pettype', 'displayname': 'Pet Type', 'type': 'string'},
            {'attributename': 'breed', 'displayname': 'Breed', 'type': 'string'},
            {'attributename': 'gender', 'displayname': 'Gender', 'type': 'lookup', 'lookupname': 'gender'},
            {'attributename': 'description', 'displayname': 'Description', 'type': 'string'},
            {'attributename': 'location', 'displayname': 'Location', 'type': 'string'}
        ],
        'GSIs': []
    },
    'request': {
        'primarykey': {'attributename': 'id', 'displayname': 'Request ID', 'type': 'integer'},
        'attributes': [
            {'attributename': 'listingid', 'displayname': 'Listing ID', 'type': 'integer'},
            {'attributename': 'ownerid', 'displayname': 'Owner ID', 'type': 'integer'},
            {'attributename': 'requesterid', 'displayname': 'Requester ID', 'type': 'integer'},
            {'attributename': 'message', 'displayname': 'Message', 'type': 'string'},
            {'attributename': 'createdat', 'displayname': 'Created At', 'type': 'datetime'},
            {'attributename': 'requeststatus', 'displayname': 'Request Status', 'type': 'lookup', 'lookupname': 'status'}
        ],
        'GSIs': []
    },
}
