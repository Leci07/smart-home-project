from flask import Flask, jsonify, request

app = Flask(__name__)

# --- Fake sensor data (stand-in for real hardware, for now) ---
state = {
    "motion": True,
    "dark": True,
    "light_on": False,
    "locked": True,
}

# --- Simple API key for authentication ---
API_KEY = "lovro_smarthome_2026"  # change this later to something less obvious


def light_should_be_on(motion, dark):
    # Light only turns on if motion is detected AND it's dark
    return motion and dark


@app.route("/status", methods=["GET"])
def get_status():
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        return jsonify({"error": "unauthorized"}), 401

    state["light_on"] = light_should_be_on(state["motion"], state["dark"])
    return jsonify(state)


@app.route("/unlock", methods=["POST"])
def unlock():
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        return jsonify({"error": "unauthorized"}), 401

    state["locked"] = False
    return jsonify({"message": "door unlocked", "locked": state["locked"]})


@app.route("/lock", methods=["POST"])
def lock():
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        return jsonify({"error": "unauthorized"}), 401

    state["locked"] = True
    return jsonify({"message": "door locked", "locked": state["locked"]})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
