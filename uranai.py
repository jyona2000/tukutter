from flask import Flask ,request ,render_template

application = Flask(__name__)

@application.route('/show_uranai')
def show_uranai():
    text = request.form['name']
    html = render_template('uranai.html', name=name)
    print(html)
    return html

@application.route('/uranai', methods=['POST'])
def uranai():
    text = request.form['name']

    if text == 'taro' :
        html = render_template('daikiti.html', name=text)
        print(html)
        return html

    else:
        html = render_template('kiti.html', name=text)
        print(html)
        return html
