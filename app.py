from flask import (
    Flask,
    render_template,
    redirect,
    request
)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_home():
    return render_template('home.html')

@app.route('/reg', methods=['GET', 'POST'])
def get_home1():
    return render_template('registr.html')


@app.route('/log', methods=['GET', 'POST'])
def get_home2():
    return render_template('log.html')



if __name__ == '__main__' :
    app.run(
        debug=True,
    )













