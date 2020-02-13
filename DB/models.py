from main import db

class WANT_COMP_NAME_TB(db.Model):
    __tablename__ = 'WANT_COMP_NAME_TB'
    COMP_NAME_ID = db.Column('COMP_NAME_ID', db.Integer, primary_key=True)
    COMP_NAME_NM = db.Column("COMP_NAME_NM", db.String(80))
    
    def __init__(self, COMP_NAME_ID, COMP_NAME_NM):
        self.COMP_NAME_ID = COMP_NAME_ID
        self.COMP_NAME_NM = COMP_NAME_NM

class WANT_COMP_NAME_TB(db.Model):
    __tablename__ = 'WANT_COMP_NAME_TB'
    COMP_NAME_ID = db.Column('COMP_NAME_ID', db.Integer, primary_key=True)
    COMP_NAME_NM = db.Column("COMP_NAME_NM", db.String(80))
    
    def __init__(self, COMP_NAME_ID, COMP_NAME_NM):
        self.COMP_NAME_ID = COMP_NAME_ID
        self.COMP_NAME_NM = COMP_NAME_NM

