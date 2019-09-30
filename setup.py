import os, time

print ('')   	
print ('-- Mixer Account Tracker --')
print ('         Set-Up           ')  
print ('')   		
print (' Enter the Mixer username you wish to track ')
print ('')   	
var = input(' Username = ')

fo = open("config.txt", "w")
fo.write((var))

fo.close()

cls = lambda: os.system('cls')
cls()
