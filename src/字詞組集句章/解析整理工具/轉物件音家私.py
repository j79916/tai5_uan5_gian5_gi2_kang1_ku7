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
from 字詞組集句章.基本元素.字 import 字
from 字詞組集句章.基本元素.詞 import 詞
from 字詞組集句章.基本元素.組 import 組
from 字詞組集句章.基本元素.集 import 集
from 字詞組集句章.基本元素.句 import 句
from 字詞組集句章.基本元素.章 import 章
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤
from 字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 字詞組集句章.基本元素.公用變數 import 無音
from 字詞組集句章.基本元素.公用變數 import 標點符號

class 轉物件音家私():
	# 逐个函式攏愛產生新的物件
	def 字轉做標準音標(self, 音標工具, 字物件):
		if not isinstance(字物件, 字):
			raise 型態錯誤('傳入來的毋是字物件：{0}'.format(str(字物件)))
		if 字物件.型 in 標點符號 and 字物件.音 in 標點符號:
			新音 = 字物件.音
		elif 字物件.音 != 無音:
			新音物件 = 音標工具(字物件.音)
			if 新音物件 == None:
				raise 解析錯誤('音標無合法：{0}'.format(str(字物件)))
			if 新音物件.標準音標() == None:
				raise 解析錯誤('音標無法度轉：{0}'.format(str(字物件)))
			新音 = 新音物件.標準音標()
		else:
			新音 = 無音
		新型物件 = 音標工具(字物件.型)
		if 字物件.音.startswith(字物件.型):
			新型 = 新音
		elif 新型物件 != None and 新型物件.標準音標() != None:
			新型 = 新型物件.標準音標()
		else:
			新型 = 字物件.型
		return 字(新型, 新音)

	def 詞轉做標準音標(self, 音標工具, 詞物件):
		if not isinstance(詞物件, 詞):
			raise 型態錯誤('傳入來的毋是詞物件：{0}'.format(str(詞物件)))
		新詞物件 = 詞()
		for 字 in 詞物件.內底字:
			新詞物件.內底字.append(self.字轉做標準音標(音標工具, 字))
		return 新詞物件

	def 組轉做標準音標(self, 音標工具, 組物件):
		if not isinstance(組物件, 組):
			raise 型態錯誤('傳入來的毋是組物件：{0}'.format(str(組物件)))
		新組物件 = 組()
		for 詞 in 組物件.內底詞:
			新組物件.內底詞.append(self.詞轉做標準音標(音標工具, 詞))
		return 新組物件

	def 集轉做標準音標(self, 音標工具, 集物件):
		if not isinstance(集物件, 集):
			raise 型態錯誤('傳入來的毋是集物件：{0}'.format(str(集物件)))
		新集物件 = 集()
		for 組 in 集物件.內底組:
			新集物件.內底組.append(self.組轉做標準音標(音標工具, 組))
		return 新集物件

	def 句轉做標準音標(self, 音標工具, 句物件):
		if not isinstance(句物件, 句):
			raise 型態錯誤('傳入來的毋是句物件：{0}'.format(str(句物件)))
		新句物件 = 句()
		for 集 in 句物件.內底集:
			新句物件.內底集.append(self.集轉做標準音標(音標工具, 集))
		return 新句物件

	def 章轉做標準音標(self, 音標工具, 章物件):
		if not isinstance(章物件, 章):
			raise 型態錯誤('傳入來的毋是章物件：{0}'.format(str(章物件)))
		新章物件 = 章()
		for 句 in 章物件.內底句:
			新章物件.內底句.append(self.句轉做標準音標(音標工具, 句))
		return 新章物件

	def 轉做標準音標(self, 音標工具, 物件):
		if isinstance(物件, 字):
			return self.字轉做標準音標(音標工具, 物件)
		if isinstance(物件, 詞):
			return self.詞轉做標準音標(音標工具, 物件)
		if isinstance(物件, 組):
			return self.組轉做標準音標(音標工具, 物件)
		if isinstance(物件, 集):
			return self.集轉做標準音標(音標工具, 物件)
		if isinstance(物件, 句):
			return self.句轉做標準音標(音標工具, 物件)
		if isinstance(物件, 章):
			return self.章轉做標準音標(音標工具, 物件)
		raise 型態錯誤('傳入來的毋是字詞組集句章其中一種物件：{0}，{1}'
			.format(type(物件), str(物件)))
