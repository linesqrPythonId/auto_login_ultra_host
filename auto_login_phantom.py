import pickle
import os
import time
import sys
import platform
from datetime import date
from selenium import webdriver
#from pyvirtualdisplay import Display #linux only
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

global has_server
has_server=0
platform_os = "NULL"
sinkronus = 0

#elemen xpath dari strong alias gagal "/html/body/div[3]/div[3]/center/div[5]/div[2]/div/div/strong"
def auto_request_ultra(user, sandi, platform_code):
	try:
		director = os.path.dirname(os.path.abspath( __file__ ))
		#virtual = Display(visible=0, size=(1024,768))
		#virtual.start()
		print('hasil: '+platform_code)
		print("[DEBUG] Membuka Webdriver")
		if platform_code == "windows":
			chromedriver = director+ "\data\phantomjs.exe"
			#print("yoho")
			time.sleep(5)
			browser = webdriver.PhantomJS(chromedriver,service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
			#print("kohi")
		elif platform_code == "linux":
			#print("joy")
			browser = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])			#make sure you set it properly :D
		print("[DEBUG] Sinkronisasi system webdriver")
		time.sleep(10)
		#browser.set_window_size(1152,768)
		browser.maximize_window()
		browser.get('https://www.ultra-h.com/home.php')
		cookie_dictionary = browser.get_cookies()
		browser.delete_all_cookies()
		for item in cookie_dictionary: 
			browser.add_cookie({
      			'domain': '.ultra-h.com', # note the dot at the beginning
      			'name': 'cookieconsent_dismissed',
      			'value': 'yes',
      			'path': '/',
      			'expires': None
    })

		#browser.get('https://www.ultra-h.com/home.php')
	#name = {"cookieconsent_dismissed":"yes"}
		#used browser.add_cookie({'name':'cookieconsent_dismissed', 'value':'yes'})
		#browser.add_cookie({'name':'cookieconsent_dismissed', 'value':'yes','domain':'ultra-h.com'})
		print("[DEBUG] Menambahkan Cookie ke dalam Webdriver")
		#WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/span")))
		time.sleep(40)
		while True:
			if EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/span")):
				counter_server = browser.find_element_by_xpath("/html/body/div[2]/span")
				print("[DEBUG] Mecengek Jumlah Server yang ada")
				server_int = counter_server.text
				break
			else: server_int = -1
		print('[DEBUG] Banyak Server yang tersedia: '+ server_int)
		if int(server_int) == 0:
			print("[DEBUG] Tidak ada list server, Membatalkan sesi")
			browser.quit()
			print("Menutup Aplikasi, dan webdriver")
			sys.exit(1)
			os.system('kill %d' % os.getpid())
	#browser.add_cookie(name);
		time.sleep(20)
		konten = str(browser.current_url)
		if konten =="https://www.ultra-h.com/login.php":
			username = browser.find_element_by_name("username")
			password = browser.find_element_by_name("password")
	#browser.findElement(By.xpath("/html/body/div[1]/div/a[1]")).click();
			print("[DEBUG] Login dengan user: " + user + " dan password: " + sandi)
			username.send_keys(user)
			password.send_keys(sandi)

			browser.find_element_by_id("login").click()
			time.sleep(40)
			kotak = os.path.dirname(os.path.abspath( __file__ ))
			if platform_os == "linux":
				browser.save_screenshot(kotak+'/meow.png')
			else:
				browser.save_screenshot(kotak+'\meow.png')
			print("[DEBUG] Ambil Screenshot")			
	#browser.get('https://www.ultra-h.com/home.php')
		try:
			#WebDriverWait(browser, 30).until(browser.current_url == 'https://www.ultra-h.com/home.php')
			linker2 = str(browser.execute_script("return document.location.href;"))
			if temp_file == linker2:
				print("[ERROR] Tampaknya Credential Login Anda Tidak Diterima Silahkan Cek Kembali akun anda")
				sys.exit(1)
				os.system('kill %d' % os.getpid())
			elif linker2 == 'https://www.ultra-h.com/home.php':
				print("[DEBUG] Credential Login Diterima")
			NEXT_BUTTON_XPATH = "/html/body/div[3]/div[3]/center/div[5]/table/tbody/tr[2]/td[8]/form[1]/input[2]"
    	# we have to wait for the page to refresh, the last thing that seems to be updated is the title
			WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, NEXT_BUTTON_XPATH)))
			if platform_os == "linux":
				browser.save_screenshot(kotak+'/meow.png')
			else:
				browser.save_screenshot(kotak+'\meow.png')
			if EC.presence_of_element_located((By.XPATH, NEXT_BUTTON_XPATH)):
				print("[DEBUG] Anda sudah memiliki sebuah server")
				has_server = 1
				print("[DEBUG] Mengalihkan Menuju Auto Absen Mode")
				#auto_login_ultra(user,sandi) 
			for cookie in browser.get_cookies():
				print((cookie['name'], cookie['value']))
		#browser.find_element_by_xpath('/html/body/div[1]/div/a[1]').click()
    	# You should see "cheese! - Google Search"
		#browser.find_element_by_name("Manage").click()
		#browser.findElement(By.xpath("//a[@class='button allow']/span[text()='Got it!']")).click(); 
			button = browser.find_element_by_xpath(NEXT_BUTTON_XPATH)
			#button.click()
			time.sleep(10)
			kotak = os.path.dirname(os.path.abspath( __file__ ))
			print("[DEBUG] Buka web Request Ultra Host")
			if platform_os == "linux":
				browser.save_screenshot(kotak+'/meow.png')
			else:
				browser.save_screenshot(kotak+'\meow.png')
			browser.get('http://www.ultra-h.com/request.php')
			if platform_os == "linux":
				browser.save_screenshot(kotak+'/meow.png')
			else:
				browser.save_screenshot(kotak+'\meow.png')
			#time.sleep(10)
			elemen = browser.find_element_by_id("s_host")
			print("ok elemen")
			opsi = elemen.find_elements_by_tag_name("option")
			print("ok opsi")
			for option in opsi:
				if "(Taken)" not in option.get_attribute("innerHTML"):
					#print("Server yang ada: %s" % option.get_attribute("value"))
					print("Server yang ada: %s" % option.get_attribute("innerHTML"))
			porting = str(input("Masukkan Portnya (cukup portnya saja): "))
			#select = Select(browser.find_element_by_id("s_host"))
			#select.select_by_visible_text(porting)
			if platform_os == "linux":
				browser.save_screenshot(kotak+'/meow.png')
			else:
				browser.save_screenshot(kotak+'\meow.png')
			for option in opsi:
				if "(Taken)" not in option.get_attribute("innerHTML"):
					if porting in option.get_attribute("innerHTML"):
						print ("Anda memilih server: "+ option.get_attribute("innerHTML"))
						option.click()
						break
						#print("Port yang ada: %s" % option.get_attribute("value"))
						#print("Status yang ada: %s" % option.get_attribute("innerHTML"))
			if platform_os == "linux":
				browser.save_screenshot(kotak+'/meow.png')
			else:
				browser.save_screenshot(kotak+'\meow.png')
			browser.find_element_by_name("Rules_3").click()
			browser.find_element_by_name("Rules_4").click()
			browser.find_element_by_name("Rules_0").click()
			browser.find_element_by_name("Rules_5").click()
			browser.find_element_by_name("Rules_2").click()
			browser.find_element_by_name("Rules_1").click()
			#for xpath request server "/html/body/div[3]/div[3]/center/form/input"
			browser.find_element_by_xpath("/html/body/div[3]/div[3]/center/form/input").click()
			if platform_os == "linux":
				browser.save_screenshot(kotak+'/meow.png')
			else:
				browser.save_screenshot(kotak+'\meow.png')
			print("[DEBUG] Screenshot Updated")
		finally:
			kotak = os.path.dirname(os.path.abspath( __file__ ))
		#browser.find_element_by_name("Manage").click()
			linker = str(browser.execute_script("return document.location.href;"))
			while linker != "https://www.ultra-h.com/panel.php":
				if (has_server == 1):
					print("[DEBUG] Terminate App, Reason = Anda Sudah Mempunyai Sebuah Server")
					break
				if(linker == "https://www.ultra-h.com/panel.php" ): break
				linker = str(browser.execute_script("return document.location.href;"))
				#print(linker) #just for debug
			#WebDriverWait(browser, 30).until(browser.current_url == 'https://ultra-h.com/panel.php')
			print('[DEBUG] Link Terakhir Sebelum Request Selesai '+'"'+browser.execute_script("return document.location.href;")+'"')
			if platform_os == "linux":
				print('[DEBUG] Mengambil Screenshot dan disimpan di: '+ '"'+kotak+'/meow.png"')
			else:
				print('[DEBUG] Mengambil Screenshot dan disimpan di: '+ '"'+kotak+'\meow.png"')
			if platform_os == "linux":
				browser.save_screenshot(kotak+'/meow.png')
			else:
				browser.save_screenshot(kotak+'\meow.png')
			print ("[DEBUG] Request Selesai Menutup Webdriver")
			#print(browser.current_url) #currently not used
			sys.exit(1)
			os.system('kill %d' % os.getpid())
			#print ("[INFO] Jangan Menutup Aplikasi, jika anda ingin menggunakan fitur syncronus")
		#then we exit the server
			browser.quit()
	except Exception as e:
		print(e)
		print("[ERROR] Terdapat Kesalahan dalam melakukan Request")
		#print("[USAGE] auto_login_ultra(user,password) -> with quotes")

def auto_login_ultra(user, sandi, platform_code):
	try:
		director = os.path.dirname(os.path.abspath( __file__ ))
		#virtual = Display(visible=0, size=(1024,768))
		#virtual.start()
		print("[DEBUG] Membuka Webdriver")
		if platform_code == "windows":
			chromedriver = director+ "\data\phantomjs.exe"
			browser = webdriver.PhantomJS(chromedriver,service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
		elif platform_code == "linux":
			browser = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])			#make sure you set it properly :D
		#browser.set_window_size(1152,768)
		print("[DEBUG] Sinkronisasi system webdriver")
		time.sleep(10)
		browser.maximize_window()
		browser.get('https://www.ultra-h.com/home.php')
		cookie_dictionary = browser.get_cookies()
		browser.delete_all_cookies()
		for item in cookie_dictionary: 
			browser.add_cookie({
      			'domain': '.ultra-h.com', # note the dot at the beginning
      			'name': 'cookieconsent_dismissed',
      			'value': 'yes',
      			'path': '/',
      			'expires': None
    })

		#browser.get('https://www.ultra-h.com/home.php')
	#name = {"cookieconsent_dismissed":"yes"}
		#used browser.add_cookie({'name':'cookieconsent_dismissed', 'value':'yes'})
		#browser.add_cookie({'name':'cookieconsent_dismissed', 'value':'yes','domain':'ultra-h.com'})
		print("[DEBUG] Menambahkan Cookie ke dalam Webdriver")
	#browser.add_cookie(name);
		time.sleep(20)
		konten = str(browser.current_url)
		if konten =="https://www.ultra-h.com/login.php":
			username = browser.find_element_by_name("username")
			password = browser.find_element_by_name("password")
	#browser.findElement(By.xpath("/html/body/div[1]/div/a[1]")).click();
			print("[DEBUG] Login dengan user: " + user + " dan password: " + sandi)
			username.send_keys(user)
			password.send_keys(sandi)

			browser.find_element_by_id("login").click()
			temp_file = browser.current_url
			time.sleep(40)
			kotak = os.path.dirname(os.path.abspath( __file__ ))
			if platform_os == "linux":
				browser.save_screenshot(kotak+'/meow.png')
			else:
				browser.save_screenshot(kotak+'\meow.png')
			print("[DEBUG] Ambil Screenshot")			
	#browser.get('https://www.ultra-h.com/home.php')
		try:
			#WebDriverWait(browser, 30).until(browser.current_url == 'https://www.ultra-h.com/home.php')
			linker2 = str(browser.execute_script("return document.location.href;"))
			if temp_file == linker2:
				print("[ERROR] Tampaknya Credential Login Anda Tidak Diterima Silahkan Cek Kembali akun anda")
				sys.exit(1)
				os.system('kill %d' % os.getpid())
			elif linker2 == 'https://www.ultra-h.com/home.php':
				print("[DEBUG] Credential Login Diterima")
			NEXT_BUTTON_XPATH = "/html/body/div[3]/div[3]/center/div[5]/table/tbody/tr[2]/td[8]/form[1]/input[2]"
    	# we have to wait for the page to refresh, the last thing that seems to be updated is the title
			WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, NEXT_BUTTON_XPATH)))
			while True:
				if EC.presence_of_element_located((By.XPATH, NEXT_BUTTON_XPATH)):
					print("Server Terdeteksi, Melakukan Auto Absen")
					has_server = 1
					break
				else:
					if browser.current_url == "https://www.ultra-h.com/login.php":
						print("[ERROR] Kesalahan Dalam Login, Reason: Tampaknya User atau Password anda salah, Terminate App")
						sys.exit(1)
						os.system('kill %d' % os.getpid())
						quit()
					print("Server Tidak Terdeteksi Melakukan Auto Request")
					auto_request_ultra(user, sandi,platform_os)
			for cookie in browser.get_cookies():
				print((cookie['name'], cookie['value']))
		#browser.find_element_by_xpath('/html/body/div[1]/div/a[1]').click()
    	# You should see "cheese! - Google Search"
		#browser.find_element_by_name("Manage").click()
		#browser.findElement(By.xpath("//a[@class='button allow']/span[text()='Got it!']")).click(); 
			button = browser.find_element_by_xpath(NEXT_BUTTON_XPATH)
			button.click()
		finally:
			kotak = os.path.dirname(os.path.abspath( __file__ ))
			#browser.save_screenshot(kotak+'\meow.png')
		#browser.find_element_by_name("Manage").click()
			linker = str(browser.execute_script("return document.location.href;"))
			while linker != "https://www.ultra-h.com/panel.php":
				if(linker == "https://www.ultra-h.com/panel.php" ): break
				linker = str(browser.execute_script("return document.location.href;"))
				#print(linker) #just for debug
			#WebDriverWait(browser, 30).until(browser.current_url == 'https://ultra-h.com/panel.php')
			print('[DEBUG] Link Terakhir Sebelum Login Sukses '+'"'+browser.execute_script("return document.location.href;")+'"')
			print('[DEBUG] Mengambil Screenshot dan disimpan di: '+ '"'+kotak+'\meow.png"')
			if platform_os == "linux":
				browser.save_screenshot(kotak+'/meow.png')
			else:
				browser.save_screenshot(kotak+'\meow.png')
			print ("[DEBUG] Login Sukses Menutup Webdriver")
			#print(browser.current_url) #currently not used
			if sinkronus == 1:
				print ("[INFO] Fitur Syncronus Aktif Jangan Menutup Aplikasi, jika anda ingin menggunakan fitur syncronus")
		#then we exit the server
			browser.quit()
	except Exception as e:
		print(e)
		print("[ERROR] Terdapat Kesalahan dalam melakukan Login")
		print("[USAGE] auto_login_ultra(user,password) -> with quotes")

def syncronus(usr,psd,os):
	print("[DEBUG] Syncronus sudah aktif menanti perubahan tanggal")
	global sinkronus
	sinkronus = 1
	auto_login_ultra(usr,psd,os)
	yourdate = date.today()
	while True:
		if yourdate < date.today():
			print("[DEBUG] Tanggal Sudah Berubah Melakukan Uji Prosedur")
			auto_login_ultra(usr,psd,os)
			print("[DEBUG] Setting Variabel Tanggal Jadi Sama Mencegah Bug")
			yourdate = date.today()

def utama():
	kotak = os.path.dirname(os.path.abspath( __file__ ))
	print (kotak)
	delta = open(kotak+'\data.txt', 'r')
	data = []
	user = []
	passwd = []
	#data=myfile.read().rstrip('\n').split(',')
	for line in delta:
		data.append(str(line).rstrip('\n'))
	i=0
	delta.close()
	while i <= len(data):
		if (i+2) <= len(data):
			user.append(str(data[i]))
			passwd.append(str(data[i+1]))
			print("Username: ", user)
			print("Password: ", passwd)
		i=i+2
		#print (i)
		if i > len(data): break
	for index in range(len(user)):
		print('Usernya: '+user[index])
		print('passnya: '+passwd[index])

def checking():
	#cek os dulu
	global platform_os
	os_hasil = str(platform.system())
	if os_hasil.lower() == "windows":
		print('[SUPPORTED] Platform Detected: '+platform.system())
		platform_os = "windows"
		time.sleep(3)
		main()
	elif os_hasil.lower() == "linux":
		print('[SUPPORTED] Platform Detected: '+platform.system())
		platform_os = "linux"
		time.sleep(3)
		main()
	else: 
		print('[UNSUPPORTED] This Script Doesnt Support with Your OS, Terminate')
		time.sleep(2)
		sys.exit(1)
		os.system('kill %d' % os.getpid())
	#main()

def main():
	err=0
	print("========================== Bot Server Ultra Host SAMP ==============================")
	print("============================== Versi : 1.0 Alpha ====================================")
	print("============================= Codename : Anaconda ====================================")
	print()
	print()
	print("Selamat datang di aplikasi bot ultra host")
	print("Silahkan memilih menu: ")
	print("[1] Auto Absen Ultra Host Untuk Server [without syncronus system]")
	print("[2] Auto Request Server [Bergantung Dengan Ketersediaan Server di Ultra Host]")
	print("[3] Auto Absen Ultra Host Untuk Server [with syncronus system]")
	print("[4] Exit")
	print("Note : Jika Ingin keluar dari program setelah memilih pilihan, gunakan Ctrl+c untuk keluar")
	try:
		if err == 1:
			print("Info: Error Terdeteksi, Silahkan Cek Programnya")
			err = 0
		#cek os dan perbaiki pilihannya
		#maake phantomjs portable for linux
		pilihan = int(input("Tentukan Pilihan Anda: "))
		if(pilihan == 1):
			pengguna = str(input("Masukkan Username Akun Ultra Host anda: "))
			psswd = str(input("Masukkan Password Akun Ultra Host anda: "))
			auto_login_ultra(pengguna,psswd,platform_os)
		elif(pilihan == 2):
			pengguna = str(input("Masukkan Username Akun Ultra Host anda: "))
			psswd = str(input("Masukkan Password Akun Ultra Host anda: "))
			auto_request_ultra(pengguna,psswd,platform_os)
		elif(pilihan == 3):
			pengguna = str(input("Masukkan Username Akun Ultra Host anda: "))
			psswd = str(input("Masukkan Password Akun Ultra Host anda: "))
			syncronus(pengguna,psswd,platform_os)
		elif(pilihan == 4):
			print("[INFO] Terima Kasih Telah Menggunakan Aplikasi Ini, Lapor Jika menemukan Bug")
			sys.exit(1)
			os.system('kill %d' % os.getpid())
	except Exception as e:
		err =1
		print("Terjadi Error Dalam Aplikasi, Menampilkan Pesan Error")
		print(e)
		main()

checking()
#syncronus()
#auto_request_ultra("senpai9","senpai9")
