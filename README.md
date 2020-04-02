# AWS-Cloud-Web-Controlled-Car
Nodejs server hosted on AWS EC2 instance, this is a website which has a login and registeration page using mongodb as database for controlling users and login to the main page. The main page of the website controls a raspberry pi which casts live video to the webpage, it also has two leds and four motors. The two stepper motors control yaw pitch and role of the camera and the other two DC motors drive a tank that the pi is attached too.

Cloud Computing Project

Title - Cloud Streamer
Neil Morrison
Description:
Cloud Based streaming camera which can also control pitch, yaw and roll of the camera, from a HTML page.
The server will be hosted on a Raspberry PI. 
The hardware will involve Raspberry PI, PI camera, 2 stepper motors and 2 stepper motor drivers.
The video stream will be hosted in the cloud using RTCP to transport the data.
The camera has an LDR to detect night and day which we can use to auto turn on by using the IR sensor built in.

Website
Our website is hosted on the EC2 instance of an AWS server. We have a total of 6 webpages that are linked together. The main page of our website is the first page that pops up, from there a user can navigate to the about page which describes our website and the project we are doing with a small paragraph and a diagram. When the user navigates back to the main page, he/she can navigate to either a login page or a registration page. The login page can navigate to either an admin page, where we can see users that are registered and delete Users from the Mongo dB database. If the user is not an admin and has been registered in the database, the user will be guided to a streaming page. The streaming page has a video stream from the raspberry pi and buttons which can drive the car the pi is attached to or tur the motors to adjust the camera on the pi. 

Camera
The Camera stream is streamed off the raspberry pi using motion streamer which broadcasts the stream, we pick the stream from the html page of EC2 instance and play it as a video using html. We have noticed that there is a delay of 1 to 2 milli seconds.

Buttons
The buttons on the streaming page are controlled by JavaScript code, the JavaScript’s connect to a remote socket server which is operating on the raspberry pi, the button presses are sent to the socket server in the form of strings. On the server side we have a dictionary of string, when the string is matched the value of that string is a function which will perform an operation on the motors of the car or the motors to control the yaw, pitch and roll of the camera. 
