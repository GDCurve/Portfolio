from flask import Flask, request, jsonify, render_template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import requests

aplikacija = Flask(__name__)

with open('pass.txt', 'r') as noslepumi:
    RECAPTCHA_SECRET_KEY = noslepumi.readline()
    EMAIL_PASSWORD = noslepumi.readline()

EMAIL_ADDRESS = 'emils.sangovics@gmail.com'

@aplikacija.route('/')
def index():
    return render_template('index.html')

@aplikacija.route('/send-email', methods=['POST'])
def send_email():
    email = request.form['email']
    message = request.form['message']
    recaptcha_response = request.form['g-recaptcha-response']

    recaptcha_verification = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={'secret': RECAPTCHA_SECRET_KEY, 'response': recaptcha_response}
    ).json()

    if not recaptcha_verification.get('success'):
        return jsonify({'message': 'captcha nesagaja'}), 400

    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = 'jauns ziņojums'

        body = f"epasts: {email}\n\nzina:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)


        return jsonify({'message': 'ziņa nosūtīta'}), 200

    except Exception as e:
        print(e)
        return jsonify({'message': 'nesanāca kautkas'}), 500

if __name__ == '__main__':
    aplikacija.run(debug=True)
