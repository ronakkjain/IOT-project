#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import smtplib

 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
smtp_message="Hi Maulik, Please water your plants."
def callback(channel):
        if GPIO.input(channel):
            try:
                print ("Water Detected!")
            except smtplib.SMTPException:
                print("unable to send mail")
        else:
                connection=smtplib.SMTP('smtp.gmail.com', 587)
                connection.ehlo()
                connection.starttls()
                connection.login('shabbshabb1986@gmail.com','Shabb@1986')
                connection.sendmail('shabbshabb1986@gmail.com','maulikm.96@gmail.com',smtp_message)
                connection.quit()
                print ("No Water Detected!")
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)

