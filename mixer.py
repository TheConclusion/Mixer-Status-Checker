import urllib.request, json 
with urllib.request.urlopen("http://mixer.com/api/v1/users/[user id]") as url:
    data = json.loads(url.read().decode())
    
# insert user id you whish to track above in the [user id] part
# Make sure to remove the brackets as well

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
