import boto3
from botocore.exceptions import ClientError
from django.conf import settings

class KMSUtils:
    @staticmethod
    def encrypt(data, algorithm='RSAES_OAEP_SHA_256'):
        kms = boto3.client('kms', region_name=settings.AWS_REGION)
        key_id = '5cd18f95-69a6-4430-b94f-6288766d2015'  # Replace with your RSA key ID

        try:
            response = kms.encrypt(
                KeyId=key_id,
                Plaintext=data.encode(),
                EncryptionAlgorithm=algorithm
            )
            print("Encrypt:", type(response['CiphertextBlob']))
            print(f"Encrypted data: {response['CiphertextBlob']}")
            return response['CiphertextBlob']
        except ClientError as e:
            print(f"Error encrypting data: {e}")
            return None

    @staticmethod
    def decrypt(ciphertext_blob):
        key_id = '5cd18f95-69a6-4430-b94f-6288766d2015'
        kms = boto3.client('kms', region_name=settings.AWS_REGION)
        
        print("Decrypt:",type(ciphertext_blob))
        print(f"Ciphertext blob: {ciphertext_blob}")
        try:
            algorithm='RSAES_OAEP_SHA_256'
            response = kms.decrypt(
                CiphertextBlob=ciphertext_blob,
                KeyId=key_id,
                EncryptionAlgorithm=algorithm,
            )
            print(f"Decrypted data: {response['Plaintext'].decode()}")
            return response['Plaintext'].decode()
        except ClientError as e:
            print(f"Error decrypting data: {e}")
            return None