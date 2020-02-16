import json
import os

from flask import Flask, request, abort, Response
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

import DB.models


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


@app.errorhandler(400)
def page_not_found(error):
    _res = {
        "error": {
            "code": 400,
            "errors": [
              {
                "message": "Bad Request",
                "reason": "notFound"
              }
            ],
            "message": "Bad Request"
          }
        }
    return Response(_res, status=400, mimetype='application/json')


@app.route("/search/company", methods=["GET"])
@cross_origin()
def company_search():
    """
    GET HTTP METHOD
    입력된 회사이름을 검색한후, 검색결과 리턴

    :params:companyName      회사이름
    """
    ret = {
        "data": []
    }
    try:
        company_name = request.args.get("companyName").strip()
        _company_list = DB.models.Query.get_comp_name_by_comp_name(company_name)
        for _company in _company_list:
            ret["data"].append(_company.comp_name_nm)
        return json.dumps(ret)
    except AttributeError:
        abort(400)


@app.route("/search/tag", methods=["GET"])
@cross_origin()
def tag_search():
    """
    GET HTTP METHOD
    입력된 tagNqme을 검색한후, 검색결과 리턴

    :params:tagName      태그이름
    """

    try:
        tag_name = request.args.get("tagName").strip()
        _data = DB.models.Query.get_company_name_by_tag_name(tag_name)
        return json.dumps(_data)
    except AttributeError:
        abort(400)


@app.route("/company", methods=["GET"])
@cross_origin()
def company():
    """
    GET HTTP METHOD
    저장되어있는 모든 회사의 이름 리턴
    """
    try:
        return json.dumps(DB.models.Query.get_all_company_name())
    except AttributeError:
        abort(400)


@app.route("/company/<int:id>", methods=["GET"])
@cross_origin()
def company_get_by_id(id:int):
    """
    GET HTTP METHOD
    URI 에 해당하는 회사의 종류 리턴

    :params:id      회사의 id
    """

    try:
        _data = DB.models.Query.get_comp_data_by_comp_id(comp_name_id=id)
        return json.dumps(_data)
    except AttributeError:
        abort(400)

@app.route("/tag", methods=["GET"])
@cross_origin()
def tag():
    """
    GET HTTP METHOD
    저장되어있는 모든 tag의 이름 리턴
    """
    try:
        return json.dumps(DB.models.Query.get_all_tag_name())
    except AttributeError:
        abort(400)


@app.route("/tag/<int:id>", methods=["GET"])
@cross_origin()
def tag_get_by_id(id:int):
    """
    GET HTTP METHOD
    URI 에 해당하는 태그의 종류 리턴

    :params:id      태그 id
    """

    try:
        _data = DB.models.Query.get_tag_data_by_tag_id(tag_name_id=id)
        return json.dumps(_data)
    except AttributeError:
        abort(400)


@app.route("/company/<int:id>", methods=["POST"])
@cross_origin()
def tag_add(id:int):
    """
    POST HTTP METHOD
    URI 에 해당하는 회사에 TAG_NAME 을 파라미터로 받은 후, 해당 파라미터에 대한 삽입 진행
    이미 존재하는 태그일경우, exception 발생을 통한 추가 삽입차단

    :params:tagName  삭제될 태그이름
    :params:id      태그가 속한 회사의 id
    """

    try:
        tag_name = request.args.get("tagName").strip()
        company_name = DB.models.Query.search_comp_name_by_comp_name_id(comp_name_id=id)
        _company_cat_id = DB.models.Query.search_comp_cat_id_by_comp_name(_company_name=company_name).comp_cat_id
        _tag_cat_id = DB.models.Query.search_tag_cat_id_by_tag_cat_nm(_tag_cat_nm=tag_name).tag_cat_id
        _is_saved_data = DB.models.Query.get_TF_by_tag_cat_id(comp_cat_id=_company_cat_id, tag_cat_id=_tag_cat_id)

        if _is_saved_data:
            raise AttributeError

        _mapped = DB.models.Mapped(comp_cat_id=_company_cat_id, tag_cat_id=_tag_cat_id)
        db.session.add(_mapped)
        db.session.commit()
        return Response( status=200, mimetype='application/json')

    except AttributeError:
        abort(400)


@app.route("/company/<int:id>", methods=["DELETE"])
@cross_origin()
def tag_del(id:int):
    """
    DELETE HTTP METHOD
    URI 에 해당하는 회사에 TAG_NAME 을 파라미터로 받은 후, 해당 파라미터에 대한 삭제 진행

    :params:tagName  삭제될 태그이름
    :params:id      태그가 속한 회사의 id
    """

    try:
        tag_name = request.args.get("tagName").strip()
        company_name = DB.models.Query.search_comp_name_by_comp_name_id(comp_name_id=id)
        DB.models.Query.delete_tag_by_tag_name_n_comp_name(company_name= company_name, tag_name= tag_name)
        return Response( status=200, mimetype='application/json')
    except AttributeError:
        abort(400)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
