## Photo collection app

Serverless Proj hosted on AWS

 - Front end deployed to an S3 bucket and a cloudfront distribution
 - Available through a Route-53 DNS name -- "serverlesssite.com"

 - Backend deployed in lambdas accessed through an API gateway
 - Connected to a dynamodb DB

![Architecture Diagram](/frontend/public/diagram-infra.png)

### naming conventions
Frontend:
 - components, pages = PascalCase
 - hooks, functions, .js = camelCase

Backend:
 - classes = PascalCase
 - variables, functions, files, modules = lowercase
