===============
RoboSitter
===============


A program for anyone who spends too much time on their computer.

Do you have bad posture and dry eyes from spending hours a day at your computer? 

This python script will help you track your screen time, remind you to take breaks, and even ask you to fix your posture


NOTE: developed and tested for MAC

------------
Usage
------------

TODO: write this section

------------
Dependencies
------------

-face_recognition --> pip install face_recognition  # Used to locate faces in video feed with CNN model

-opencv --> pip install opencv-python  # Used to launch and handle video feed 

-pync --> pip install pync  # Used to send MAC terminal notifications

------------
Features
------------
-Screen-time tracking using facial recognition. Encourages user to take 5 to 10 minute breaks after every 50 to 60 minutes of screentime.

-Sends user random reminders to fix their posture

------------
TODO
------------

Implement user profiles using face encodings

Implement a better and less hacky algorithm for deciding when a user should take a break

Implement visualization for screen-time tracking (graphs charts etc.)


------------
References
------------

Icon made by "https://www.flaticon.com/authors/freepik"
