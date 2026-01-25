model = {
    'gsipartitionkeys':[
        'USER'
    ],
    'items': {
        'admin': {
            'PK': {'type': 'string', 'format': 'PROJECT#<uuidv4>'},
            'SK': {'type': 'string', 'format': 'ADMIN#<uuidv7>'},
            'USER': {'type': 'string', 'format': 'USER#<usersubid>'},
            'name': {'type': 'string', 'format': 'userinput', 'validation': 'varchar<=50'},
            's3bucket': {'type': 'url'}
        },
        'member': {
            'PK': {'type': 'string', 'format': 'PROJECT#<uuidv4>'},
            'SK': {'type': 'string', 'format': 'MEMBER#<uuidv7>'},
            'USER': {'type': 'string', 'format': 'USER#<usersubid>'},
            'securitygroup': {'type': 'uuidv4', 'lookup': 'securitygroup'}
        },
        'folder': {
            'PK': {'type': 'string', 'format': 'PROJECT#<uuidv4>'},
            'SK': {'type': 'string', 'format': 'FOLDER#<uuidv7>'},
            'USER': {'type': 'string', 'format': 'USER#<usersubid>'},
            'name': {'type': 'string', 'format': 'userinput', 'validation': 'varchar<=50'},
            'path': {'type': 'string'}
        },
        'file': {
            'PK': {'type': 'string', 'format': 'PROJECT#<uuidv4>'},
            'SK': {'type': 'string', 'format': 'FILE#<uuidv7>'},
            'USER': {'type': 'string', 'format': 'USER#<usersubid>'},
            'name': {'type': 'string', 'format': 'userinput', 'validation': 'varchar<=50'},
            'path': {'type': 'string'},
            'size': {'type': 'int'}
        },
        'audit': {
            'PK': {'type': 'string', 'format': 'PROJECT#<uuidv4>'},
            'SK': {'type': 'string', 'format': 'AUDIT#<uuidv7>'},
            'USER': {'type': 'string', 'format': 'USER#<usersubid>'},
            'change': {'type': 'dict'}
        },
        'securitygroup': {
            'PK': {'type': 'string', 'format': 'PROJECT#<uuidv4>'},
            'SK': {'type': 'string', 'format': 'SECURITYGROUP#<uuidv7>'},
            'name': {'type': 'string', 'format': 'userinput', 'validation': 'varchar<=50'},
            'views': {'type': 'arr'}
        }
    }
}
