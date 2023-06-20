from helper_functions import *
from flask import Flask, render_template, request, redirect, make_response, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('input_page.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Logic to handle the calculation
    user_birthday = request.form.get('user_birthday')
    partner_birthday = request.form.get('partner_birthday')
    connection_date = request.form.get('connection_date')
    user_more_time_together_date = get_more_time_together_date(user_birthday, connection_date)
    partner_more_time_together_date = get_more_time_together_date(partner_birthday, connection_date)

    return "When you will have spent more time with your partner than without: " + str(
        user_more_time_together_date) + ". When your partner will have spent more time with you than without: " + str(
        partner_more_time_together_date)


if __name__ == '__main__':
    #print(get_more_time_together_date(datetime(2002,8,24), datetime(2007,1,30)))
    app.run(debug=True)