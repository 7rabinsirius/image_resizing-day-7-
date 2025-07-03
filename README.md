# image_resizing-day-7-

# 🖼️ Bulk Image Resizer with Python

This project is a simple yet powerful script that resizes all images in a specified folder to a uniform size (600x400 pixels by default) using the [Pillow](https://python-pillow.org/) library. It's perfect for batch-processing images for web uploads, games, or machine learning datasets.

## 📂 Features

- Automatically processes all images in the `sample_images` folder
- Resizes each image to 600x400 resolution
- Saves resized images to a separate `resized_images` folder
- Creates output directory if it doesn't exist
- Robust error handling for missing files or bad images

## 📦 Requirements

- Python 3.x
- Pillow (Python Imaging Library fork)

Install Pillow using pip:

```bash
pip install Pillow
```

## 🚀 How to Use

1. Place all the original images into the `sample_images/` folder.
2. Run the script:
   ```bash
   python resize_images.py
   ```
3. Resized images will be saved to the `resized_images/` folder.

## 🔧 Customization

You can change:
- Input/output folder names
- Target size (currently `(600, 400)`)
- File naming pattern (e.g., add timestamp or preserve original names)

## 🧠 How It Works

The script:
- Reads filenames from the input directory
- Resizes each image to a fixed size
- Handles errors gracefully if files are missing or unreadable
- Saves all resized images in a clean output directory

## 🛡️ Error Handling

- Skips non-image files (you can add a filter with `str.endswith()` for safety)
- Prints clear messages for missing directories or corrupted images

## 📁 Example Directory Structure

```
project_root/
│
├── sample_images/
│   ├── image1.jpg
│   └── image2.png
│
├── resized_images/
│   └── sample_resized1.jpg
│
└── resize_images.py
```


