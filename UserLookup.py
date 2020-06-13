import csv
import datetime as dt
import twint

time_format = "%H:%M:%S"

time1 = dt.datetime.strptime("02:00:00",time_format)
time2 = dt.datetime.strptime("04:00:00",time_format)

with open('keyword.csv','r') as readFile:
	reader = csv.reader(readFile)
	baris = list(reader)
	#mengecek waktu tweet dilakukan untuk dibandingkan terhadap aturan
	for i in range(1, len(baris)):
		a = dt.datetime.strptime(baris[i][1],time_format)
		b = baris[i][2]
		if a > time1 and a < time2:
			#mengambil informasi username twitter
			c = twint.Config()
			c.Username = b
			c.User_full = True
			c.Store_csv = True
			c.Output = "deteksibot.csv"
			twint.run.Lookup(c)
