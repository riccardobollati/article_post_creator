from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import math

import dominant_color
import post_logo_creator

def create_post(img_base,text):

    #parameters
    base_size = 70
    #text max width
    max_w = 800
    
    #find main color in HEX format
    main_color = dominant_color.find_color(img_base)
    print(f'main color: {main_color}')
    post = Image.open(img_base)
    cover = Image.open("raw/post_cover.png")

    #resize image
    size = post.size
    if size[0]!=size[1]:
        
        area = (0, 0, min(size), min(size))
        post = post.crop(area)

    post = post.resize((1080,1080),Image.ANTIALIAS)

    #apply filter
    post.paste(cover,(0,0),cover)


    #quote writing -------------------------------------------------------------------------------------------
    #quote
    quote = text[0]
    #author
    if text[1] :
        author = text[1]
    else:
        author = False

    draw = ImageDraw.Draw(post)
    
    if len(quote) > 68:
        font_size = int(base_size -  (math.log( ((len(quote)-9)**39),6)-88))
    else:
        font_size = base_size

    font = ImageFont.truetype("fonts/AvenirLTStd-Black.otf", font_size)
                                           

    print(f'font size : {font_size}\n')
    
    #text size (if one line)
    text_size = draw.textsize(quote, font=font)

    #text division
    if text_size[0] > max_w:

        splitted_quote = quote.split(' ')
        multiline_quote = []

        i = 0
        
        while len(splitted_quote)-(i):

            line = splitted_quote[i]

            if (len(splitted_quote) - i) > 2: 

                if len(splitted_quote)-(i+1) != 1:
                    while draw.textsize(line, font=font)[0] < 600:                                      

                        if draw.textsize((line + f' {splitted_quote[i+1]}'), font=font)[0] < 600:

                            line = line + f' {splitted_quote[i+1]}'
                            i = i+1
                        else:
                            i = i+1
                            line = line + '\n'
                            break
                    multiline_quote.append(line)
                    del line
                else:
                    i=i+1
        
            else:
                multiline_quote.append(line)
                i=i+1
    
    quote = ' '.join(multiline_quote)
    divided_quote = quote

    #text size
    text_size = draw.multiline_textsize(divided_quote, font=font, spacing=(font_size/2.5))

    #text coordinates
    text_x = 540 - text_size[0]/2
    text_y = 540 - text_size[1]/2

    #print text
    draw.multiline_text((text_x,text_y), divided_quote ,(255,255,255),font=font, align = 'center', spacing=(font_size/2.5))

    #divider
    divider_thickness = 2
    
    #divider coordinates
    div_x_1 = 540 - text_size[0]/2
    div_y_1_1 = 540 - (text_size[1]/2 + divider_thickness + 15)
    div_y_1_2 = 540 + (text_size[1]/2 + divider_thickness + 20)

    div_x_2 = div_x_1 + text_size[0]
    div_y_2_1 = div_y_1_1 + divider_thickness
    div_y_2_2 = div_y_1_2 + divider_thickness
    
    #draw dividers
    draw.rectangle([div_x_1,div_y_1_1,div_x_2,div_y_2_1], fill= 'white')
    draw.rectangle([(div_x_1 + ((div_x_2 - div_x_1)/8)),div_y_1_2,(div_x_2-((div_x_2 - div_x_1)/8)),div_y_2_2], fill= 'white')

    #apply logo
    logo = post_logo_creator.logo_creator('raw/m_per_post.png','raw/schizzo_su_m_per_post.png',main_color)
    logo = logo.resize((int(logo.size[0]/1.5),int(logo.size[1]/1.5)),Image.ANTIALIAS)
    
    #coordinate logo
    x_logo = int(540 - logo.size[0]/2)
    y_logo = int(text_y - 80)

    post.paste(logo,(x_logo,y_logo),logo)

    #add author
    if author:
        
        font = ImageFont.truetype("fonts/LFAXD.ttf", 25)
        #author coordinates
        author_x = 540 - draw.textsize(author, font=font)[0]/2
        author_y = div_y_2_2 + 10

        draw.text((author_x,author_y), f'~{author}~' ,(255,255,255),font=font, align = 'center')

    return post
