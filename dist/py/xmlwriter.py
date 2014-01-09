import psycopg2

def xmlWrite():
	xml=open("ips.xml","w")
	xml.write("<?xml version=\"1.0\"?>")

	con=psycopg2.connect("dbname='dbfport' host='localhost' user='fport' password='fportpass'")
	cur = conn.cursor()
	cur.execute("""SELECT * FROM sunucular ORDER BY id DESC LIMIT 50""")
	rows = cur.fetchall()

	for row in rows:
		xml.write("<ngrep>")
		xml.write("<from>row[1]</from>")
		xml.write("<to>row[2]</to>")
		xml.write("<date>row[3]</date>")
		xml.write("</ngrep>")
	xml.close()
