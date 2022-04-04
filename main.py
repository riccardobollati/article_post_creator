import os
from tkinter import image_names
import post_creator

quote = "cojosdnvoefn vjinvjn ffre fe rf erf er fer ferfesgewr g rgergfwregerfdf"

post = post_creator.create_post("pics\ok_prova.jpg",quote)
post.save('post/post.png')