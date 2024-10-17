from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import config
from eventLib import event

events = event('event.txt')

RECAPTHA_KEY = config.RECAPTCHA_SECRET_KEY
CHAT_ID = 727148312
EVENT_FILE = './event.txt'

app = Flask(__name__)
app.secret_key = 'some_random_secret_key'  # For flash messages

# Configure your email server (this example uses Gmail SMTP)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USERNAME = 'arturpetrov07@gmail.com'
PASSWORD = 'nnsv aybk jhyp xfsy'  # Use app-specific password if using Gmail 2FA

@app.route('/')
def contact():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        recaptcha_response = request.form['g-recaptcha-response']

        recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_data = {
            'secret': RECAPTHA_KEY,
            'response': recaptcha_response
        }

        recaptcha_request = requests.post(recaptcha_url, data=recaptcha_data)
        recaptcha_result = recaptcha_request.json()



        if recaptcha_result['success'] and recaptcha_result['score'] >= 0.5:
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = USERNAME
            msg['Subject'] = f"New message from {name}"

            # Email body content
            body = f"Name: {name}\enter/Email: {email}\enter/Message:\enter/{message}"

            # Send the email
            try:
                """server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                server.starttls()
                server.login(USERNAME, PASSWORD)
                text = msg.as_string()
                server.sendmail(email, USERNAME, text)
                server.quit()"""

                text = body
                print(text)
                events.TriggerEvent('sendMessage', text)

                flash("Your message has been sent successfully!", "success")
            except Exception as e:
                print(f"Error: {e}")
                flash("There was an issue sending your message. Please try again later.", "danger")

            return redirect(url_for('contact'))
        else:
            flash("reCAPTCHA verification failed. Please try again.", "danger")
            return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3666, debug=True)

