# Identity Extraction from Documents using Fireworks

First install the requirements:
```
pip install -r requirements.txt
```

To run the code, run the following commands:
```
python main.py -i <image_path> -st <structured>
```
where `<image_path>` is the path to the image you want to run inference on, and `<structured>` is a boolean value (True or False) to determine if you want to run the structured inference with OPEN AI or not, since fireworks does not have structured output support yet.

Make sure to set the `OPENAI_API_KEY` and `FIREWORKS_API_KEY` either in the environment variables or in the `config/open_ai.json` and `config/fireworks.json` files.

## Instructions:

**Context/Setup** 
You are working with a FSI enterprise for their KYC process. As part of this PoV, the Enterprise wants to create a solution for Identity Verification across various types of documents such as Passports & Drivers license. 

**Task**
 Your task is to use Firework AI’s platform & APIs to provide an end-to-end PoV solution.  
Fireworks Documentation: https://docs.fireworks.ai/
Please create an account and an API token to use with the solution.  If you require more credits, please contact the recruiter and we should be able to add them to your account.
Input Documents: https://drive.google.com/drive/u/0/folders/1GNyJZ8bluOg_TBuYFfrSsE4WfRsLYEcN
Language: You have choose a language of your choice

**Goal**
A PoC that extracts out the relevant information required for identity verification.
For the output, you should explain why certain design choices were made and their tradeoffs in the end-to-end process. 

**Time Limit**
24 hours
