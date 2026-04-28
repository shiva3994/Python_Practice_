""" MODULES TO BE USED """
#Twilio
#Datetime module
#Time 
""" STEPS TO BE TAKEN """
## Twilio client set up
## User inputs
## Schdeuling logic
## Send message
""""""

## STEP 1 :: INSTALLED REQUIRED LIBRARIES
from twilio.rest import Client
from datetime import datetime, timedelta
import time

## STEP 2 :: TWILIO CREDENTIALS
account_sid = 'XXXXXX'
auth_token = 'XXXXXX'

client = Client(account_sid, auth_token)

## STEP 3 :: SEND MESSAGE FUNCTION
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to = f'whatsapp:{recipient_number}')
        print(f'Message sent sucessfully! Message SID {message.sid}')
    except Exception as e:
        print('An error occured')

## STEP 4 :: USER INPUT
name = input('Enter the recepient name = ')
recipient_number = input('Enter the recipient Whatsapp number with country code (e.g. +91 ): ')
message_body = input(f'Enter the message you want to send to {name}: ')

## STEP 5 :: DATE/TIME AND CALCULATE DELAY
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24 Hours format): ')

#DATETIME 
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#CALCULATE DELAY
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time: ')
else:
    print(f'Message scheduled will be sent to {name} at {schedule_datetime}.')

    #WAIT TILL SCHEDULED TIME
    time.sleep(delay_seconds) #MSSG WILL WAIT FOR 1000 SECONDS

    #SEND MESSAGE
    send_whatsapp_message(recipient_number, message_body)