#Импорт
from flask import Flask, flash, render_template,request, redirect, url_for


app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_html =request.form.get("button_html")
    button_db = request.form.get('button_db')
    button_telegram = request.form.get('button_telegram')

    return render_template(
        'index.html',
        button_python=button_python,
        button_telegram=button_telegram,
        button_html=button_html,
        button_db=button_db
    )
    

@app.route('/feedback', methods=['POST'])
def feedback_form():
    text =request.form["text"]
    email = request.form["email"]

    return render_template('feedback.html', email=email, text=text)

     


    

if __name__ == "__main__":
    app.run(debug=True)