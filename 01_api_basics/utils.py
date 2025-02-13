from ./consts import *

def get_model_response(messages):
    bedrock_client = boto3.client(service_name=SERVICE_NAME,region_name=REGION_NAME)

    # Send the message.
    response = bedrock_client.converse(
        modelId=MODEL_ID
        messages=messages,
    )

    return response["output"]["message"]["content"][0]["text"]