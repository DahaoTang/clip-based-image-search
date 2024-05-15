# CLIP-based Image Search

-- 2024 May Personal Project

## Introduction

This personal project develops a straightforward image search application using CLIP, which matches images in a database to user-provided descriptions. The application is deployed through a simple Next.js-based website interface.

https://github.com/DahaoTang/clip-based-image-search/assets/87845979/9e861772-b175-49fe-9118-1d89740094de


## Setup Instructions

### Preparation

1. **Download Data:** Acquire the dataset from the open-source Flickr 8k Dataset available at [Flickr 8k Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k).
2. **Rename Database:** Change the folder name from "archive" to "data" and copy it into the `./backend` and `/frontend/public` directories.
3. **Folder Structure:** Within `./backend`, create the directory structure `index/image`. Ensure that `image` is an empty folder at `./backend/index`.
4. **Install Necessary Tools:** Ensure [npm](https://www.npmjs.com/) and [pipenv](https://pipenv.pypa.io/en/latest/) are installed on your local machine.

### Installation

1. **Python Environment:** Navigate to `./backend` and initiate a Python virtual environment by running `pipenv shell`.
2. **Install Dependencies:** Execute `pipenv install` to install all necessary Python dependencies.
3. **Data Conversion:** Run the `setup.py` Python script to convert the dataset into `.pt` files. Note that this process might take over 30 minutes.

### Execution

- **Frontend:** Proceed to `./frontend` and execute `npm run dev` to start the frontend.
- **Backend:** In `./backend`, run `python3 main.py` to launch the backend.
