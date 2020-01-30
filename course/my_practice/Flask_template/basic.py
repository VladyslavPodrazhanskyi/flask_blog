from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/vars')
def vars():
    int_list = list(range(25))
    name = 'Topinumbur'
    name_list = list(name)
    puppy_dict = {
        'name': name,
        'age': 2
    }
    return render_template('vars.html', name=name, int_list=int_list,
                           name_list=name_list, puppy_dict=puppy_dict)





if __name__ == "__main__":
    app.run(debug=True)