__version__ = 0.1

import os
import re
import time

def wtnick():
	#nicnames
	iname=os.popen("cat /proc/net/dev")
	p=iname.read()

	list=open("nicname.txt","w")

	list.write(p)
	list.close()

	list=open("nicname.txt","r")

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

	openports=open("ports.txt","w")

	openports.write(nmap)
	openports.close()

	openports=open("ports.txt","r")

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
	hr=os.popen("ngrep -O dns.dump -d %s port 80 -n 10"%(niclist[nic]))
	p=hr.read()
	print p
	getip=open("getlist.txt","w")
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
	ngrepText=open("getlist.txt","r")
	
	for i in ngrepText.readlines():

		ip=re.search("(\w+).(\w+).(\w+).(\w+):(\w+)\s->",i)

		if(ip):
			
			#eger bulunan ip kendisiyse yazmamali:
			##whatisyourip()
			
			if(thisip not in str(ip)):

				wrop=open("all.txt","a")
				wrop.write("%s.%s.%s.%s:%s \n"%(ip.group(1),ip.group(2),ip.group(3),ip.group(4),ip.group(5)))
				wrop.close()
						
		del ip

	ngrepText.close()


## filter() tekrarli veriyi benzerlerinden ayiran bir metoddur. 
## ayni verilerin tekrar yazilmasini engeller.
def filterx():

	allip=open("all.txt","r")

	for i in allip.readlines():
		easyf=open("easy.txt","r")
		if(i not in easyf and thisip not in i):
			finalf=open("easy.txt","a")
			finalf.write("%s"%i)
			finalf.close()
			easyf.close()

	allip.close()



def whatisyourip():

	global thisip
	thisip=raw_input("this systems ip address => ")



if __name__ == "__main__":
		#wtnick network interface isimlerini tarayip listeler. ngrepi kullanabilmemiz
		# icin trafigin oldugu ag arayuzu secilmelidir.
		#wtnick 1 kere calismalidir. 
	
	##sistemin ip adresini ogrenip karsilastiracagiz:

	whatisyourip()

	wtnick()
	while(True):
		#analyse ve show sonsuz dongude kullanici parametre girmesi sartiyla kesilecek.
		analyse()

		#ngrep araci listen() de calisiyor.
		listen()
		show()
		filterx()

		

