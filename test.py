from Batch.CSV import CSV
import unittest
import re
from DB.models import Query


class TestCustom(unittest.TestCase):
    def _csv_load(self, _path="./Raw/wanted_temp_data.csv"):
        self.csv = CSV(_path=_path)

    def test_csv_tag_language_data(self):
        """
        CSV 데이터의 태그개수가 언어별로 동일한지 확인
        """
        self._csv_load()
        _csv_data = self.csv.read_data.loc[:,"tag_ko":"tag_ja"].values.tolist()
        while len(_csv_data) != 0:
            _tag_data = _csv_data.pop()
            _len = [x.count("|") for x in _tag_data]
            self.assertTrue( (_len[0] == _len[1] and
                              _len[0] == _len[2] and
                              _len[1] == _len[2]) == True,
                            msg= f"have verified that the number of tags assigned to each language matches each other.\n Check Tag Count"
                            )
        print(self.test_csv_tag_language_data.__name__, "-- pass")


    def test_csv_tag_number_data(self):
        """
        CSV 데이터의 태그번호가 언어별로 동일한지 확인
        """
        self._csv_load()
        _csv_data = self.csv.read_data.loc[:,"tag_ko":"tag_ja"].values.tolist()
        while len(_csv_data) != 0:
            _tag_data = _csv_data.pop()
            _numbers = [re.findall("\d", x) for x in _tag_data]
            self.assertTrue( (_numbers[0] == _numbers[1] and
                              _numbers[0] == _numbers[2] and
                              _numbers[1] == _numbers[2]) == True,
                            msg= f" have verified that the tag numbers specified for each language match each other.\n Check TagNumber is correct"
                            )
        print(self.test_csv_tag_number_data.__name__, "-- pass")

    def test_search_comp_name_function_can_find_parentheses(self):
        """
        search_comp_name 함수가 소괄호를 입력받았을때, 정상적인 검색이 가능한지 확인
        """
        _comp_list = [
            "자버(Jober)",
            "(주)몬스터스튜디오",
            "와이즈키즈(wisekids)",
            "데이터얼라이언스(DataAlliance)",
            "주렁주렁(zoolungzoolung)",
            "스트라다월드와이드(Strada)",
            "도빗(Dobbit)",
            "대상홀딩스(주) - existing",
            "지오코리아(페루관광청)",
            "까브드뱅(Cave de Vin)",
            "아이엠에이치씨(IMHC)",
            "(주) 휴톰-중복",
            "(주) 새론다이내믹스",
            "(주)아임블록",
            "(주)이모션글로벌-중복",
            "애디터(Additor)",
            "플라이앤컴퍼니(푸드플라이)"
        ]

        _find_parentheses_result = Query.get_comp_name_by_comp_name(_comp_name="(")
        _name_list = []

        for _ in _find_parentheses_result:
            _name_list.append(_.comp_name_nm)
        self.assertTrue(_comp_list == _name_list,
                        msg= "search_comp_name_function_can_find_parentheses Fail, Chaeck DB")

        print(self.test_search_comp_name_function_can_find_parentheses.__name__, "-- pass")

if __name__ == '__main__':
    unittest.main()