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
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib

class 連線控制器(BaseHTTPRequestHandler):
	def 輸出(self, 資料):
		self.wfile.write(str(資料).encode(encoding='utf_8', errors='strict'))
	def 送出位元資料(self, 位元組):
		self.wfile.write(位元組)
	def 連線路徑(self):
		return urllib.parse.unquote(self.path)
	def 送出連線成功資訊(self, 資料型態='text/html'):
		self.send_response(200)
		self.send_header('Content-type', 資料型態)
		self.end_headers()
	def 送出連線錯誤資訊(self, 狀態編號):
		self.send_response(狀態編號)
		self.end_headers()

if __name__ == '__main__':
	try:
		server = HTTPServer(('', 8000), 連線控制器)
		print ('started httpserver...')
		server.serve_forever()
	except KeyboardInterrupt:
		print ('^C received, shutting down server')
		server.socket.close()
