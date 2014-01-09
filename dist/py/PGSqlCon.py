import psycopg2
def pgcon():
	try:
    	con=psycopg2.connect("dbname='dbfport' user='fport' password='fportpass'")
    	cur = con.cursor()
	except:
    	print "Parametre hatasi!"

def dbwrite(ipa, ipb):
	query = "INSERT INTO sunucular (ipa, ipb) VALUES ('"+str(ipa)+"','"+str(ipb)+"')"
	cur.execute(query)