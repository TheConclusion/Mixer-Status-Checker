import os, time
import importlib
import urllib.request, json 

fo = open("config.txt", "r+")
name = fo.read(10);

url = "https://mixer.com/api/v1/channels/" + (name)

fo.close()

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

realurl = "https://mixer.com/api/v1/users/" + str(data["userId"])

fo = open("fallback.json", "w")
with urllib.request.urlopen(realurl) as url:


    data = json.loads(url.read().decode())
fo.write(str(data))
fo.close()

print ('')   	
print ('-- Mixer Account Tracker --')

print ('')
print ('')
print ('')

print (' ' + ('Currently tracking:' + (' ' + (data["username"] + (' (' + str(data["id"]) + (')'))))))

print ('')

print (' User is ' + ('Level:' + (' ') + str(data["level"]) + (' ') + ('and has') + (' ') + str(data["experience"]) + (' ') +  ('experience points.')))
			
print ('')

print (' User (' + (data["username"] + (') ') + ('currently owns') + (' ') + str(data["sparks"]) + (' ') + ('sparks')))

print ('')
print ('')
print ('')

print ('-- all rights belong to © Mixer, 2019 --')


print ('')
print ('')
print ('')
print ('')
print ('')
print ('')
print ('')
print ('')
print ('')

print ('The stats will automaticaly update every 60 seconds')

print ('')
print ('')
