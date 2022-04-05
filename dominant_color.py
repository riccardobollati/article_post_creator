from __future__ import print_function
import binascii
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

def find_color(path) :
    
    NUM_CLUSTERS = 5

    print('reading image...')
    im = Image.open(path)
    im = im.resize((150, 150))      #optional, to reduce time
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

    print('finding clusters...')
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         #assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    #count occurrences
    
    index_max = scipy.argmax(counts)                    #find most frequent
    peak = codes[index_max]

    colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    
    return colour