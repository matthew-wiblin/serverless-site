views = {
    'home': {
        'title': 'Welcome to the Home Page',
        'titlesize': 1,
        'border': True,
        'components': [
            {'type': 'divider'},
            {'type': 'grid', 'components': [
                [
                    [
                        {'type': 'card', 'title': 'Overview of the site', 
                            'description': ['This site is a simple file storage manager', 
                                'You can sign up for an account and manage/store your projects',
                                'Complete with audit and other functionality']},
                        {'type': 'photo', 'where': 'frontend', 'location': 'spaniels-three.png'}
                    ],
                    [
                        {'type': 'card', 'title': 'Architecture overview', 
                            'description': ['Frontend is created in JS/React deployed to an S3 bucket w/ cloudfront and R53',
                                'Authentication is handled with AWS Cognito',
                                'Backend in python and go deployed using the serverless framework to AWS lambda']},
                        {'type': 'photo', 'where': 'frontend', 'location': 'diagram-infra.png'}
                    ]
                ]
            ]},
        ]
    },
    'projects-list': {
        'authenticated': True,
        'title': 'Your Projects ...',
        'titlesize': 2,
        'border': True,
        'components': [
            {'type': 'divider'},
            {'type': 'grid', 'columns': 4, 'data': {
                'SK': ['ADMIN#', 'MEMBER#'],
                'USER': 'USER#<userid>',
            }}
        ]
    }
}
