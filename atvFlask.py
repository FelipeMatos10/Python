from flask import Flask


app = Flask(__name__)
@app.route('/decorator')
def explicacao():
    return 'O que é um decorator em Python e pra que ele? \n É um comando que em determinada rota seja executada uma determinada funcao.'


if __name__ == '__main__':
    app.run(debug=True)