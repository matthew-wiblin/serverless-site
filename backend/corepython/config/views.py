views = {
    'home': {
        'title': 'Welcome to the Home Page',
        'titlesize': 1,
        'border': True,
        'components': [
            {'type': 'divider'},
            {'type': 'columns', 'components': [
                [
                    {'type': 'card', 'title': 'Overview of the site', 
                        'description': ['This site is a simple photo uploader', 
                            'You can sign up for an account and manage/store your photos']},
                    {'type': 'photo', 'where': 'frontend', 'location': 'spaniel-brown.png'}
                ],
                [
                    {'type': 'card', 'title': 'Architecture overview', 
                        'description': ['Frontend is created in JS/React deployed to an S3 bucket w/ cloudfront and R53',
                            'Authentication is handled with AWS Cognito',
                            'Backend in python and go deployed using the serverless framework to AWS lambda',
                            'Data stored in a mixture of dynamodb and S3 buckets']},
                    {'type': 'photo', 'where': 'frontend', 'location': 'diagram-infra.png'}
                ]
            ]},
        ]
    },
    'profile': {

    }
}
