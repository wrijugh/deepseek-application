# This script demonstrates how to use the ChatCompletionsClient to interact with the deployed model
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
endpoint = os.getenv("DEPLOYMENT_ENDPOINT")
model_name = os.getenv("DEPLOYMENT_MODEL_NAME")
token = os.getenv("DEPLOYMENT_TOKEN")

print(endpoint)

# Create a ChatCompletionsClient
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def get_response(query): 
    response = client.complete(
        stream=True,
        messages=[
            UserMessage(content=query),
        ],
        model=model_name,
    )
    return response


# full_response = ""
# response_container = st.empty()
# for update in response:
#     if update.choices:
#         if update.choices and update.choices[0].delta.content:
#             full_response += update.choices[0].delta.content
#             response_container.markdown(full_response) #update incrementally

# client.close()