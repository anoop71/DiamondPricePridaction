import pywhatkit

def send_whatsapp_message(phone_number, message):
    try:
        # Send the WhatsApp message instantly
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        print("Message sent successfully.")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Parameters for sending the message
phone_number = "+916350249258"  # Replace with the recipient's phone number
message = "Hello, this is a test message"  # Replace with your message

# Call the function to send the WhatsApp message
send_whatsapp_message(phone_number, message)
