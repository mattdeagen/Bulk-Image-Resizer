from PIL import Image, ImageDraw
import os

# get paths for input and output folder
input_dir = os.getcwd() + '\input\\'
output_dir = os.getcwd() + '\output\\'
os.mkdir(output_dir)

dirs = os.listdir(input_dir)

def round_corners(im, rad=25):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def resize(width, height, rounded_corners=0, make_bw=0, add_resized=1):
    for item in dirs:
        if os.path.isfile(input_dir+item):
            im = Image.open(input_dir+item)
            item_name = item.split(".")
            im_resized = im.resize((width,height), Image.LANCZOS)
            # convert image to greyscale
            if(make_bw == 1):
                im_resized = im_resized.convert("L")
            # add rounded corners to resized image
            if(rounded_corners == 1):
                im_resized = round_corners(im_resized, 25)
            # add 'resized' to file name
            if(add_resized == 1):
                im_resized.save(f"{output_dir}{item_name[0]} resized.png", 'PNG', quality=90)
            else:
                im_resized.save(f"{output_dir}{item_name[0]}.png", 'PNG', quality=90)
    print("Finished. Go to the output folder to get resized images.")
            


print("Welcome to the Bulk Image Resizer.\n*Make sure all images to be resized are in the input directory\n\n")

desired_width = int(input("Please enter desired width: "))
desired_height = int(input("Please enter desired height: "))

rounded_corners = int(input("Would you like the corners rounded? [1]-yes [0]-no: "))

make_bw = int(input("Would you like the pictures to be black and white? [1]-yes [0]-no: "))

add_resized = int(input("Would you like the word \'resized\' to be added to the end of each file? [1]-yes [0]-no: "))

resize(desired_width, desired_height, rounded_corners, make_bw, add_resized)
