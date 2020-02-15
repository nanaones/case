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
        
    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

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

        # ------------------------------------------------        
class Mapped(db.Model):
    __tablename__ = 'WANT_MAPPED_TB'
    mapped_tb_id = db.Column('MAPPED_TB_ID', db.Integer, primary_key=True)
    comp_cat_id = db.Column("COMP_CAT_ID", db.ForeignKey("WANT_COMP_CAT_TB.COMP_CAT_ID"))
    tag_cat_id = db.Column("TAG_CAT_ID", db.ForeignKey("WANT_TAG_CAT_TB.TAG_CAT_ID"))
    
    def __init__(self, comp_cat_id, tag_cat_id ):
        self.comp_cat_id = comp_cat_id
        self.tag_cat_id = tag_cat_id
        

