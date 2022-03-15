import unittest
from my_info import My_info as My
from parse import parse
from search_mentions import search_mentions
from utility import *
from test_data import *
from config import *

class TestMysquare(unittest.TestCase): # unittest.TestCaseを継承したクラスを作成
    def test_testunit(self): # テスト用のメソッド名は`test_`で始める
        print("testing...")
        self.assertEqual(3, 3) # square関数に3を渡すと9が出力されるかどうか確認
        self.assertNotEqual(2, 1) # square関数に1を渡すと1が出力されるかどうか確認
        self.assertTrue(True) # square関数に-3を渡すと9が出力されるかどうか確認
        self.assertFalse(False) # square関数に0を渡すと0が出力されるかどうか確認
        self.assertIs(1,1)
        self.assertIsNot([1,2],[1,2])
        self.assertIn(5,[3,6,5,7])
        self.assertGreaterEqual(9,7)
        print("testOK!")

    def test_search_mentions(self):
        if is_RandomValueBot:
            self.assertEqual(My.id, my_account_data["data"]["id"]) # @RandomValueBotのid
        self.assertEqual(len(search_mentions("2244994945")), 10)
        # search_mentions("1") # id:1 は存在しないのでraise Exceptionになる

    def test_parse(self):
        content1 = "abc"
        self.assertEqual(parse(content1), ["abc"])
        content2 = " def"
        self.assertEqual(parse(content2), ["def"])
        content2 = "　\n　def \n \n "
        self.assertEqual(parse(content2), ["def"])

    def test_utility(self):
        self.assertEqual(toCSV([111,543,232]), "111,543,232")
        self.assertEqual(toCSV([]), "")
        self.assertEqual(toCSV(["abc","ppp"]), "abc,ppp")

    def test_like(self):
        pass



if __name__ == "__main__":
    unittest.main()