from flask import Flask, render_template, request, redirect, url_for
import requests
import config
from eventLib import event

events = event('event.txt')

RECAPTHA_KEY = config.RECAPTCHA_SECRET_KEY

app = Flask(__name__)

@app.route('/')
def contact():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
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

            # Email body content
            body = f"Name: {name}\enter/Email: {email}\enter/Message:\enter/{message}"

            # Send the email
            try:
                text = body
                print(text)
                events.TriggerEvent('sendMessage', text)
            except Exception as e:
                print(f"Error: {e}")

            return redirect(url_for('contact'))
        else:
            return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3666, debug=True)

