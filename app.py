from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import DB.models
from flask_sqlalchemy import SQLAlchemy
import os

if not os.getenv("DATABASEURI") is None:
    _dbms_uri = os.getenv("DATABASEURI")
else:
    _dbms_uri = "postgresql://postgres:8015@localhost/postgres"

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = _dbms_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
CORS(app)


@app.route("/companySearch", methods=["GET"])
@cross_origin()
def company_search():
    ret = {
        "data": []
    }
    try:
        company_name = request.args.get("companyName").strip()
        _company_list = DB.models.Query.get_comp_name_by_comp_name(company_name)
        for _company in _company_list:
            ret["data"].append(_company.comp_name_nm)
        return json.dumps(ret)
    except BaseException as e:
        print(e)
        return json.dumps()



@app.route("/tagSearch", methods=["GET"])
@cross_origin()
def tag_search():
    tag_name = request.args.get("tagName").strip()
    _data = DB.models.Query.get_company_name_by_tag_name(tag_name)
    return json.dumps(_data)

#
# @app.route("/tag", methods=["POST"])
# @cross_origin()
# def tag_search():
#     tag_name = request.args.get("tagName")
#     _data = DB.models.Query.get_company_name_by_tag_name(tag_name)
#     return json.dumps(_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000 )
