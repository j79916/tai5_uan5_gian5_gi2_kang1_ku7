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
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 資料庫連線
from 華語台語雙語語料庫系統.文章標點處理工具 import 文章標點處理工具
from 言語資料庫.常用方法 import 展開
from 言語資料庫.公用資料 import 標點符號
from 言語資料庫.公用資料 import 臺語腔口
from 言語資料庫.常用方法 import 提掉空白
from 言語資料庫.公用資料 import 揣文字上大流水號
from 言語資料庫.公用資料 import 文字組合邊界
from 言語資料庫.公用資料 import 文字組合符號
from 言語資料庫.公用資料 import 揣出組合中流水號的實際文字流水號
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 設定編修狀況
from 言語資料庫.公用資料 import 用流水號揣編修
from 言語資料庫.公用資料 import 加編修狀況
from 言語資料庫.公用資料 import 字詞

標點處理工具 = 文章標點處理工具()
標點處理工具.標點符號 = 標點符號

def 切法相像(參考, 原始, 切開語句):
	看到佗 = 0
	原始數量 = len(原始)
	無問題 = True
	正規語句 = []
	for 目標長度 in 參考:
		累積長度 = 0
		正規語句.append('')
		while 累積長度 < 目標長度:
			if 看到佗 >= 原始數量:
				無問題 = False
				break
			累積長度 += 原始[看到佗]
			正規語句[-1] += 切開語句[看到佗]
			看到佗 += 1
			if 累積長度 > 目標長度:
				無問題 = False
	return 無問題, 正規語句

def 插入文字(資料庫欄位, 資料庫紀錄):
	有存在無指令 = 'SELECT "流水號" FROM "言語"."文字" WHERE '
	for i in range(len(資料庫欄位)):
		if i > 0:
			有存在無指令 += (' AND ')
		有存在無指令 += (資料庫欄位[i])
		有存在無指令 += ('=')
		有存在無指令 += (資料庫紀錄[i])
	有存在無指令+=' ORDER BY "流水號"'
	流水號 = 資料庫連線.prepare(有存在無指令).first()
	if 流水號 == None:
		新紀錄指令 = ('INSERT INTO "言語"."文字" ' +
			'(' + ','.join(資料庫欄位) + ') VALUES (' + ','.join(資料庫紀錄) + ')')
		資料庫連線.prepare(新紀錄指令)()
		流水號 = 揣文字上大流水號()
		加編修狀況(流水號, '文字')		
	return 流水號

def 產生閩南語組合(流水號, 來源, 種類, 腔口, 地區, 年代, 組合, 型體, 音標, 調變, 音變):
	參考的切法 = None
	if 型體 != None:
		切開的型體 = 提掉空白(展開([標點處理工具.分離漢字(一个詞) for 一个詞 in 標點處理工具.切開語句(型體)[::1]]))
		型體的切法 = list(map(標點處理工具.計算漢字語句漢字數量, 切開的型體))
		參考的切法 = 型體的切法
	if 音標 != None:
		切開的音標 = 提掉空白(標點處理工具.切開語句(音標)[::1])
		音標的切法 = list(map(標點處理工具.計算音標語句音標數量, 切開的音標))
		參考的切法 = 音標的切法
	if 調變 != None:
		切開的調變 = 提掉空白(標點處理工具.切開語句(調變)[::1])
		調變的切法 = list(map(標點處理工具.計算音標語句音標數量, 切開的調變))
		參考的切法 = 調變的切法
	if 音變 != None:
		切開的音變 = 提掉空白(標點處理工具.切開語句(音變)[::1])
		音變的切法 = list(map(標點處理工具.計算音標語句音標數量, 切開的音變))
		參考的切法 = 音變的切法
	####
	print(切開的型體)
	print(切開的音標)
	print(參考的切法)
	資料一致 = True
	if 型體 != None:
		無問題, 正規型體語句 = 切法相像(參考的切法, 型體的切法, 切開的型體)
		資料一致 &= 無問題
	if 音標 != None:
		無問題, 正規音標語句 = 切法相像(參考的切法, 音標的切法, 切開的音標)
		資料一致 &= 無問題
	if 調變 != None:
		無問題, 正規調變語句 = 切法相像(參考的切法, 調變的切法, 切開的調變)
		資料一致 &= 無問題
	if 音變 != None:
		無問題, 正規音變語句 = 切法相像(參考的切法, 音變的切法, 切開的音變)
		資料一致 &= 無問題
		####
# 	print(參考的切法)
	if not 資料一致:
		設定編修狀況(流水號, '資料無一致')
		print('資料無一致')
		return
	if 參考的切法 == [1]:
		# 更新組合(#,#)
		print('是字')
		return []
	elif len(參考的切法) == 1:
		流水號組合 = []
		資料庫欄位 = ["來源", "種類", "腔口", "地區", "年代"]
		if 型體 != None:
			資料庫欄位.append('"型體"')
		if 音標 != None:
			資料庫欄位.append('"音標"')
			一个一个音標 = 正規音標語句[0].replace('--', '-').split('-')
		if 調變 != None:
			資料庫欄位.append('"調變"')
			一个一个調變 = 正規調變語句[0].replace('--', '-').split('-')
		if 音變 != None:
			資料庫欄位.append('"音變"')
			一个一个音變 = 正規音變語句[0].replace('--', '-').split('-')
		for i in range(len(切開的型體)):
			資料庫紀錄 = [ '\'' + str(欄位) + '\'' for 欄位 in [來源, 種類, 腔口, 地區, 年代]]
			if 型體 != None:
				資料庫紀錄.append('\'' + 切開的型體[i] + '\'')
			if 音標 != None:
				if i >= len(一个一个音標):
					break
				資料庫紀錄.append('\'' + 一个一个音標[i] + '\'')
			if 調變 != None:
				if i >= len(一个一个調變):
					break
				資料庫紀錄.append('\'' + 一个一个調變[i] + '\'')
			if 音變 != None:
				if i >= len(一个一个音變):
					break
				資料庫紀錄.append('\'' + 一个一个音變[i] + '\'')
			流水號組合.append(插入文字(資料庫欄位, 資料庫紀錄))
		return list(map(str, 流水號組合))

	資料庫欄位 = ["來源", "種類", "腔口", "地區", "年代"]
	if 型體 != None:
		資料庫欄位.append('"型體"')
	if 音標 != None:
		資料庫欄位.append('"音標"')
	if 調變 != None:
		資料庫欄位.append('"調變"')
	if 音變 != None:
		資料庫欄位.append('"音變"')
		####
	流水號組合 = []
	for i in range(len(參考的切法)):
		資料庫紀錄 = [ '\'' + str(欄位) + '\'' for 欄位 in [來源, 字詞, 腔口, 地區, 年代]]
		if 型體 != None:
			資料庫紀錄.append('\'' + 正規型體語句[i] + '\'')
		if 音標 != None:
			資料庫紀錄.append('\'' + 正規音標語句[i] + '\'')
		if 調變 != None:
			資料庫紀錄.append('\'' + 正規調變語句[i] + '\'')
		if 音變 != None:
			資料庫紀錄.append('\'' + 正規音變語句[i] + '\'')
		####
		流水號組合.append(插入文字(資料庫欄位, 資料庫紀錄))
# 		print(','.join(資料庫欄位) + ' VALUES (' + ','.join(資料庫紀錄) + ')')
	return list(map(str, 流水號組合))


設定組合 = lambda 流水號, 組合: 資料庫連線.prepare('UPDATE "言語"."文字" ' +
	'SET "組合"=$2 ' +
	'WHERE "流水號"=$1')(流水號, 組合)

揣指定組合文字 = lambda : 資料庫連線.prepare('SELECT "流水號","來源","種類","腔口","地區","年代","組合","型體","音標","調變","音變" ' +
	'FROM "言語"."文字" WHERE "組合" NOT LIKE \'#%#\' ORDER BY "流水號" DESC')()

for 流水號, 來源, 種類, 腔口, 地區, 年代, 組合, 型體, 音標, 調變, 音變 in 揣指定組合文字():
	print(流水號)
	編修資料 = 用流水號揣編修(流水號)
	if 編修資料[1] != '正常':
		continue
	print(型體)
	指定流水號 = 組合.split(文字組合符號)[1]
	if 腔口.startswith(臺語腔口):
		語句流水號組合 = 產生閩南語組合(流水號, 來源, 種類, 腔口, 地區, 年代, 組合, 型體, 音標, 調變, 音變)
		實際文字流水號 = str(揣出組合中流水號的實際文字流水號(指定流水號))
		if 語句流水號組合==None:
			continue
		print(實際文字流水號)
		print(組合.split(文字組合符號)[1])
		上尾流水號組合 = []
		有改著 = False
		for 語句流水號 in 語句流水號組合:
			if 語句流水號 == 實際文字流水號:
				上尾流水號組合.append(str(指定流水號))
				有改著 = True
			else:
				上尾流水號組合.append(語句流水號)
		print(語句流水號組合)
		print(上尾流水號組合)
		if 有改著:
			if 語句流水號組合 == []:
				設定組合(流水號, 文字組合邊界 + 文字組合符號 + 文字組合邊界)
			elif 語句流水號組合 != None:
				設定組合(流水號, 文字組合邊界 + 文字組合符號 + 文字組合符號.join(語句流水號組合)
				+ 文字組合符號 + 文字組合邊界)
		else:
			設定編修狀況(流水號, '組合指定有問題')


# while True:
# 	a = 3

用揣無組合文字 = lambda : 資料庫連線.prepare('SELECT "流水號","來源","種類","腔口","地區","年代","組合","型體","音標","調變","音變" ' +
	'FROM "言語"."文字" WHERE "組合" IS NULL ORDER BY "流水號" DESC')()

for 流水號, 來源, 種類, 腔口, 地區, 年代, 組合, 型體, 音標, 調變, 音變 in 用揣無組合文字():
	print(流水號)
	編修資料 = 用流水號揣編修(流水號)
	if 編修資料[1] != '正常':
		continue
	print(型體)
# 	print(音標)
	if 腔口.startswith(臺語腔口):
		語句流水號組合 = 產生閩南語組合(流水號, 來源, 種類, 腔口, 地區, 年代, 組合, 型體, 音標, 調變, 音變)
		if 語句流水號組合 == []:
			設定組合(流水號, 文字組合邊界 + 文字組合符號 + 文字組合邊界)
		elif 語句流水號組合 != None:
# 			print (','.join(語句流水號組合))
			設定組合(流水號, 文字組合邊界 + 文字組合符號 + 文字組合符號.join(語句流水號組合)
				+ 文字組合符號 + 文字組合邊界)
