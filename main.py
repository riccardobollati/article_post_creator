import post_creator

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
image_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file

quote = [0,0]
quote[0] = input("type the sentence:\n")
quote[1] = input("type the author, if you don't want one leave blank and press enter:\n")

post = post_creator.create_post(image_path,quote)
post.save('post/post.png')