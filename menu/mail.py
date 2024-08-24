import smtplib

def send_email(sender_email, sender_password, recipient_email, message):
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message)

        print('Mail sent successfully.')

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection to the SMTP server
        server.quit()

# Sender email credentials
sender_email = 'parv23155@gmail.com'
sender_password = 'dckg ueoc wmsz vidg'

# Recipient email and message
recipient_email = 'parvagarwal73@gmail.com'
message = 'Hello friend'

# Call the function to send the email
send_email(sender_email, sender_password, recipient_email, message)
