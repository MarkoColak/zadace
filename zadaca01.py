import random

def randomOcjena():
    return random.randint(1, 5)

lista =['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa',
         'Marko', 'Dario', 'Mihael',
         'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon',
         'Ivan', 'Ante', 'Ivan',
         'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip',
         'Tomislav', 'Luka', 'Ivan',
         'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka',
         'Ana', 'Emanuel',
         'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante',
         'Marijan', 'Mario',
         'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas',
         'Ivan', 'Freda', 'Kristina',
         'Josip', 'Lucija']

ocjene ={}

for ime in lista:
    ocjene[ime] = randomOcjena()

brojOcjena = {}
pozitivneOcjene = 0

for student in ocjene:
    print("student: Ocjena: " , (student, ocjene[student]))

    ocjena = ocjene[student]
    if ocjena > 1:
        pozitivneOcjene +=1
    if ocjena in brojOcjena:
        brojOcjena[ocjena] += 1
    else:
        brojOcjena[ocjena] = 1

for ocjena in brojOcjena:
    print("ocjena %d se pojavljuje %d puta" %(ocjena, brojOcjena[ocjena]))

print("Pozitivne ocjene: %d" %(pozitivneOcjene))
print("Prolaznost : %d%%" % ((pozitivneOcjene / len(ocjene))* 100))






        
