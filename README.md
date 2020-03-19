# Lambda Function for SSH KEY Pairs

This repository is containing lambda function that have a property for generating SSH key pair and then store them to the S3 bucket instead of local filesystem.

## Dependecies


* virtualenv

That script is containing script for end to end local dependency environment .


```
    $ virtualenv v-env
    $ source v-env/bin/activate
    $ pip3 install cryptography
    $ pip3 install boto3
```

## Build and Deploy :) 

You need terraform to deploy or you can easily deploy via aws cli . I have prefer the terraform .

```
$ ./build.sh
```