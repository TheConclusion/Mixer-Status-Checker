@echo off

title Mixer - Data Dashboard

if exist autorun.txt (
goto :START
) else (
goto :MAIN
)

:MAIN

@echo. 
@echo  -- Mixer Account Tracker --
@echo        Motd/Bulletin
@echo. 
@echo  Mixer stat tracker requires a stable internet connection to run.
@echo  Please make sure you are running Python 3.7 or above 
@echo. 
@echo. 
@echo  -- all rights belong to Mixer, 2019 --
@echo. 
PAUSE

cls

REM Insert the setup.py file location below (Make sure not to move this file)
REM Make sure to have a recent version of python istalled [3.0 or higher]

:SETUP

setup.py


:AUTORUN


:START

cls

REM Insert the core.py file location below (Make sure not to move this file)
REM Make sure to have a recent version of python istalled [3.0 or higher]

core.py REM replace core.py with the location of the folder if issues occur.

TIMEOUT /T 60 

GOTO START
