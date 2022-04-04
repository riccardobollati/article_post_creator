import os
import post_creator

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
image_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file

quote = "cojosdnvoefn vjinvjn ffre fe rf erf er fer ferfesgewr g rgergfwregerfdf"

post = post_creator.create_post(image_path,quote)
post.save('post/post.png')