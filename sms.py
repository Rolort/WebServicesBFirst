import boto3

def sendSMS(text, phoneNumber):
    try:
        CompText = text + " es tu código de verificación de BFirst"
        client = boto3.client(
        "sns",
        aws_access_key_id = "AKIAXJRFWVWW53ZDRPED",
        aws_secret_access_key = "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",
        region_name = "eu-west-1"
        )

        client.publish(
        PhoneNumber = phoneNumber,
        Message = CompText
        )
        return True
    except Exception as e:
        print (e)
        print (e.args[0])
        return False
