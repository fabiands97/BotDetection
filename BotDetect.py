import csv
import datetime as dt
from datetime import datetime

#mengimpor file .csv sebagai Input data awal
with open('deteksibot.csv','r') as readFile:
	reader = csv.reader(readFile)
	baris = list(reader)
	
	#iterasi tiap baris / username	
	for i in range(1, len(baris)):
		#mengecek isi biodata user
		bio=baris[i][3]
		if bio == "":
			baris[i][9] = 20
		else:
			baris[i][9] = 0


		#membandingkan lama bergabung dengan jumlah tweet
		bulan = "%d %b %Y"
		bu11 = datetime.now().strftime(bulan)
		bu1 = datetime.strptime(bu11,bulan)
		bu2 = dt.datetime.strptime(baris[i][4],bulan)
		bu = bu1-bu2
		x = bu.days
		if x >= 365:
			baris[i][10] = 40
		else:
			baris[i][10] = 0

		#membandingkan jumlah followers dan following
		fing = int(baris[i][7])
		fer = int(baris[i][8])
		fol = fing/fer
		if fol > 2 or fing == 1:
			baris[i][11] = 20
		else:
			baris[i][11] = 0

		#jumlah persentasi atau probabilitas Bot
		baris[i][12] = baris[i][9] + baris[i][10] + baris[i][11]
		print("Persentase Bot dari User @"+str(baris[i][2])+" adalah "+str(baris[i][12])+"%") 


#meletakkan hasil perhitungan atau output ke file yang sudah ada
with open('deteksibot.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(baris)

readFile.close()
writeFile.close()
