from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import pytz

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["webhooks"]
collection = db["events"]

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event")
    author = data.get("sender", {}).get("login", "unknown")
    timestamp = datetime.utcnow().replace(tzinfo=pytz.utc).isoformat()

    from_branch = None
    to_branch = None

    if event_type == "push":
        to_branch = data.get("ref", "").split("/")[-1]
    elif event_type == "pull_request":
        from_branch = data["pull_request"]["head"]["ref"]
        to_branch = data["pull_request"]["base"]["ref"]

    event_doc = {
        "event_type": event_type,
        "author": author,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }
 
    print("Webhook hit!")
    print(event_doc)
    
    collection.insert_one(event_doc)
    return jsonify({"message": "Received"}), 200

@app.route("/events", methods=["GET"])
def get_events():
    events = list(collection.find().sort("timestamp", -1).limit(10))
    for e in events:
        e["_id"] = str(e["_id"])
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
