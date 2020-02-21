from main import db


class CompanyName(db.Model):
    __tablename__ = 'WANT_COMP_NAME_TB'
    comp_name_id = db.Column('COMP_NAME_ID', db.Integer, primary_key=True)
    comp_name_nm = db.Column("COMP_NAME_NM", db.String(80))
    
    def __init__(self, comp_name_id, comp_name_nm):
        self.comp_name_id = comp_name_id
        self.comp_name_nm = comp_name_nm


class CompanyCat(db.Model):
    __tablename__ = 'WANT_COMP_CAT_TB'
    comp_cat_id = db.Column('COMP_CAT_ID', db.Integer, primary_key=True)
    comp_name_nm = db.Column("COMP_NAME_NM", db.String(80))
    
    def __init__(self, comp_cat_id, comp_name_nm):
        self.comp_cat_id = comp_cat_id
        self.comp_name_nm = comp_name_nm



class CompanyNameCat(db.Model):
    __tablename__ = 'WANT_COMP_NAME_CAT_TB'
    comp_name_cat_id = db.Column('COMP_NAME_CAT_ID', db.Integer, primary_key=True)
    comp_name_id = db.Column("COMP_NAME_ID", db.ForeignKey("WANT_COMP_NAME_TB.COMP_NAME_ID"))
    comp_cat_id = db.Column("COMP_CAT_ID", db.ForeignKey("WANT_COMP_CAT_TB.COMP_CAT_ID"))
    
    def __init__(self, comp_name_id, comp_cat_id ):
        self.comp_name_id = comp_name_id
        self.comp_cat_id = comp_cat_id


class TagName(db.Model):
    __tablename__ = 'WANT_TAG_NAME_TB'
    tag_name_id = db.Column('TAG_NAME_ID', db.Integer, primary_key=True)
    tag_name_nm = db.Column("TAG_NAME_NM", db.String(80))

    def __init__(self, tag_name_id, tag_name_nm):
        self.tag_name_id = tag_name_id
        self.tag_name_nm = tag_name_nm



class TagCat(db.Model):
    __tablename__ = 'WANT_TAG_CAT_TB'
    tag_cat_id = db.Column('TAG_CAT_ID', db.Integer, primary_key=True)
    tag_cat_nm = db.Column("TAG_CAT_NM", db.String(80))

    def __init__(self,tag_cat_id, tag_cat_nm):
        self.tag_cat_id = tag_cat_id
        self.tag_cat_nm = tag_cat_nm

class TagNameCat(db.Model):
    __tablename__ = 'WANT_TAG_NAME_CAT_TB'
    tag_name_cat_id = db.Column('TAG_NAME_CAT_ID', db.Integer,  primary_key=True)
    tag_name_id = db.Column("TAG_NAME_ID", db.Integer, db.ForeignKey("WANT_TAG_NAME_TB.TAG_NAME_ID"))
    tag_cat_id = db.Column("TAG_CAT_ID", db.Integer, db.ForeignKey("WANT_TAG_CAT_TB.TAG_CAT_ID"))
    
    def __init__(self, tag_name_id, tag_cat_id ):
        self.tag_name_id = tag_name_id
        self.tag_cat_id = tag_cat_id


class Mapped(db.Model):
    __tablename__ = 'WANT_MAPPED_TB'
    mapped_tb_id = db.Column('MAPPED_TB_ID', db.Integer, primary_key=True)
    comp_cat_id = db.Column("COMP_CAT_ID", db.ForeignKey("WANT_COMP_CAT_TB.COMP_CAT_ID"))
    tag_cat_id = db.Column("TAG_CAT_ID", db.ForeignKey("WANT_TAG_CAT_TB.TAG_CAT_ID"))
    
    def __init__(self, comp_cat_id, tag_cat_id):
        self.mapped_tb_id
        self.comp_cat_id = comp_cat_id
        self.tag_cat_id = tag_cat_id


# TODO: O(N^2)의 안좋은 복잡도를 가지고있는 메서드 모두 수정
class Query:
    @staticmethod
    def search_comp_cat_id_by_comp_name(_company_name: str):
        """
        _company_name 를 기준으로 cat_id 찾기
        
        """
        comp_name_id = CompanyName.query.filter_by(comp_name_nm=_company_name).first().comp_name_id
        return CompanyNameCat.query.filter_by(comp_name_id=comp_name_id).first()

    @staticmethod
    def search_tag_cat_id_by_tag_cat_nm(_tag_cat_nm: str):
        """
        _tag_cat_nm 를 기준으로 _tag_cat_id 찾기
        """
        tag_name_id = TagName.query.filter_by(tag_name_nm=_tag_cat_nm).first().tag_name_id
        return TagNameCat.query.filter_by(tag_name_id=tag_name_id).first()

    @staticmethod
    def search_tag_id_by_tag_name(_tag_name: str) -> int:
        """
        입력받은 _tag_name 문자를 기준으로 tag의 id를 찾기
        """
        return TagName.query.filter_by(tag_name_nm=_tag_name).first().tag_name_id

    @staticmethod
    def search_tag_cat_id_by_tag_name_id(_tag_name_id: int):
        """
        _tag_name_id 를 기준으로 tag_cat_id 찾기
        """
        return TagNameCat.query.filter_by(tag_name_id=_tag_name_id).first().tag_cat_id

    @staticmethod
    def search_company_cat_by_tag_cat_id(tag_cat_id: int):
        """
        입력받은 tag cat 를 기준으로 company_list를 반환
        """
        return Mapped.query.filter_by(tag_cat_id=tag_cat_id).all()

    @staticmethod
    def search_company_name_by_comp_cat_id(comp_cat_id: int):
        """
        입력받은 comp_cat_id 를 기준으로 company_list를 반환
        """
        return CompanyCat.query.filter_by(comp_cat_id=comp_cat_id).all()

    @staticmethod
    def search_tag_cat_name_by_comp_cat_id(comp_cat_id: int):
        """
        입력받은 comp_cat_id 를 기준으로 comp_cat_id 가 같은 List를 반환
        """
        return Mapped.query.filter_by(comp_cat_id=comp_cat_id).all()

    @staticmethod
    def search_tag_id_by_tag_cat_id(tag_cat_id: int):
        """
        입력받은 tag_cat_id 를 기준으로 tag_name_id 가 입력받은 tag_cat_id와 같은 List를 반환
        """
        return TagNameCat.query.filter_by(tag_cat_id=tag_cat_id).all()

    @staticmethod
    def search_tag_name_by_tag_id(tag_name_id: int):
        """
        입력받은 tag_name_id 를 기준으로 tag_name 반환
        """
        return TagName.query.filter_by(tag_name_id=tag_name_id).first().tag_name_nm

    @staticmethod
    def search_comp_name_by_comp_name_id(comp_name_id: int):
        """
        입력받은 tag_name_id 를 기준으로 tag_name 반환
        """
        return CompanyName.query.filter_by(comp_name_id=comp_name_id).first().comp_name_nm

    @staticmethod
    def get_comp_name_by_comp_name(_comp_name: str):
        """
        입력받은 문자를 기준으로 회사이름 찾기
        """
        return CompanyName.query.filter(CompanyName.comp_name_nm.like("%"+_comp_name+"%")).all()

    @staticmethod
    def get_company_name_by_tag_name(_tag_name_string: str) -> dict:
        """
        입력받은 _tag_name_string 를 기준으로 company list를 반환
        """

        _ret = []
        _tag_id = Query.search_tag_id_by_tag_name(_tag_name_string)
        print(_tag_id, "_tag_id")
        _tag_cat_id = Query.search_tag_cat_id_by_tag_name_id(_tag_id)
        _comp_list = Query.search_company_cat_by_tag_cat_id(_tag_cat_id)

        for _company in _comp_list:
            _company_id_list = Query.search_company_name_by_comp_cat_id(comp_cat_id=_company.comp_cat_id)
            for _company_id in _company_id_list:
                _ret.append(_company_id.comp_name_nm)
        return {"data": list(set(_ret))}

    @staticmethod
    def get_comp_data_by_comp_id(comp_name_id: int):
        """
        입력받은 comp_name_id 를 기준으로 comp_name 반환
        """
        _tags = []
        _comp_name = CompanyName.query.filter_by(comp_name_id=comp_name_id).first().comp_name_nm
        _comp_cat_id = Query.search_comp_cat_id_by_comp_name(_company_name=_comp_name).comp_cat_id
        _tag_cat_id = Query.search_tag_cat_name_by_comp_cat_id(comp_cat_id=_comp_cat_id)
        
        for _ in _tag_cat_id:
            tag_name_id_list = Query.search_tag_id_by_tag_cat_id(_.tag_cat_id)
            for _id in tag_name_id_list:
                _tags.append(TagName.query.filter_by(tag_name_id=_id.tag_name_id).first().tag_name_nm)

        _ret = {
            "companyName": _comp_name,
            "tags": _tags
        }
        return _ret

    @staticmethod
    def get_tag_data_by_tag_id(tag_name_id: int):
        """
        입력받은 tag_name_id 를 기준으로 Dict 반환
        """
        _tags = []
        _tag_cat_id = Query.search_tag_cat_id_by_tag_name_id(tag_name_id)
        _tag_id_list = Query.search_tag_id_by_tag_cat_id(tag_cat_id=_tag_cat_id)
        for _ in _tag_id_list:
            _tags.append(Query.search_tag_name_by_tag_id(tag_name_id=_.tag_name_id))

        _ret = {
            "tags": _tags
        }
        return _ret

    @staticmethod
    def delete_tag_by_tag_name_n_comp_name(company_name: str, tag_name: str):
        """
        입력받은 company_name, tag_name을 기준으로 삭제
        """
        _tags = []
        _company_cat_id = Query.search_comp_cat_id_by_comp_name(_company_name=company_name).comp_cat_id
        _tag_cat_id = Query.search_tag_cat_id_by_tag_cat_nm(_tag_cat_nm=tag_name).tag_cat_id
        _data = Mapped.query.filter_by(comp_cat_id=_company_cat_id, tag_cat_id=_tag_cat_id).all()
        for _ in _data:
            Mapped.query.filter_by(mapped_tb_id=_.mapped_tb_id).delete()
        db.session.commit()

    @staticmethod
    def get_TF_by_tag_cat_id(comp_cat_id: int, tag_cat_id: int):
        """
        입력받은 문자를 기준으로 회사이름 찾기
        """
        _data = Mapped.query.filter_by(comp_cat_id=comp_cat_id, tag_cat_id=tag_cat_id).all()
        return bool(_data)

    @staticmethod
    def get_all_company_name():
        """
        입력되어있는 모든회사의 이름을 리턴한다.
        """
        _ret = {
            "company": []
        }
        for _data in CompanyCat.query.all():
            _ret["company"].append(_data.comp_name_nm)

        return _ret

    @staticmethod
    def get_all_tag_name():
        """
        입력되어있는 태그의 이름을 리턴한다.
        """
        _ret = {
            "tag": []
        }

        for _ in TagName.query.join(TagNameCat, TagName.tag_name_id == TagNameCat.tag_name_id).all():
            _ret["tag"].append(_.tag_name_nm)

        return _ret
