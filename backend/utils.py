import torch

import clip


def get_image_and_caption_list(caption_txt_file_path="data/captions.txt"):

    image_list = []
    caption_list = []

    lines = []
    with open(caption_txt_file_path, "r") as f:
        # Read in the image name and its caption, then remove the header
        lines = f.readlines()[1:]

        for line in lines:
            line = line.rstrip("\n").split(",")
            image_list.append(f"data/Images/{line[0]}")
            caption_list.append(line[1])

    return image_list, caption_list


def get_image_from_caption(user_caption, count, image_list, plot_or_not=False):
    device = "cpu"
    model, preprocess = clip.load("RN50", device=device, jit=False)

    # Load and preprocess image data
    image_data = torch.stack([torch.load(
        'index/image/'+i.rstrip('.jpg').strip('data/Images')+'.pt', map_location=device) for i in image_list])
    image_data /= image_data.norm(dim=-1, keepdim=True)

    # Tokenize and encode the text caption
    text_features = torch.cat([clip.tokenize(f"{user_caption}")]).to(device)
    text_features = model.encode_text(text_features)
    text_features = text_features.to(device)

    # Reshape and convert image data
    image_data = image_data.reshape(image_data.shape[0], image_data.shape[-1])
    image_data = image_data.float()
    text_features = text_features.float()

    # Calculate similarity and get top images
    similarity = (100.0 * image_data @ text_features.T)
    similarity = similarity.reshape(-1).softmax(dim=-1)
    values, indices = similarity.topk(count)
    result_image = [image_list[i] for i in indices.numpy().tolist()]

    return result_image
