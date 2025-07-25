#!/bin/bash

source .env

echo -e "\n -- Building React app ... \n"
npm run build

echo -e "\n -- Clearing S3 bucket ($S3BUCKETNAME) ... \n"
aws s3 rm s3://$S3BUCKETNAME/ --recursive

echo -e "\n -- Uploading new build to S3 ($S3BUCKETNAME) ... \n"
aws s3 cp dist/ s3://$S3BUCKETNAME/ --recursive

echo -e "\n -- Invalidating CloudFront cache ($CLOUDFRONT) ... \n"
AWS_PAGER="" aws cloudfront create-invalidation --distribution-id $CLOUDFRONT --paths "/*" --no-paginate

echo -e "\n -- Deployment complete! \n"
