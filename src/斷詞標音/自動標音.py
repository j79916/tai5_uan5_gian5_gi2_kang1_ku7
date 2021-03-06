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
from 資料庫.欄位資訊 import 偏漳優勢音腔口
from 資料庫.欄位資訊 import 偏泉優勢音腔口
from 資料庫.欄位資訊 import 混合優勢音腔口
from 斷詞標音.閩南語標音整合 import 閩南語標音整合
from 字詞組集句章.綜合標音.句綜合標音 import 句綜合標音
from 字詞組集句章.綜合標音.閩南語字綜合標音 import 閩南語字綜合標音
from 斷詞標音.客話標音整合 import 客話標音整合
from 資料庫.欄位資訊 import 四縣腔
from 資料庫.欄位資訊 import 海陸腔
from 資料庫.欄位資訊 import 大埔腔
from 資料庫.欄位資訊 import 饒平腔
from 資料庫.欄位資訊 import 詔安腔
from 字詞組集句章.綜合標音.客話字綜合標音 import 客話字綜合標音
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 斷詞標音.型音辭典 import 型音辭典
from 斷詞標音.國語標音整合 import 國語標音整合
from 斷詞標音.現掀辭典 import 現掀辭典
from 資料庫.欄位資訊 import 國語臺員腔
from 字詞組集句章.綜合標音.國語字綜合標音 import 國語字綜合標音
from 斷詞標音.排標音結果 import 排標音結果

class 自動標音():
	標音模組 = {
		(閩南語標音整合, 閩南語字綜合標音, 現掀辭典):[偏漳優勢音腔口, 偏泉優勢音腔口, 混合優勢音腔口],
		(客話標音整合, 客話字綜合標音, 現掀辭典):[四縣腔, 海陸腔, 大埔腔, 饒平腔, 詔安腔],
		(國語標音整合, 國語字綜合標音, 現掀辭典):[國語臺員腔],
		}
	支援腔口 = None
	腔口標音工具 = None
	腔口綜合標音 = None
	排標音 = 排標音結果()
# 	支援腔口 = {偏漳優勢音腔口:(閩南語偏漳標音,閩南語字綜合標音),
# 		偏泉優勢音腔口:(閩南語偏泉標音,閩南語字綜合標音),
# 		混合優勢音腔口:(閩南語混合標音,閩南語字綜合標音),
# 		四縣腔:(客家話四縣標音,客話字綜合標音),
# 		海陸腔:(客家話海陸標音,客話字綜合標音),
# 		大埔腔:(客家話大埔標音,客話字綜合標音),
# 		饒平腔:(客家話饒平標音,客話字綜合標音),
# 		詔安腔:(客家話詔安標音,客話字綜合標音),
# 		}
	def __init__(self):
		self.支援腔口 = set()
		self.腔口標音工具 = {}
		self.腔口綜合標音 = {}
		for 工具, 腔口 in self.標音模組.items():
			標音整合, 字綜合標音, 辭典 = 工具
			for 腔 in 腔口:
				標音工具 = 標音整合(腔, 辭典)
				self.支援腔口.add(腔)
				self.腔口標音工具[腔] = 標音工具
				self.腔口綜合標音[腔] = 字綜合標音
		return
	
	def 有支援無(self,腔):
		return 腔 in self.支援腔口
		
	def 語句標音(self, 查詢腔口, 查詢語句):
		if 查詢腔口 not in self.腔口綜合標音:
			raise(解析錯誤, '腔口毋著：{0}'.format(查詢腔口))
		字綜合標音 = self.腔口綜合標音[查詢腔口]
		章物件 = self.語句斷詞標音(查詢腔口, 查詢語句)
		標音句 = 句綜合標音(字綜合標音, 章物件)
		return 標音句.轉json格式()
	
	def 語句斷詞標音(self, 查詢腔口, 查詢語句):
		if 查詢腔口 not in self.腔口標音工具:
			raise(解析錯誤, '腔口毋著：{0}'.format(查詢腔口))
		標音工具 = self.腔口標音工具[查詢腔口]
		章物件 = 標音工具.語句斷詞標音(查詢語句)
		排好章物件 = self.排標音.照白文層排(章物件)
		return 排好章物件
	
	def 物件斷詞標音(self, 查詢腔口, 查詢物件):
		if 查詢腔口 not in self.腔口標音工具:
			raise(解析錯誤, '腔口毋著：{0}'.format(查詢腔口))
		標音工具 = self.腔口標音工具[查詢腔口]
		章物件 = 標音工具.物件斷詞標音(查詢物件)
		排好章物件 = self.排標音.照白文層排(章物件)
		return 排好章物件
	
	def 物件綜合標音(self, 查詢腔口, 查詢物件):
		if 查詢腔口 not in self.腔口標音工具:
			raise(解析錯誤, '腔口毋著：{0}'.format(查詢腔口))
		字綜合標音 = self.腔口綜合標音[查詢腔口]
		標音句 = 句綜合標音(字綜合標音, 查詢物件)
		return 標音句.轉json格式()
