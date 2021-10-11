from flask import Flask, request, render_template, Response
from database import MySQL

app = Flask(__name__, template_folder='templates', static_folder='public')

@app.route('/', methods=['POST', 'GET'])
def query():
    if request.method == 'POST':
        # obtendo informações
        name = request.form.get('name')

        if name is None or name == '':
            return render_template('index.html', invalid_name=True)

    database = MySQL()
    students = database.return_student(name)

# Criar filtro para retornar alunos de tal turma, idade ou status