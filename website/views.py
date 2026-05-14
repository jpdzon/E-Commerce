from flask import Blueprint, render_template, jsonify, request, current_app
from bson import ObjectId
from flask_login import login_required, current_user
views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template("home.html", items=[])


# READ — fetch all events for the calendar
@views.route("/events")
def events():
    db = current_app.db
    all_events = list(db.events.find())
    result = []
    for e in all_events:
        result.append(
            {
                "id": str(e["_id"]),
                "title": e["title"],
                "start": e["start"],
                "end": e.get("end", ""),
                "location": e.get("location", ""),
                 "created_by": e.get("created_by", "")
            }
        )
    return jsonify(result)


# CREATE — save a new event
@views.route("/events/create", methods=["POST"])
def create_event():
    data = request.json
    db = current_app.db
    new_event = {
        "title": data["title"],
        "start": data["start"],
        "end": data.get("end", ""),
        "location": data.get("location", ""),
        "created_by": current_user.id
    }
    result = db.events.insert_one(new_event)
    return jsonify({"id": str(result.inserted_id)})


# UPDATE — edit an existing event
@views.route("/events/update/<event_id>", methods=["PUT"])
def update_event(event_id):
    data = request.json
    db = current_app.db
    db.events.update_one(
        {"_id": ObjectId(event_id)},
        {
            "$set": {
                "title": data["title"],
                "start": data["start"],
                "end": data.get("end", ""),
                "location": data.get("location", ""),
            }
        },
    )
    return jsonify({"success": True})


# DELETE — remove an event
@views.route("/events/delete/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    db = current_app.db
    db.events.delete_one({"_id": ObjectId(event_id)})
    return jsonify({"success": True})
