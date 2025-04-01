from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Webhook funcionando correctamente (modo prueba)"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    mensaje_usuario = data.get("message", {}).get("text", "")
    numero_cliente = data.get("message", {}).get("from", "")

    if not mensaje_usuario:
        return jsonify({"error": "Mensaje vacío"}), 400

    # Simulación sin conexión a OpenAI
    respuesta_falsa = f"Recibí tu mensaje: {mensaje_usuario}"

    return jsonify({
        "text": respuesta_falsa,
        "to": numero_cliente
    })