import os
import json
from openai import OpenAI
import fireworks.client

from classes import Identity
from constants import *

class LLM:
    def __init__(self, open_ai_model = 'gpt-4o-mini'):
        openai_api_key = os.environ.get('OPENAI_API_KEY')
        if not openai_api_key:
            with open(os.path.join(PATH_CONFIG, OPEN_AI_CONFIG), 'r') as file:
                openai_api_key = json.load(file)['key']
        self.client = OpenAI(
            api_key = openai_api_key
        )
        self.model = open_ai_model
        self.model_4o = 'gpt-4o-2024-08-06'
        fireworks_api_key = os.environ.get('FIREWORKS_API_KEY')
        if not fireworks_api_key:
            with open(os.path.join(PATH_CONFIG, FIREWORKS_CONFIG), 'r') as file:
                fireworks_api_key = json.load(file)['key']
        self.fireworks_client = fireworks.client.Fireworks(
            api_key = fireworks_api_key
        )

    def chat_completion_structured_output_openai(self, messages, structure = Identity):
        response = self.client.beta.chat.completions.parse(
            model = self.model,
            messages = messages,
            response_format = structure
        )
        return response.choices[0].message.parsed
    
    def chat_completion_fireworks(self, message, image, structure = Identity):
        response = self.fireworks_client.chat.completions.create(
            model = "accounts/fireworks/models/phi-3-vision-128k-instruct",
            messages = [{
                "role": "user",
                "content": [{
                    "type": "text",
                    "text": message,
                }, {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image}"
                    }
                }],
            }]
        )
        return response.choices[0].message.content
