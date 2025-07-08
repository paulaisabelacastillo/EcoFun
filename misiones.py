from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Guardamos los días completados en un set
misiones_completadas = set()

@app.route("/")
def index():
    return render_template("misiones.html")

@app.route("/completar", methods=["POST"])
def completar_mision():
    data = request.get_json()
    dia = data.get("dia")
    if dia is not None:
        misiones_completadas.add(str(dia))  # 👈 convertimos a string
    return jsonify({"completadas": len(misiones_completadas)})

@app.route("/conteo")
def conteo():
    return jsonify({
        "completadas": len(misiones_completadas),
        "dias": list(misiones_completadas)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
