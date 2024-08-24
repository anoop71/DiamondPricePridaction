import smtplib
import schedule
import time

def schedule_and_send_email(from_address, to_address, subject, body, password, time_str):
    def send_email():
        email_message = f"Subject: {subject}\n\n{body}"
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_address, password)
            server.sendmail(from_address, to_address, email_message)
            server.quit()
            print(f"Successfully sent email message to {to_address}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    # Schedule the email to be sent at the specified time every day
    schedule.every().day.at(time_str).do(send_email)
    print(f"Email scheduled at {time_str} every day.")

    # Run the scheduler
    run_scheduler()

# Parameters
from_address = 'parv23155@gmail.com'
to_address = 'parvagarwal73@gmail.com'
subject = 'Scheduled Email'
body = 'This email was sent at a scheduled time.'
password = 'dckg ueoc wmsz vidg'
time_str = '10:44'  # Change to desired time in HH:MM format

# Call the function to schedule and send the email
schedule_and_send_email(from_address, to_address, subject, body, password, time_str)
