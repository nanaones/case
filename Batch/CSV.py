import pandas as pd

class CSV:
    """
    주어진 CSV데이터를 읽고, 원하는 형태로 가공하여 전달합니다.
    """
    def __init__(self, _path:str):
        """
        param:_path: CSV 파일의 경로
        return:None
        """
        self.csv_path = _path
        self.read_data = pd.read_csv(self.csv_path, sep=',')
    
    def extract_tag_list(self, _list):
        """
        param:_list: List 타입의 data
        return:sorted(set(out)):set: Set 타입의 데이터
        """
        out = []
        for data in _list:
            out += data.split('|')
        return sorted(set(out))
    
