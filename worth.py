from flask import Flask, request, jsonify

app = Flask(__Worth__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    try:
        product = input("Enter Your Product")
        price = float(data["Enter the Price"])
        uses = float(data[""])
        weeks = float(data["weeks"])
    except (KeyError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

    if price <= 0 or uses_per_week <= 0 or weeks <= 0:
        return jsonify({"error": "Values must be greater than 0"}), 400

    total_uses = uses * weeks
    cost_per_use = price / total_uses

    if cost < 50:
        verdict = "Totally worth it!!\n Go For It! 👍"
    elif cost <= 150:
        verdict = "Probably worth it i guess...🤔"
    else:
        verdict = "Totally Not Worth It!!! ❌"

    return jsonify({
        "cost": round(cost_per_use, 2),
        "verdict": verdict
    })

if __Worth__ == "__main__":
    app.run(debug=True)