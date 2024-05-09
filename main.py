from flask import Flask, render_template, request  # Importa a classe Flask do módulo Flask

app = Flask(__name__)  # Cria uma instância da aplicação Flask
@app.route('/',)  # Define uma rota padrão (página inicial) da aplicação
def index():
    return render_template('index.html', resultado=" ")

@app.route('/Fatorial', methods=['POST'])  # Define uma rota padrão (página inicial) da aplicação
def Fatorial():
    numero = int(request.form["numero"])
    resultado = ""
    fatorial = 1

    if numero < 0:
        resultado="Fatorial não funciona com numeros negativos"
    else:
        while numero > 1:
            fatorial *= numero
            numero -= 1
        resultado= fatorial
    return render_template('index.html', resultado = resultado)

if __name__ == '__main__':  # Verifica se este arquivo está sendo executado diretamente
    app.run(debug=True)  # Inicia o servidor de desenvolvimento do Flask com modo de depuração ativado
