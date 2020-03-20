# Lambda Function for SSH KEY Pairs

This repository is containing lambda function that have a property for generating SSH key pair and then store them to the S3 bucket instead of local filesystem.

## Build and Deploy

You can build generator function with docker, and then you can deploy with from container.

For configure the aws cli you should set AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY related with your aws credentials

```
    $ aws lambda update-function-code --function-name staging-ssh-key-generator  --zip-file fileb://function.zip
```