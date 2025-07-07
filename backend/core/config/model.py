model = {
    'photo': {
        'primarykey': {'attributename': 'id', 'Label': 'User ID', 'type': 'integer'},
        'attributes': [
            {'attributename': 'username', 'Label': 'Username', 'type': 'string'},
            {'attributename': 'photoname', 'Label': 'Photo Name', 'type': 'string'},
            {'attributename': 'imageurl', 'Label': 'Image URL', 'type': 'string'},
            {'attributename': 'createdat', 'Label': 'Created At', 'type': 'datetime'},
            {'attributename': 'description', 'Label': 'Description', 'type': 'string'}
        ],
        'GSIs': []
    }
}

# Old app idea ;)

# {
#     'user': {
#         'primarykey': {'attributename': 'id', 'Label': 'User ID', 'type': 'integer'},
#         'attributes': [
#             {'attributename': 'username', 'Label': 'Username', 'type': 'string'},
#             {'attributename': 'listingscreated', 'Label': 'Listings Created', 'type': 'array'},
#             {'attributename': 'requestssent', 'Label': 'Requests Sent', 'type': 'array'},
#             {'attributename': 'requestsrecieved', 'Label': 'Requests Recieved', 'type': 'array'}
#         ],
#         'GSIs': []
#     },
#     'listing': {
#         'primarykey': {'attributename': 'id', 'Label': 'Listing ID', 'type': 'integer'},
#         'attributes': [
#             {'attributename': 'userid', 'Label': 'Owner ID', 'type': 'integer'},
#             {'attributename': 'imageurl', 'Label': 'Image URL', 'type': 'string'},
#             {'attributename': 'createdat', 'Label': 'Created At', 'type': 'datetime'},
#             {'attributename': 'listingstatus', 'Label': 'Listing Status', 'type': 'lookup', 'lookupname': 'status'},
#             {'attributename': 'pettype', 'Label': 'Pet Type', 'type': 'string'},
#             {'attributename': 'breed', 'Label': 'Breed', 'type': 'string'},
#             {'attributename': 'gender', 'Label': 'Gender', 'type': 'lookup', 'lookupname': 'gender'},
#             {'attributename': 'description', 'Label': 'Description', 'type': 'string'},
#             {'attributename': 'location', 'Label': 'Location', 'type': 'string'}
#         ],
#         'GSIs': []
#     },
#     'request': {
#         'primarykey': {'attributename': 'id', 'Label': 'Request ID', 'type': 'integer'},
#         'attributes': [
#             {'attributename': 'listingid', 'Label': 'Listing ID', 'type': 'integer'},
#             {'attributename': 'ownerid', 'Label': 'Owner ID', 'type': 'integer'},
#             {'attributename': 'requesterid', 'Label': 'Requester ID', 'type': 'integer'},
#             {'attributename': 'message', 'Label': 'Message', 'type': 'string'},
#             {'attributename': 'createdat', 'Label': 'Created At', 'type': 'datetime'},
#             {'attributename': 'requeststatus', 'Label': 'Request Status', 'type': 'lookup', 'lookupname': 'status'}
#         ],
#         'GSIs': []
#     },
# }
