#Media processing functions (Picture and Video) for Conflict Gateway Scrapers.

#detect operating system to avoid PIL Import error
import os
system = os.name
if system == "nt":
    import Image, ImageOps
elif system == "posix":
    from PIL import Image, ImageOps
      
import boto
from boto.s3.key import Key
import uuid
import urllib2 as urllib
import requests
import cStringIO
from StringIO import StringIO
import hashlib
import re
import socket
import string
import random


#Amazon web services configuration (via boto module)
s3 = boto.connect_s3("USER",
                     "KEY")
b = s3.get_bucket('BUCKNAME')

#random image name generator
def image_name_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))

#trim the profile img and upload to s3 bucket
def uploadImg(image):
    try:
        newname = image_name_generator()
        'grab image from the net and save temp'
        r = requests.get(image)
        tmp_image = Image.open(StringIO(r.content))
        tmp_image_path = "" + newname + ".png"
        tmp_image.save(tmp_image_path)
        'resize'
        im = Image.open(tmp_image_path)
        size = 400, 400
        imsize = ImageOps.fit(im, size, Image.ANTIALIAS)
        im.save(tmp_image_path, "PNG")
        'Save img to S3'
        k = Key(b)
        k.key = "img/thumbs/" + newname + ".png"
        k.set_contents_from_filename(tmp_image_path, policy='public-read')
        k.set_acl('public-read')
        'delete tmp file'
        os.remove(tmp_image_path)    
        status = newname + ".png"     
    except:
        status = "newsthumb.png"
    return status


