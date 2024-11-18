To run the code, run the following command:
```
python main.py -i <image_path> -st <structured>
```
where `<image_path>` is the path to the image you want to run inference on, and `<structured>` is a boolean value (True or False) to determine if you want to run the structured inference with OPEN AI or not, since fireworks does not have structured output support yet.

Make sure to set the `OPENAI_API_KEY` and `FIREWORKS_API_KEY` either in the environment variables or in the `config/open_ai.json` and `config/fireworks.json` files.