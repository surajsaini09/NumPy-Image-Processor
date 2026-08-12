
from image_processor import load_image

img = load_image("images/123.jpg")

print(type(img))
print(img.shape)
print(img.dtype)

from image_processor import show_image
show_image(img)

from image_processor import convert_grayscale
grayscale_img = convert_grayscale(img)
show_image(grayscale_img)

from image_processor import adjust_brightness

adjust_brightness_img = adjust_brightness(grayscale_img, 0.5)
show_image(adjust_brightness_img)

from image_processor import flip_image
flipped_img = flip_image(grayscale_img, 'horizontal')
show_image(flipped_img)
