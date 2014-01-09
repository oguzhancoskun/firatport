__version__ = 0.1

import os
import re
import time
import psycopg2
import sys

con = None
cur = None
thisip = None
niclist = None
nic = None
thread = 0

def wtnick():
	#nicnames
	iname=os.popen("cat /proc/net/dev")
	p=iname.read()

	list=open("/tmp/fptmp/nicname","w")

	list.write(p)
	list.close()

	list=open("/tmp/fptmp/nicname","r")

	np=0
	global niclist
	niclist=[]

	print("-network interface names select:\n ")

	for i in list.readlines():
	
		x=re.search("(\w+):",i)
	
		if(x):
			print("  +%s select %s"%(x.group(1),np))
			niclist.insert(np,x.group(1))
			np+=1
	list.close()

	global nic
	nic=int(raw_input("\n>>> "))

def analyse():

	#nmap
	ports=os.popen("nmap 127.0.0.01")
	nmap=ports.read()

	openports=open("/tmp/fptmp/ports","w")

	openports.write(nmap)
	openports.close()

	openports=open("/tmp/fptmp/ports","r")

	sp=0

	global portlist
	portlist=[]

	#print("\n-your systems open ports list:")

	for i in openports.readlines():

		t=re.search("(\w+)/",i)

		if(t):
		        #print("%s select %s"%(t.group(1),sp))
		        portlist.insert(sp,t.group(1))
		        sp+=1

	openports.close()

	#pid=int(raw_input("\nselect : "))

def listen():
	#ngrep	
	#j acik portlarin sayisini verir. dongu icerisinde listeye atilan
	#portlarn tamami taranabilir.

	#for j in range(0,len(portlist),1):  normalde calismasi gereken                                  
		
	print("listening port 80")
	hr=os.popen("ngrep -O /tmp/fptmp/dns.dump -d %s port 80 -n 10"%(niclist[nic]))
	p=hr.read()
	print p
	getip=open("/tmp/fptmp/getlist","w")
	getip.write(p) 
	getip.close()

"""			
	#timecounter: belirli zaman araliklariyla dongu sagliyor.
		sec1=str(time.time())
		trm1=sec1[8:10]
		trm2=0
		while (int(trm2)-int(trm1))<5:
			sec2=str(time.time())
			trm2=sec2[8:10]
"""
			

def show():
	#show
	ngrepText=open("/tmp/fptmp/getlist","r")
	
	for i in ngrepText.readlines():

		ip=re.search("(\w+).(\w+).(\w+).(\w+):(\w+)\s->",i)

		if(ip):
			
			#eger bulunan ip kendisiyse yazmamali:
			##whatisyourip()
			
			if(thisip not in str(ip)):

				wrop=open("/tmp/fptmp/all","a")
				wrop.write("%s.%s.%s.%s:%s \n"%(ip.group(1),ip.group(2),ip.group(3),ip.group(4),ip.group(5)))
				wrop.close()
						
		del ip

	ngrepText.close()


## filter() tekrarli veriyi benzerlerinden ayiran bir metoddur. 
## ayni verilerin tekrar yazilmasini engeller.
def filterx():

	allip=open("/tmp/fptmp/all","r")

	for i in allip.readlines():
		
		cur.execute("INSERT INTO sunucular (ipa,ipb) VALUES (\'"+str(thisip)+"\',\'"+str(i)+"\')")

		easyf=open("/tmp/fptmp/base","r")
		if(i not in easyf and thisip not in i):
			finalf=open("/tmp/fptmp/base","a")
			finalf.write("%s"%i)
			#cur.execute("INSERT INTO servers (ipa,ipb) VALUES (\'"+str(thisip)+"\',\'"+str(i)+"\')")
			finalf.close()
			easyf.close()	
		
	allip.close()

#this function writed xml messages at 'dist/py/' directory in another file
def xmlWrite():
	xml=open("ips.xml","w")
	xml.write("<?xml version=\"1.0\"?>\n")

	con=psycopg2.connect("dbname='dbfport' host='localhost' user='fport' password='fportpass'")
	cur = con.cursor()
	cur.execute("""SELECT * FROM sunucular ORDER BY id DESC LIMIT 50""")
	rows = cur.fetchall()

	for row in rows:
		xml.write("<ngrep>\n")
		xml.write("\t<from>"+str(row[1])+"</from>\n")
		xml.write("\t<to>"+str(row[2])[:-1]+"</to>\n")
		xml.write("\t<date>"+str(row[3])+"</date>\n")
		xml.write("</ngrep>\n")
	xml.close()

#in this systems ip address
def whatisyourip():

	global thisip
	ss = os.popen("ifconfig | grep Bcast")
	t = ss.read()
	ip = re.search("addr:(\w+).(\w+).(\w+).(\w+)",t)
	thisip = "%s.%s.%s.%s"%(ip.group(1),ip.group(2),ip.group(3),ip.group(4))
	print "Your ip address is: ",thisip


#installing use app's in firatport project
def install_fport():

	print "installing ngrep.."
	setapp=os.popen("sudo apt-get install ngrep")
	ss=setapp.read()
	print ss
	print "installing nmap.."
	setapp=os.popen("sudo apt-get install nmap")
	ss=setapp.read()
	print ss
	print "installing tshark"
	setapp=os.popen("sudo apt-get install tshark")
	ss=setapp.read()
	print ss
	print "installing postgresql database connection.."
	setapp=os.popen("sudo apt-get install python-psycopg2")
	ss=setapp.read()
	print ss

#database connection module
def db_con():
	global cur
	global con
	con = psycopg2.connect("dbname='dbfport' user='fport' host='localhost' password='fportpass'")
	con.autocommit=True
	cur = con.cursor()

#create project main files
def create_info():

	os.popen("mkdir /tmp/fptmp")
	os.popen("touch /tmp/fptmp/base")
	os.popen("touch /tmp/fptmp/nicname")
	os.popen("touch /tmp/fptmp/all")
	os.popen("touch /tmp/fptmp/ports")
	os.popen("touch /tmp/fptmp/getlist")





if __name__ == "__main__":
		#wtnick network interface isimlerini tarayip listeler. ngrepi kullanabilmemiz
		# icin trafigin oldugu ag arayuzu secilmelidir.
		#wtnick 1 kere calismalidir. 
	
	##sistemin ip adresini ogrenip karsilastiracagiz:

	#if installing background tools please running install_fport() sub module
	#install_fport()
	db_con()
	#seek_attacks()

	#create basic control files
	choo=raw_input("do you want to create a project files?(y/n):")

	if(choo=='y'):
		create_info()
	#db connection 
	

	whatisyourip()
	wtnick()
	
	while(True):

		#analyse ve show sonsuz dongude kullanici parametre girmesi sartiyla kesilecek.
		analyse()
		#ngrep araci listen() de calisiyor.
		listen()
		show()
		filterx()
		xmlWrite()


