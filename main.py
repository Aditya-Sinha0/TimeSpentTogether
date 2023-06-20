from helper_functions import *
from flask import Flask, render_template, request, redirect, make_response, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('input_page.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Logic to handle the calculation
    birthday = request.form.get('birthday')
    connection_date = request.form.get('connection_date')
    print(birthday)
    return str(get_more_time_together_date(birthday, connection_date))


if __name__ == '__main__':
    #print(get_more_time_together_date(datetime(2002,8,24), datetime(2007,1,31)))
    app.run(debug=True)