import boto3
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
import os

def upload_s3(files = ["/tmp/private.key", "/tmp/pub.key"]):

    s3_client = boto3.resource("s3")
    BUCKET = os.environ["CONFIG_BUCKET"]

    for file in files:
        obj = str.split(file, "/")
        s3_client.meta.client.upload_file(file, BUCKET, obj[2])


def generate_keys(key_size=2048):

    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=2048
    )
    private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.PKCS8,
        crypto_serialization.NoEncryption())
    public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )

    return private_key, public_key

def lambda_handler(event, context):

    keys = generate_keys()

    with open("/tmp/private.key", 'wb') as content_file:
        os.chmod("/tmp/private.key", 400)
        content_file.write(keys[0])

    with open("/tmp/pub.key", 'wb') as content_file:
        os.chmod("/tmp/pub.key", 400)
        content_file.write(keys[1])
        
    upload_s3()