import random
import urllib

def download_image(url):
    name = random.randrange(1,1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrive(url, fullname)

download_image("https://scontent.fblr11-1.fna.fbcdn.net/v/t1.0-9/s960x960/93421044_2599800636792189_1806457394952142848_o.jpg?_nc_cat=106&_nc_sid=dd9801&_nc_oc=AQmvTZgWANeWwXsCPyaoO0T-XIQt8L-LsdRdhnPk0zURHUA9BdQ7G_RcoA-gPijF3Mg&_nc_ht=scontent.fblr11-1.fna&_nc_tp=7&oh=317c51718cac7b32df7cb79588b4a02a&oe=5EDDD3A9")