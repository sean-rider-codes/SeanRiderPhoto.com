import os

url = 'E:\Libraries\Documents\GitHub\SeanRiderPhoto.com\Galleries\Flooz2Img\ '[:-1]

entries = os.listdir(url)

for entry in entries:
    print('<div class = "cell><img id ="'+entry+'" src ="'+url+entry+'" alt ="'+entry+'" class="responsive></div>')