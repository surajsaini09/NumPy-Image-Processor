from PIL import Image
import numpy as np 

def load_image(image_path): 
    with Image.open(image_path) as img: 
        return np.array(img)

def show_image(img):
        img = Image.fromarray(img)
        img.show()

def convert_grayscale(img):
    if len(img.shape) == 3 and img.shape[2] == 3:
        return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    else:
        raise ValueError("Input image must be a color image with 3 channels.")
    
def adjust_brightness(img, factor):
    if len(img.shape) == 2:  # Grayscale image
        return np.clip(img * factor, 0, 255).astype(np.uint8)
    elif len(img.shape) == 3 and img.shape[2] == 3:  # Color image
        return np.clip(img * factor, 0, 255).astype(np.uint8)
    else:
        raise ValueError("Input image must be either a grayscale or color image.")
     
def flip_image(img, direction):
    if direction == 'horizontal':
        return np.flip(img, axis = 0)
    elif direction == 'vertical':
        return np.flip(img, axis=0)
    else:
        raise ValueError("Direction must be either 'horizontal' or 'vertical'.")
    
