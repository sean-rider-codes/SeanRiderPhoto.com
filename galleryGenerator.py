import os

url = 'E:\Libraries\Documents\GitHub\SeanRiderPhoto.com\img\other\ '[:-1]

entries = os.listdir(url)

for entry in entries:
    print('<div class = "gcell"><img id ="'+entry+'" src ="'+url+entry+'" alt ="'+entry+'" class="responsive"></div>')