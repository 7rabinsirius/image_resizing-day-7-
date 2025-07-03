from PIL import Image
import os

folder_path = "sample_images"
output_folder = "resized_images"
os.makedirs(output_folder, exist_ok=True)

try:
    file_list = os.listdir(folder_path)

    for i, filename in enumerate(file_list):
        file_path = os.path.join(folder_path, filename)  
        try:
            img = Image.open(file_path)

            new_size = (600, 400)
            resized_image = img.resize(new_size)

            output_path = os.path.join(output_folder, f"sample_resized{i + 1}.jpg")
            resized_image.save(output_path)

        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")

except FileNotFoundError:
    print("Error: The specified directory does not exist.")
except NotADirectoryError:
    print("Error: The specified path is a file, not a directory.")