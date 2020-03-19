import csv
import wget

save_path = 'C:\\Users\\bulzg\\Desktop\\img\\'
cont = 0
ext = '.jpg'

with open('goh.csv') as csv_f:
    csv_read = csv.reader(csv_f)

    next(csv_read)

    for i in csv_read:
        link = i[2]
        try:
            wget.download(link, out=save_path+str(cont)+ext)
            cont = cont+1
        except :
            pass
        