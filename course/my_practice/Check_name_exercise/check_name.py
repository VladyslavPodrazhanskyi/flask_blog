from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/report')
def report():
    name = request.args.get('name')
    upper_letter, lower_letter = False, False
    if name != name.upper():
        lower_letter = True
    if name != name.lower():
        upper_letter = True
    # end_num = s[-1].isdigit()
    try:
        int(name[-1])
        end_num = True
    except ValueError:
        end_num = False

    return render_template('report.html', name=name, end_num=end_num, lower_letter=lower_letter, upper_letter=upper_letter)


if __name__ == "__main__":
    app.run(debug=True)
