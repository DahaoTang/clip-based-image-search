import torch
from PIL import Image
from tqdm import tqdm

import clip
from utils import *

model, preprocess = clip.load("RN50", device='cpu', jit=False)

image_list, caption_list = get_image_and_caption_list()

for image in tqdm(image_list):

    file_name = image.rstrip(".jpg") # Remove the ".jpg"

    data = preprocess(Image.open(image)).unsqueeze(0).to('cpu')

    with torch.no_grad():
        image_features = model.encode_image(data)
        file_name = file_name.strip("data/Images")
        torch.save(image_features, f'index/image/{file_name}.pt')
