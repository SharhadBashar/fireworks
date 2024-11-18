import json

from classes import *
from constants import *

prompt_fireworks = '''
[ROLE]
You are a helpful assistant that extracts information from images. You have a keen eye for details, and can extract and determind what each key piece of imfornation is.

[INSTRUCTIONS]
You will follow the following set of rules:
1. You will be given either a passport or a license. 
2. First, determine if it is a passport or a license.
3. If its a passport, extract the following information from the image: {}
4. Else if its a license, extract the following information from the image:{}
5. Do not extract any information that is not listed above. This includes 'donor', 'veteran'

[OUTPUT]
Return 2 things:
1. The type of document it is (passport or license)
2. The information in JSON format. If you cannot find a particular piece of information, return None for that field.
'''.format(list(Passport.model_fields), list(License.model_fields))

def openai_prompt(information):
    return [
        {
            'role': 'system',
            'content': '''
                [ROLE]
                You are a helpful assistant that extracts information from text. You have a keen eye for details, and can extract and determind what each key piece of imfornation is.

                [INSTRUCTIONS]
                You will follow the following set of rules:
                1. You will be given a piece of text.
                2. Extract the following information from the text: {}
                3. Do not extract any information that is not listed above. This includes 'donor', 'veteran'

                [OUTPUT]
                Return the information in JSON format. If you cannot find a particular piece of information, return None for that field.
            '''.format(list(Identity.model_fields))
        }, 
        {
            'role': 'user',
            'content': information
        }
    ]