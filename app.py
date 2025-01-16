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


import turtle

# Создаем объект черепашки
my_turtle = turtle.Turtle()

# Задаем цвет и толщину линии (необязательно)
my_turtle.color("blue")
my_turtle.pensize(3)

# Рисуем квадрат
for _ in range(4):
    my_turtle.forward(100)  # Длина стороны квадрата
    my_turtle.left(90)       # Поворот на 90 градусов влево

# Завершаем рисование и закрываем окно по клику
turtle.done()










