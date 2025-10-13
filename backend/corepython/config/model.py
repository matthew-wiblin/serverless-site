model = {
    'user': {
        'primarykey': {'attributename': 'id', 'Label': 'User ID', 'type': 'integer'},
        'attributes': [
            {'attributename': 'username', 'Label': 'Username', 'type': 'string'}
        ],
        'GSIs': []
    },
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
