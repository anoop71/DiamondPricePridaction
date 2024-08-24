from twilio.rest import Client

def send_sms(account_sid, auth_token, twilio_num, to_number, message_body):
    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # Send the SMS
        message = client.messages.create(
            body=message_body,
            from_=twilio_num,
            to=to_number
        )

        print(f"Message sent: {message.body}")

    except Exception as e:
        print(f"Failed to send SMS: {e}")

# Your Twilio account SID and Auth Token
account_sid = 'AC9d7cf318a1c101e8cbd511ab25060c7a'
auth_token = 'd126f4896c906ac6760be5e573b4d615'
twilio_num = '+17079690945'

# Get user input for phone number and message
to_number = input('Enter the phone number: ')
message_body = input('Enter the message: ')

# Call the function to send the SMS
send_sms(account_sid, auth_token, twilio_num, to_number, message_body)
