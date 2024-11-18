import json
import argparse

from llm import LLM
from prompt import *
from classes import *
from helper import encode_image


def main(image_path, structured):
    llm = LLM()
    image = encode_image(image_path)
    information = llm.chat_completion_fireworks(prompt_fireworks, image)
    print('----------------------------------')
    print(information.strip())
    print('----------------------------------')
    if structured:
        information = llm.chat_completion_structured_output_openai(openai_prompt(information), Identity)
        print(information)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Process an image path.')
    parser.add_argument('-i', '--image_path', type = str, help = 'Path to the image file')
    parser.add_argument('-st', '--structured', type = bool, help = 'Whether to output structured data with a second OpenAI call', default = False)
    args = parser.parse_args()

    print('Input image path:', args.image_path)
    main(args.image_path, args.structured)
