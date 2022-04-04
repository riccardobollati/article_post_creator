from PIL import Image 

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def logo_creator(simple_logo,schizzo,new_col):

    #applicare colore allo schizzo

    rgb_new_col = hex_to_rgb(new_col)

    image = Image.open(schizzo)
    pixelMap = image.load()
    newImg = Image.new(image.mode,image.size)
    pixelsNew = newImg.load() 
    width,height = newImg.size
    
    for i in range(width): 
        for j in range(height):
            pixelsNew[i,j] = pixelMap[i,j]

            if pixelMap[i,j][3] > 50 and pixelMap[i,j][0] < 255:
                pixelsNew[i,j] = rgb_new_col
                
    #unione logo e schizzo
    logo_post = Image.open(simple_logo)
    logo_post.paste(newImg,(0,0),newImg)

    return logo_post
