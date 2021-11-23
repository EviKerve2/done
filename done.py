from Funktsioonid import*
user=[Evi]
psword=[12345]

while True:
    print("Näita kõike-0, Reg-1,  ")
    v=int(input())
    if v==0:
        koik_kasu
    elif v==1:
        print("Registreerimine")
        while 1:
            log=input("Kasutajatunnus")








        elif v.upper()=="I":
            while 1:
                pas=input("Sisesta oma parool")
                tulemus=paskontroll(pas)
                if tulemus==True:
                    users.append(log)
                    password.append(pas)
                    break
    elif v==2:
        print("Avtoriseerimine")
        if passwords.index(pas)==users.index(user):
            print("Tere tulemast")

    elif v==3:
        print("Välja")