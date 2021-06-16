from csv import reader
with open('rezultati.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    rezultati = list(map(tuple, csv_reader))
    rezultati.sort()

rezultati_sortirani_po_prezimenu=[]
for ime, prezime, bodovi in rezultati:
    rezultati_sortirani_po_prezimenu.append(prezime,)
print("Ovo su rezultati sortirani po prezimenu;", "\n", rezultati_sortirani_po_prezimenu)


bodovi_na_ispitima=[]
for ime,prezime,bodovi in rezultati:
    bodovi_na_ispitima.append(bodovi)

rjecnik={}
nedovoljan=0
dovoljan=0
dobar=0
vrlo_dobar=0
odlican=0
for i in bodovi_na_ispitima:
    rjecnik[i]=bodovi_na_ispitima
    if int(i)>= 0 and int(i)<=49:
        nedovoljan+=1
    if int(i)>=50 and int(i)<=64:
        dovoljan+=1
    if int(i)>=65 and int(i)<80:
        dobar+=1
    if int(i)>=80 and int(i)<=89:
        vrlo_dobar+=1
    if int(i)>90:
        odlican+=1
    
print("Studenata sa ocjenom 1 ima:", nedovoljan)
print("Studenata sa ocjenom 2 ima:", dovoljan)
print("Studenata sa ocjenom 3 ima:", dobar)
print("Studenata sa ocjenom 4 ima:", vrlo_dobar)
print("Studenata sa ocjenom 5 ima:",odlican)

exit=input("unesite broj za izlaz:")





