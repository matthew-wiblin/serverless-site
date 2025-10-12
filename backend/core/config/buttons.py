buttons = {
    'uploadphoto': {
        'title': 'Upload a Photo',
        'entity': 'photo',
        'fields': [
            { 'name': 'photoname', 'label': True, 'type': 'text', 'required': True },
            { 'name': 'photo', 'label': 'Upload a Photo', 'type': 'photoupload', 'required': True },
            { 'name': 'description', 'label': True, 'type': 'text', 'required': False }
        ]
    },
    'uploadphotobulk': {
        'title': 'Upload Photos',
        'entity': 'photo',
        'fields': [
            { 'name': 'photoname', 'label': True, 'type': 'text', 'required': True },
            { 'name': 'photo', 'label': 'Upload Photos', 'type': 'photouploadmulti', 'required': True }
        ]
    }
}
