from flask import *
from database import Database
from routes.api import api
import requests
app = Flask(__name__)
app.register_blueprint(api)


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route("/")
def index():
    their_ip=request.remote_addr
    entries = requests.get('https://shielded-brook-48294.herokuapp.com/entries').json()
    return render_template('index.html', entries=entries,ip=their_ip)


# index = app.route("/")(index())


@app.route("/add", methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        data = {'title': request.form['title'],
                'post': request.form['post']}
        requests.post('https://shielded-brook-48294.herokuapp.com/post', data=data)
        return redirect(url_for('index'))

    return render_template('add_entry.html')


@app.route('/clear')
def delete_entries():
    requests.delete('https://shielded-brook-48294.herokuapp.com/delete')
    return redirect(url_for("index"))


@app.route("/editentry", methods=["GET", "POST"])
def edit_entry():
    if request.method == "GET":
        title = request.args["title"]
        post = request.args["post"]
        return render_template("edit.html", title=title, post=post)
    requests.post("https://shielded-brook-48294.herokuapp.com/edit", data=request.form)
    return redirect(url_for("index"))


@app.route("/rawcontent")
def raw_content():
    """try:
        request.args["type"]
    except KeyError:
        entries = requests.get('https://shielded-brook-48294.herokuapp.com/entries').json()
        return str(entries)
    if request.args["type"] == "html":
        entries = requests.get('https://shielded-brook-48294.herokuapp.com/entries').json()
        return str(entries)
    elif request.args["type"] == "json":
        return jsonify(requests.get('https://shielded-brook-48294.herokuapp.com/entries').json())"""
    return 'Down for maintenance<script type="text/javascript" src="../static/js/redirect.js"></script>'


if __name__ == '__main__':
    app.run(debug=True)
