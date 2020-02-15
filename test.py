from Batch.storeCSV import StoreCSV
import unittest

class TestCustom(unittest.TestCase):
    def test_csv_tag_data(self):
        _path = "./Raw/wanted_temp_data.csv"
        csv = StoreCSV(_path=_path)
        _csv_data = csv.read_data.loc[:,"tag_ko":"tag_ja"].values.tolist()
        print(_csv_data[0])
        while len(_csv_data) != 0:
            _tag_data = _csv_data.pop()
            _len = [x.count("|") for x in _tag_data]
            self.assertTrue( (_len[0] == _len[1] and _len[0] == _len[2] and _len[1] == _len[2]) == True)

if __name__ == '__main__':
    unittest.main()