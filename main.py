from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# criar a nossa primeira pagina = primeira rota
@app.route("/") #decorator
def homepage():
    return render_template("homepage.html")

# roda o nosso aplicativo
socketio.run(app, host="192.168.15.178")

# websocket
app.run(debug=True)