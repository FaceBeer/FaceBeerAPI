from flask import Flask, request, make_response
from dao import DAO
import json

app = Flask(__name__)


@app.route('/')
def index():
    return "Bonjour world! from FaceBeer API"


@app.route("/reset")
def reset():
    dao.reset()


@app.route("/get_all_users", methods=["GET", "OPTIONS"])
def all_user_leaderboard():
    response = make_response()
    if request.method == "OPTIONS":
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response
    else:
        rows = dao.get_all_rows()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.response = json.dumps({"code": 200, "message": rows})
        return response


@app.route("/user/<name>", methods=["GET","OPTIONS"])
def user_leaderboard(name):
    response = make_response()
    rows = dao.get_user(name)
    if request.method == "OPTIONS":
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        response.headers.add('Access-Control-Allow-Credentials', True)
    else:
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.response = json.dumps({"code": 200, "message": rows})
    print(response.headers)
    return response


@app.route("/append", methods=["POST"])
def add_reading():
    name = request.form["name"]
    bac = request.form["bac"]
    timestamp = request.form["timestamp"]
    dao.add_item(name, bac, timestamp)
    response = {"code": 200, "message": "Successfully added row"}
    return response


if __name__ == "__main__":
    dao = DAO()
    app.run(host='0.0.0.0', port=8000)
