from flask import Flask, jsonify, render_template, request

from bubble_sort import bubble_sort


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/sort")
def sort_numbers():
    payload = request.get_json(silent=True) or {}
    numbers = payload.get("numbers")

    if not isinstance(numbers, list):
        return jsonify({"error": "numbers must be a list"}), 400

    try:
        parsed_numbers = [float(number) for number in numbers]
    except (TypeError, ValueError):
        return jsonify({"error": "numbers must contain only numeric values"}), 400

    sorted_numbers, steps = bubble_sort(parsed_numbers)
    return jsonify({"sorted": sorted_numbers, "steps": steps})


if __name__ == "__main__":
    app.run(debug=True)
