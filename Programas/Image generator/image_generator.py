import os

import openai
import requests


def create_images(text, name):
    name = name + '.png'
    openai.api_key = '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'
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']

    image_response = requests.get(image_url)
    # download image
    if image_response.status_code == 200:
        with open(f'imgs/{name}', 'wb') as file:
            file.write(image_response.content)
        print('image saved!!')
    else:
        print("image not downloaded")

    return f'images/{name}'


if __name__ == "__main__":
    img = create_images(" a white siamese cat", 'cat')
