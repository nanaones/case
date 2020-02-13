from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

from DB import DB

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:8015@localhost/postgres"
db = SQLAlchemy(app)


@app.route("/test", methods = ["GET"])
def get_owner():
    _return = {
        1: [],
        2: []
    }
    for indata in DB.WANT_COMP_NAME_TB.query.order_by(DB.WANT_COMP_NAME_TB.COMP_NAME_ID.desc()).all():
        _return[1].append(indata.COMP_NAME_ID)

    for indata in DB.WANT_COMP_NAME_TB.query.order_by(DB.WANT_COMP_NAME_TB.COMP_NAME_NM.desc()).all():
        _return[2].append(indata.COMP_NAME_NM)

    return json.dumps({"data": _return})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000 )
    
    
    
    