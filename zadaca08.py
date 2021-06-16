def dobrodosao(ime):
    print("dobrodosao",ime)

pozdrav = (lambda ime:("pozdrav"+ime))

def dobrodoslica(funkcija):
    return funkcija("ja")
print(dobrodoslica(dobrodosao))
