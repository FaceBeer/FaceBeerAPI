from flask import Flask, request
from dao import DAO

app = Flask(__name__)


@app.route('/')
def index():
    return "Bonjour world! from FaceBeer API"


@app.route("/get_leaderboard", methods=["GET"])
def leaderboard():
    rows = dao.get_all_rows()
    response = {"code": 500, "message": rows}
    return response


@app.route("/append", methods=["POST"])
def add_reading():
    name = request.form["name"]
    bac = request.form["bac"]
    timestamp = request.form["timestamp"]
    dao.add_item(name, bac, timestamp)
    response = {"code": 500, "message": "Successfully added row"}
    return response


if __name__ == "__main__":
    dao = DAO()
    app.run(host='0.0.0.0', port=8000)
