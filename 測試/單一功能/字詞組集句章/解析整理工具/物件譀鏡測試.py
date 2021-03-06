"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import unittest
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡

class 物件譀鏡測試(unittest.TestCase):
	def setUp(self):
		self.分析器 = 拆文分析器()
		self.譀鏡 = 物件譀鏡()
	def tearDown(self):
		pass

	def test_看字(self):
		型 = '我'
		音 = 'gua2'
		字物件 = self.分析器.產生對齊字(型, 音)
		self.assertEqual(self.譀鏡.看型(字物件), 型)
		self.assertEqual(self.譀鏡.看音(字物件), 音)

	def test_看詞(self):
		型 = '姑娘'
		音 = 'koo1-niu5'
		詞物件 = self.分析器.產生對齊詞(型, 音)
		self.assertEqual(self.譀鏡.看型(詞物件), 型)
		self.assertEqual(self.譀鏡.看音(詞物件), 音)

	def test_看組孤字(self):
		型 = '恁老母ti3佗位！'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7 !'
		組物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(self.譀鏡.看型(組物件), 型)
		self.assertEqual(self.譀鏡.看音(組物件), 音)

	def test_看組連字(self):
		型 = '恁老母ti3佗位！'
		音 = 'lin1 lau3-bu2 ti3 to1-ui7 !'
		組物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(self.譀鏡.看型(組物件), 型)
		self.assertEqual(self.譀鏡.看音(組物件), 音)

	def test_看集(self):
		型 = '恁老母ti3佗位'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7'
		集物件 = self.分析器.產生對齊集(型, 音)
		self.assertEqual(self.譀鏡.看型(集物件), 型)
		self.assertEqual(self.譀鏡.看音(集物件), 音)

	def test_看集內底有兩組以上(self):
		型 = '恁老母ti3佗位'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7'
		集物件 = 集([self.分析器.產生對齊組(型, 音), self.分析器.產生對齊組(型, 音)])
		self.assertRaises(解析錯誤, self.譀鏡.看型, 集物件)
		self.assertRaises(解析錯誤, self.譀鏡.看音, 集物件)

	def test_看句(self):
		型 = '恁老母ti3佗位'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7'
		句物件 = self.分析器.產生對齊句(型, 音)
		self.assertEqual(self.譀鏡.看型(句物件), 型)
		self.assertEqual(self.譀鏡.看音(句物件), 音)

	def test_看章(self):
		型 = '恁老母ti3佗位！恁老母ti3佗位！'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! lin1 lau3-bu2 ti3 to1-ui7 !'
		章物件 = self.分析器.產生對齊章(型, 音)
		self.assertEqual(self.譀鏡.看型(章物件), 型)
		self.assertEqual(self.譀鏡.看音(章物件), 音)

	def test_看章換符合(self):
		型 = '恁老母ti3佗位！恁老母ti3佗位！'
		音 = 'lin1 lau3 bu2 ti3 to1 ui7 ! lin1 lau3 bu2 ti3 to1 ui7 !'
		章物件 = self.分析器.產生對齊組(型, 音)
		self.assertEqual(self.譀鏡.看型(章物件), 型)
		self.assertEqual(self.譀鏡.看音(章物件), 音)


if __name__ == '__main__':
	unittest.main()
