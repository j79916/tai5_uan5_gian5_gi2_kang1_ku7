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
from 資料佮語料匯入整合.整理中的台語詞典.詞六國語通用拼音轉注音符號表 import 通用佮注音聲韻轉換表
from 資料佮語料匯入整合.整理中的台語詞典.詞六國語通用拼音轉注音符號表 import 通用佮注音調轉換表
from 資料庫.資料庫連線 import 資料庫連線
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.轉物件音家私 import 轉物件音家私
from 字詞組集句章.解析整理工具.物件譀鏡 import 物件譀鏡
from 字詞組集句章.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from 資料庫.欄位資訊 import 臺員
from 資料庫.欄位資訊 import 字詞
from 資料庫.整合.整合入言語 import 加文字佮版本
from 資料庫.整合.整合入言語 import 加關係
from 資料庫.欄位資訊 import 義近
from 資料庫.欄位資訊 import 會當替換
from 字詞組集句章.解析整理工具.解析錯誤 import 解析錯誤

class 整理中的台語詞典06:

	# 通用佮注音聲韻轉換表.update()
	# 通用佮注音調轉換表.update({'5':'ˊ'})
	詞典06調整表 = [('5', '2'), ('chii', 'chih'), ('shii', 'shih'), ('zhii', 'jhih'), ('zii', 'zih'),
			('sii', 'sih'), ('rhii', 'rih'),
			('y', 'i'), ('ii', 'i'), ('zi', 'ji'), ('jih', 'zih'), ('w', 'u'), ('uu', 'u'), ('er', 'e'),
			('ung', 'ong'), ('ien', 'ian'), ('au', 'ao'), ('uo', 'o'),
			('rh', 'r'), ('zh', 'jh'), ('ung', 'uong'),
			('chng', 'cheng'), ('dng', 'deng'), ('fng', 'fong'), ('gng', 'geng'), ('hng', 'heng'),
			('mng', 'meng'), ('lng', 'leng'), ('png', 'peng'), ('rng', 'reng'), ('shng', 'sheng'),
			('nng', 'neng'), ('bng', 'beng'), ('sng', 'seng'), ('tng', 'teng'), ('zng', 'zeng'),
			('cng', 'ceng'), ('kng', 'keng'), ]

	揣台華資料 = 資料庫連線.prepare('SELECT "識別碼","華語漢字","華語音標","台語漢字","台語音標" ' +
		'FROM "整理中的台語詞典"."整理中的台語詞典06" ORDER BY "識別碼"')
	辭典名 = '整理中的台語詞典06'
	訓練 = False

	初胚工具 = 文章初胚工具()
	分析器 = 拆文分析器()
	轉音家私 = 轉物件音家私()
	譀鏡 = 物件譀鏡()
	def __init__(self):
		for 識別碼, 華語漢字, 華語音標, 台語漢字, 台語音標 in self.揣台華資料():
			try:
# 				print(識別碼)
				文字資料 = []
				台語音 = []
				for 音 in 台語音標.strip()[1:-1].split('-'):
					台語音.append(音[1:-1].split('/'))
				攏總音 = []
				self.揣出全部組合(台語音, 0, '', 攏總音)
			# 	print(攏總音)
				for 台音 in 攏總音:
					音 = 台音.strip()
					if 音 != '':
						處理過型=self.初胚工具.數字調英文中央加分字符號(台語漢字)
						處理過音=音.replace('8','6')
						處理過音=處理過音.replace('h4','h7')
						處理過音=處理過音.replace('p4','p7')
						處理過音=處理過音.replace('t4','t7')
						處理過音=處理過音.replace('k4','k7')
						通用詞物件 = self.分析器.產生對齊詞(處理過型, 處理過音)
						臺羅詞物件 = self.轉音家私.轉做標準音標(通用拼音音標, 通用詞物件)
						# 來源, 種類, 腔口, 地區, 年代, 型體, 音標, 版本
						文字資料.append((self.辭典名, 字詞, '漢語族閩方言閩南語', 臺員, 88,
								self.譀鏡.看型(臺羅詞物件), self.譀鏡.看音(臺羅詞物件), '正常'))
				國語音 = []
				for 音 in 華語音標.strip()[1:-1].split('-'):
					國語音.append(音[1:-1].split('/'))
			# 	print(國語音)
				攏總國語音 = []
				self.揣出全部組合順紲做國語處理(國語音, 0, '', 攏總國語音)
				for 國音 in 攏總國語音:
					文字資料.append((self.辭典名, 字詞, '漢語族官話方言北京官話臺灣腔', 臺員, 93, 華語漢字, 國音, '正常'))
			except Exception as 錯誤:
				print(識別碼, 華語漢字, 華語音標, 台語漢字, 台語音標, 錯誤)
			else:
				if self.訓練:
					print(文字資料)
					流水號 = []
					for 來源, 種類, 腔口, 地區, 年代, 型體, 音標, 版本 in 文字資料:
						流水號.append(加文字佮版本(來源, 種類, 腔口, 地區, 年代, 型體, 音標, 版本))
					for i in range(len(流水號)):
						for j in range(i + 1, len(流水號)):
							加關係(流水號[i], 流水號[j], 義近, 會當替換)

	def 揣出全部組合(self, 音陣列, 位置, 累積音, 全部結果):
		if 位置 == len(音陣列):
			全部結果.append(累積音[1:])
			return
		for 音 in 音陣列[位置]:
			self.揣出全部組合(音陣列, 位置 + 1, 累積音 + '-' + 音, 全部結果)
		return

	def 揣出全部組合順紲做國語處理(self, 音陣列, 位置, 累積音, 全部結果):
		if 位置 == len(音陣列):
			全部結果.append(累積音[1:])
			return
		for 音 in 音陣列[位置]:
			原 = 音
			for 舊, 新 in self.詞典06調整表:
				音 = 音.replace(舊, 新)
			if 音[:-1] in 通用佮注音聲韻轉換表 and 音[-1] in 通用佮注音調轉換表:
				self.揣出全部組合順紲做國語處理(音陣列, 位置 + 1,
					累積音 + ' ' + 通用佮注音聲韻轉換表[音[:-1]] + 通用佮注音調轉換表[音[-1]], 全部結果)
			else:
				raise 解析錯誤(原 + " →" + 音 + " 無法度轉")
		return

if __name__ == '__main__':
	整理中的台語詞典06()
