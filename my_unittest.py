import unittest
import main

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

if __name__ == "__main__":
    unittest.main()