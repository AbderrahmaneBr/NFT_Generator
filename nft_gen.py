from PIL import Image, ImageDraw
import random

def fill(img, r, g, b):
        pixels = img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if (pixels[x, y][3] != 0):
                    pixels[x, y] = (r, g, b)

def add(img1, img2):
    pixels_1 = img1.load()
    pixels_2 = img2.load()
    # Assuming the two images have the same size
    for x in range(img1.size[0]):
        for y in range(img1.size[1]):
            if (pixels_2[x, y][3] != 0):
                pixels_1[x, y] = pixels_2[x, y]
            

class NFT_Model:
    def __init__(self, canvas_size, name, num_to_gen, background, character, character_skin, character_upper_part):
        self.canvasSize = canvas_size
        self.name = name
        self.numToGen = num_to_gen
        self.background = background
        self.character = character
        self.characterSkin = character_skin
        self.characterUpperPart = character_upper_part

# GETTING ADDITIONAL INFORMATIONS
NFT_Model.name = input("What is the name of the NFT? \n> ")
NFT_Model.numToGen = int(input("How Many NFT do you want to Generate? \n> "))

# INITIALISATION PROCESS
# Background Init
NFT_Model.background = input("Please Enter The Background Layer Path: \n> ")
# Character Init
NFT_Model.character = input("Please Enter The Character Layer Path: \n> ")

# Character Skin
skin_choice = input("Does your character have a skin? (y/n): \n> ")
if (skin_choice == 'y'):
    NFT_Model.characterSkin = input("Please Enter Character's Skin Layer Path: \n> ")
else:
    NFT_Model.characterSkin = False

# Character Upper Part
upper_part_choice = input("Does your character have an upper part? (y/n): \n> ")
if (skin_choice == 'y'):
    NFT_Model.characterUpperPart = input("Please Enter Character Upper Part Layer Path: \n> ")
else:
    NFT_Model.characterUpperPart = False
  
# IMPORTING AND LOADING LAYERS PROCESS
image_background = Image.open(NFT_Model.background)
image_character = Image.open(NFT_Model.character)

if(NFT_Model.characterSkin!=False):
    image_characterSkin = Image.open(NFT_Model.characterSkin)

if(NFT_Model.characterUpperPart!=False):
    image_characterUpperPart = Image.open(NFT_Model.characterUpperPart)

# LAYERS PROCESSING
ext = input("Please choose an Extension(.png, .jpg...): ")

for i in range(0, NFT_Model.numToGen):

    fill(image_character, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if(NFT_Model.characterSkin!=False):
        fill(image_characterSkin, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if(NFT_Model.characterUpperPart!=False):
        fill(image_characterUpperPart, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    fill(image_background, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if(NFT_Model.characterSkin!=False):
        add(image_background, image_characterSkin)

    add(image_background, image_character)
    
    if(NFT_Model.characterUpperPart!=False):
        add(image_background, image_characterUpperPart)

    image_name = NFT_Model.name + '#' + str(i)
    image_background.save(image_name + ext)

    print("{} Generated Successfully!".format(image_name))

print("\nDone!")


