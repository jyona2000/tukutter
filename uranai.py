from flask import Flask ,request

application = Flask(__name__)

@application.route('/uranai', methods=['POST'])
def uranai():
    text = request.form['name']

    if text == "taro" :
        return "dakiti"

    else:
        return "kiti"
