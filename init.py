from DB.models import TagName, TagCat, TagNameCat, CompanyName, CompanyCat, CompanyNameCat, Mapped
from DB.qurey import search_comp_cat_id, search_tag_cat_id
from Batch.storeCSV import StoreCSV
import numpy as np
from main import db


_path = './Raw/wanted_temp_data.csv'
class Batch:
    
    def __init__(self, _path='./Raw/wanted_temp_data.csv'):
        self.csv = StoreCSV(_path=_path)
        self._init_datas()

    def _init_tag_data(self):
        tag_cat_nm = [TagCat(tag_cat_id=_tag[0]+1, tag_cat_nm=_tag[1])for _tag in enumerate(self.base_tag)]
        tag_name_nm = [TagName(tag_name_id=_tag[0]+1, tag_name_nm=_tag[1])for _tag in enumerate(self.total_tag)]
        tag_name_cat = [TagNameCat(tag_name_id=_tag[1], tag_cat_id=_tag[0])for _tag in self.zipped]
        
        db.session.add_all(tag_cat_nm)
        db.session.add_all(tag_name_nm)
        db.session.commit()
        db.session.add_all(tag_name_cat)
        db.session.commit()

    def _init_comp_data(self):        
        com_name = [CompanyName(comp_name_id=_idx[0]+1, comp_name_nm=_idx[1])for _idx in enumerate(self._total_company_name_list)]
        com_cat = [CompanyCat(comp_cat_id=_idx+1, comp_name_nm=self._company_cat_name[_idx][0])for _idx in self._company_cat_name]
        com_name_cat = [CompanyNameCat(comp_cat_id=_idx[0]+1, comp_name_id=_idx[1]) for _idx in self._tuple]

        db.session.add_all(com_cat)
        db.session.add_all(com_name)
        db.session.commit()
        db.session.add_all(com_name_cat)
        db.session.commit()

    def _init_datas(self):
        _company_table = self.csv.read_data.loc[:,"company_ko":"company_ja"].values.tolist()
        self._total_company_name_list = []
        self._company_cat_name = {}
        self._tuple = []    
        _idx = 0
        
        en_tag = self.csv.extract_tag_list(_list=self.csv.read_data["tag_en"].values.tolist())
        kr_tag = self.csv.extract_tag_list(_list=self.csv.read_data["tag_ko"].values.tolist())
        jp_tag = self.csv.extract_tag_list(_list=self.csv.read_data["tag_ja"].values.tolist())

        self.base_tag = en_tag
        self.total_tag = en_tag + kr_tag + jp_tag

        idx_list = list(range(1, len(self.base_tag)+1))*3
        total_list = list(range(1, len(self.total_tag)+1))
        self.zipped = zip(idx_list, total_list)

        for _comp_name in _company_table:
            _sub_list = [_item for _item in _comp_name if str(_item) != 'nan']
            self._total_company_name_list += _sub_list
            self._company_cat_name[_company_table.index(_comp_name)] = _sub_list

        for _data in self._total_company_name_list:
            _idx += 1
            for _detail in self._company_cat_name:
                if  _data in self._company_cat_name[_detail]:
                    self._tuple.append((_detail,_idx))

    def init_mapped_data(self):
        # print(self._total_company_name_list)
        # print(self.total_tag)

        _tags= self.csv.read_data.loc[:,"tag_ko":"tag_ja"].values.tolist()
        print(a[0])        
        
        #  = search_comp_cat_id("원티드랩").comp_cat_id
        # print(a)
        # search_tag_cat_id()
        # TC = TagNameCat.query.all()
        # CC = CompanyNameCat.query.all()
        # for _ in TC:
        #     print(_.tag_cat_id)
        #     print(_.tag_name_id)
        
        
    def init_db(self):
        self._init_tag_data()
        self._init_comp_data()
        


#  ==== 마지막 테이블 데이터 넣는거 남음

B = Batch()
# B.init_db()
B.init_mapped_data()