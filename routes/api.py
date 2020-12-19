from flask import Blueprint
from database import Database
import json
from flask import request
api = Blueprint('api', __name__, template_folder='templates')


@api.route('/entries', methods=["GET"])
def get_all_entries():
    entries = Database.get_records()
    for entry in entries:
        entry['_id'] = str(entry['_id'])
    return json.dumps(entries)


@api.route('/delete', methods=['DELETE'])
def delete_all_entries():
    Database.delete_records()
    return "records deleted"


@api.route('/post', methods=['POST'])
def post_an_entry():
    doc = {
        'title': request.form['title'],
        'post': request.form['post']
    }
    Database.insert_record(doc)
    return 'record added'


@api.route("/edit", methods=["POST"])
def edit_an_entry():
    sieve = {
        "title": request.form["title"],
        "post": request.form["post"]
    }
    newdoc = {
        "title": request.form["new_title"],
        "post": request.form["new_post"]
    }
    Database.edit_doc(sieve, newdoc)
