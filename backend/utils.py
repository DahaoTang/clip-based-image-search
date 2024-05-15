import torch

import clip


def get_image_and_caption_list(caption_txt_file_path="data/captions.txt"):
    """
        The function will read the captions.txt file and 
        retrieve the information provided by the database and return them as two lists.

        Param:
            caption_txt_file_path: the path to captions.txt 

        Return:
            Two lists, one for the paths of all the images, 
            the other one for the description for each of the image.
    """

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
    """
        Uses the CLIP model to find images most similar to a given caption. It returns a specified number of images
        that best match the user's description.

        Param:
            user_caption: the description for the image wanted, provided by the user
            count: the number of images wanted
            image_list: the list containing the paths of all the images
        
        Return:
            List of images produced by CLIP.

    """
    device = 'cpu'
    model, preprocess = clip.load("RN50", device=device, jit=False)

    # Load and preprocess images
    image_features = []
    for image_path in image_list:
        image_name = image_path.rstrip(".jpg").strip("data/Images")
        image_pt = torch.load("index/image/" + image_name + ".pt", map_location=device)
        image_features.append(image_pt)
    image_tensors = torch.stack(image_features).float()
    image_tensors /= image_tensors.norm(dim=-1, keepdim=True)

    # Tokenize uer caption to retrieve feature
    text_tokens = clip.tokenize([user_caption]).to(device)
    text_features = model.encode_text(text_tokens).float()

    # Calculate similarity
    similarity = (100.0 * image_tensors @ text_features.T).softmax(dim=0)

    # Selected top ones
    top_values, top_indices = similarity.squeeze().topk(count)

    # Get paths of images to return
    result_images = [image_list[idx] for idx in top_indices.tolist()]

    return result_images