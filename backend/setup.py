import torch
from PIL import Image
from tqdm import tqdm

import clip
from utils import get_image_and_caption_list

# Load the CLIP model with specified settings
model, preprocess = clip.load("RN50", device='cpu', jit=False)

# Retrieve lists of image paths and captions
image_list, caption_list = get_image_and_caption_list()

# Process each image in the list
for image_path in tqdm(image_list):
    # Construct file name for storing processed image features
    file_name = image_path.split('/')[-1].replace(".jpg", "")

    # Open and preprocess the image
    image_data = Image.open(image_path)
    processed_image = preprocess(image_data).unsqueeze(0).to('cpu')

    # Encode image to extract features
    with torch.no_grad():
        image_features = model.encode_image(processed_image)
        # Save the image features to disk
        torch.save(image_features, f'index/image/{file_name}.pt')
