import os 
import imageio
from PIL import Image

def resize_images(images_folder, size=(200, 200)):
    image_files = [os.path.join(images_folder, file) for file in os.listdir(images_folder) if file.endswith(('png', 'jpg', 'jpeg'))]

    resized_images = []
    for file_name in sorted(image_files):
        img = Image.open(file_name)
        img_resized = img.resize(size, Image.ANTIALIAS)  # Resize to specified size
        resized_images.append(img_resized)

    return resized_images

def create_gif(images_folder, gif_path):
    resized_images = resize_images(images_folder)
    imageio.mimsave(gif_path, resized_images, duration=0.2)  # Adjust duration between frames as needed


if __name__ == "__main__":
    images_folder_path = 'test_video'  # Replace this with your image folder path
    output_gif_path = 'output.gif'

    create_gif(images_folder_path, output_gif_path)
