# app.py at the same level myproject!
# перед первым запуском приложения необходимо
# инициировать базу данных.

# flask db init
# flask db migrate -m 'create puppies and owners'
# flask db upgrade

# Запуск приложения   - python app.py


from myproject import app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

