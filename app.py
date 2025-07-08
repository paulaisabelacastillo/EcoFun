from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

# Página principal
@app.route("/")
def home():
    return render_template("index.html")

# Página de misiones
@app.route("/misiones")
def misiones():
    if "completadas" not in session:
        session["completadas"] = []
    return render_template("misiones.html", completadas=session["completadas"])

# Endpoint para registrar misión completada
@app.route("/completar/<int:dia>")
def completar_mision(dia):
    if "completadas" not in session:
        session["completadas"] = []
    if dia not in session["completadas"]:
        session["completadas"].append(dia)
        session.modified = True
    return redirect(url_for("misiones"))

if __name__ == '__main__':
    app.run(debug=True)
