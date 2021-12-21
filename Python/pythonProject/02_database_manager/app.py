from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLACHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Página em branco"


if __name__ == "__main__":
    app.run(debug=True)
