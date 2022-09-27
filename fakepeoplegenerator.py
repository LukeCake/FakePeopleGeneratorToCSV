# Random person ID generator / Generátor rč pro osoby narození od 1960 do 1999

import random
from _datetime import date
import csv
import string

def random_char(char_num):
     return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

def divisible_random(a,b,n):
    if b-a < n:
      raise Exception('{} is too big'.format(n))
    result = random.randint(a, b)
    while result % n != 0:
      result = random.randint(a, b)
    return result

def pick_random(list):
    route = "lists/" + list + ".txt"
    f.write(random.choice(open(route, "r", encoding="utf-8").read().splitlines()) + ";")


yearnow = date.today()
yearnowint = yearnow.year

#input
counter = 0
womancounter = 0
mencounter = 0
degreecounter = 0
outputs = int(input('Kolik rodných čísel chceš generovat?: '))

with open('FakePeople.csv', 'w', encoding='windows-1250') as f:

    while(counter < outputs):

            # get a random int in the range 6001010000 - 9930129999, the number is divisible by 11
            rc = divisible_random(1000000000,9999999999,11)

            #slice YY/MM/DD
            rcyear = str(rc)
            slice_year = slice(0, 2)
            rcyear = rcyear[slice_year]

            rcmonth = str(rc)
            slice_month = slice(2, 4)
            rcmonth = rcmonth[slice_month]
            rcday = str(rc)
            slice_day = slice(4, 6)
            rcday = rcday[slice_day]

            # chceck real date YY/MM/DD
            # RČ do roku 1953 byly za / 3 místná
            if 0 < int(rcyear) <21 or 53 < int(rcyear) < 99:
                if 0 < int(rcmonth) <= 12:
                    # řešíme jen dny 1 - 28 kvůli přestupnému roku
                    if 0 < int(rcday) <= 28:
                        # create rndm woman ID = MM + 50

                        rndmsexlist = [0, 50]
                        if (random.choice(rndmsexlist)) != 0:
                            # print("\nNÁHODNÁ Žena měním RČ z " + str(rc))
                            rc = rc + 50000000
                            # print("na " + str(rc))
                            # print("Podmínky OK, Zapisuji ŽENU do souboru - RČ: " + str(rc))
                            counter = counter + 1
                            womancounter = womancounter + 1

                            f.write(str(rc) + ";")

                            pick_random("czenamesfemale")
                            pick_random("czesurnamesfemale")

                            # if 22 <= (100 + int(yearnowint) - 2000 - int(rcyear)) <= 99:
                            #     probability = random.randint(1, 20)
                            #     if probability <= 1:
                            #         print("tento člověk získal při pravděpodobností 5% titul za jménem")
                            #         pick_random("titulzajmenem")
                            #     else:
                            #         f.write(";")
                            # else:
                            #     f.write(";")

                            if 24 <= (100 + int(yearnowint) - 2000 - int(rcyear)) <= 99:
                                probability = random.randint(1, 20)
                                if probability <= 3:
                                    # print("tento člověk získal při pravděpodobností 15% titul")
                                    pick_random("titulpredjmenem")
                                    degreecounter = degreecounter + 1
                                else:
                                    f.write(";")
                            else:
                                f.write(";")

                        else:
                            # print("\nPodmínky OK, Zapisuji MUŽE  do souboru - RČ: " + str(rc))
                            counter = counter + 1

                            f.write(str(rc) + ";")

                            pick_random("czenamesmale")
                            pick_random("czesurnamesmale")
                            mencounter = mencounter + 1

                            if 24 <= (100 + int(yearnowint) - 2000 - int(rcyear)) <= 99:
                                probability = random.randint(1, 20)
                                if probability <= 3:
                                    # print("tento člověk získal při pravděpodobností 15% titul")
                                    pick_random("titulpredjmenem")
                                    degreecounter = degreecounter + 1
                                else:
                                    f.write(";")
                            else:
                                f.write(";")

                            # if 22 <= (100 + int(yearnowint) - 2000 - int(rcyear)) <= 99:
                            #     probability = random.randint(1, 20)
                            #     if probability <= 1:
                            #         print("tento člověk získal při pravděpodobností 5% titul za jménem")
                            #         pick_random("titulzajmenem")
                            #     else:
                            #         f.write(";")
                            # else:
                            #     f.write(";")

                        pick_random("pojistovna")

                        #ulice
                        name = []
                        with open('lists/ulice/ulicetest.csv',newline='',  mode='r', encoding="utf-8") as file:
                            reader = csv.reader(file)
                            chosen_row = random.choice(list(reader))
                            # print(list(chosen_row))

                            listofadress = ""
                            for ele in chosen_row:
                                listofadress += ele
                            listofadress = (listofadress.split(";"))

                            #write
                            f.write(listofadress[1] + " ")
                            #rndm street number
                            f.write(str(random.randint(1, 40)) + ";")
                            f.write(listofadress[5] + ";")
                            f.write(listofadress[3] + ";")
                            f.write(str(random.randint(60200, 62800)) + ";")

                            #random email
                            f.write(random.choice(['CZ', 'SK']) + ";")

                            # random email
                            f.write(random_char(7) + "@gmail.com" + ";")

                            # random telephone
                            f.write(str(random.randint(720000000, 792000000)) + ";")




                        #enter za koncem řádku
                        f.write("\n")

f.close()

print("Celkem vygenerováno RČ: " + str(counter))
print("žen: " + str(womancounter) + " z " + str(outputs) + ", mužů: " + str(mencounter) + " z " + str(outputs) + ", osob s titulem: " + str(degreecounter) + " z " + str(outputs))
print("Zápis proběhl do soubru ./fakePeople.csv")