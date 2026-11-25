from http.server import HTTPServer,SimpleHTTPRequestHandler
'''
دو ابزار از ماژول http.server وارد می‌کنیم:
- HTTPServer: ساخت سرور HTTP
- SimpleHTTPRequestHandler: مدیریت درخواست‌های مرورگر و ارسال فایل‌ها
'''
server=HTTPServer(('localhost',8001),SimpleHTTPRequestHandler)
server.serve_forever() #سرور را روشن نگه می‌داریم تا درخواست‌های مرورگر را دریافت کند.
