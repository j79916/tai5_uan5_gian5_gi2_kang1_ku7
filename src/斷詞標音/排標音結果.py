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
from 字詞組集句章.解析整理工具.集內組照排 import 集內組照排
from 斷詞標音.辭典條目 import 辭典條目

class 排標音結果:
	組照排 = 集內組照排()
	條目 = 辭典條目()
	文讀層 = None
	白話層 = None
	def __init__(self):
		self.文讀層 = self.條目.文讀層
		self.白話層 = self.條目.白話層

	def 照白文層排(self, 物件):
		return self.組照排.排好(self.白文照排, 物件)

	def 白文照排(self, 組物件):
		詞物件 = 組物件.內底詞[0]
		白 = 0
		文 = 0
		流水號=0
		if hasattr(詞物件, '屬性'):
			if self.白話層 in 詞物件.屬性:
				白 = -詞物件.屬性[self.白話層]
			if self.文讀層 in 詞物件.屬性:
				文 = 詞物件.屬性[self.文讀層]
			if '流水號' in 詞物件.屬性:
				流水號 = 詞物件.屬性['流水號']
		return (白, 文,流水號)
