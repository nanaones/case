from DB.models import db, TagName, TagCat, TagNameCat, CompanyName, CompanyCat, CompanyNameCat, Mapped, Query
from Batch.CSV import CSV


class Batch:
    """
    wanted_temp_data.csv 파일에 저장된 데이터를 지정된 스키마에 맞춰 DB에 저장.
    """
    
    def __init__(self, _path='./Raw/wanted_temp_data.csv'):
        self.csv = CSV(_path=_path)
        self._init_datas()

    def _init_tag_data(self) -> None:
        """
        Tag 데이터를 데이터베이스 스키마에 맞춰서 저장
        param:None
        return:None
        """
        tag_cat_nm = [TagCat(tag_cat_id=_tag[0]+1, tag_cat_nm=_tag[1])for _tag in enumerate(self.base_tag)]
        tag_name_nm = [TagName(tag_name_id=_tag[0]+1, tag_name_nm=_tag[1])for _tag in enumerate(self.total_tag)]
        tag_name_cat = [TagNameCat(tag_name_id=_tag[1], tag_cat_id=_tag[0])for _tag in self.zipped]
        
        db.session.add_all(tag_cat_nm)
        db.session.add_all(tag_name_nm)
        db.session.commit()
        db.session.add_all(tag_name_cat)
        db.session.commit()

    def _init_comp_data(self) -> None:  
        """
        Company 데이터를 데이터베이스 스키마에 맞춰서 저장
        param:None
        return:None
        """
        com_name = [CompanyName(comp_name_id=_idx[0]+1, comp_name_nm=_idx[1])for _idx in enumerate(self._total_company_name_list)]
        com_cat = [CompanyCat(comp_cat_id=_idx+1, comp_name_nm=self._company_cat_name[_idx][0])for _idx in self._company_cat_name]
        com_name_cat = [CompanyNameCat(comp_cat_id=_idx[0]+1, comp_name_id=_idx[1]) for _idx in self._tuple]

        db.session.add_all(com_cat)
        db.session.add_all(com_name)
        db.session.commit()
        db.session.add_all(com_name_cat)
        db.session.commit()

    def _init_datas(self) -> None:
        """
        self._init_tag_data,
        self._init_comp_data,
        self._init_mapped_data
        위의 클래스 메서드가 사용하는 Instance value를 선언하는 클래스 메서드
        param:None
        return:None
        """
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

    def _init_mapped_data(self) -> None:
        """
        Company 관련 데이터와 Tag 데이터를 Mapping한 데이터베이스 스키마에 맞춰서 데이터를 저장합니다.
        param:None
        return:None
        """
        
        _company_names = self._company_cat_name
        _tags= self.csv.read_data["tag_en"].values.tolist()
        _Mapped_list = []
        _idx = 0

        print(len(_company_names))
        print(len(_company_names))

        while len(_tags) != _idx:
            _company_nm = _company_names[_idx]
            _tag_list = _tags[_idx].split("|")

            for _company in _company_nm:
                _comp_cat_id = Query.search_comp_cat_id_by_comp_name(_company_name=_company).comp_cat_id
                
                for _tag in _tag_list:
                    _tag_cat_id = Query.search_tag_cat_id_by_tag_cat_nm(_tag_cat_nm=_tag).tag_cat_id
                    _Mapped_list.append(Mapped(comp_cat_id=_comp_cat_id, tag_cat_id=_tag_cat_id))

            _idx += 1
        print(_idx)
        db.session.add_all(_Mapped_list)
        db.session.commit()

    def init_db(self) -> None:
        """
        self._init_tag_data,
        self._init_comp_data,
        self._init_mapped_data
        
        위 3가지의 클래스매서드를 모두 수행하여 데이터베이스 초기화를 진행.
        param:None
        return:None
        """
        
        self._init_tag_data()
        self._init_comp_data()
        self._init_mapped_data()


if __name__ == '__main__':
    B = Batch()
    B.init_db()

