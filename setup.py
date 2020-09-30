import os, time

print ('')   	
print ('-- Mixer Account Tracker --')
print ('         Set-Up           ')  
print ('')   		
print (' Enter the Mixer username you wish to track ')
print ('')   	
var = input(' Username = ')
print ('')  
	
cls = lambda: os.system('cls')
cls()

print ('')   	
print ('-- Mixer Account Tracker --')
print ('         Set-Up           ')  
print ('')   		
print (' Do you want to turn on autorun mode, this will skip the bulletin and setup. ')
print (' You will be unable to change the username to track ')
print ('')  
print (' Note: please only enable if you know what you are doing. ')
print ('')
answer = input("Please enter y/n ")
print ('') 

if answer == "y":
   fo = open("autorun.txt", "w")
   fo.write("autorun is enabled ( remove this file to turn it off ) ")

fo = open("config.txt", "w")
fo.write((var))
fo.close()

cls()