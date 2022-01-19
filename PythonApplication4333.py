from module1 import *
rus=[]
ang=[]
ang_list=loe_failist("ang.txt",ang)
rus_list=loe_failist("rus.txt",rus)

while True:
    m=input("На какоm языке разговаривать -H,\nВсе слова -A,\nПеревод-G,\nНовое слово-T,\nОшибка-N,\nКонтроль-K;\nЗакончить работу-L")
    if m.upper()=="G":
        pass
    if m.upper()=="T":
        rus_list=uus_sona("rus.txt",input("новое слово: "))
        ang_list=uus_sona("ang.txt",input("New word"))
    
    elif m.upper()=="N":
        keel1=input("Какой язык?")
        if keel1=="rus":
                rus_list=correction(input("Слово: "),rus_list)
                failisse(rus_list,"rus.txt")
        else:   
                ang_list=correction(input("Word: "),ang_list)
                failisse(ang_list,"ang.txt")
    elif m.upper()=="A":
         print(rus_list)
         print(ang_list)
    elif m.upper()=="H":
        keel=input("На каком языке разговаривать?")
        sonad=""
        if keel=="rus":
            mas=rus_list
            lang="ru"
    

    
    
    MODULE?????????????????????????????






def loe_failist(f:str,l:list):
    """
    Info failist f listisse l
    """
    fail=open(f,"r", encoding="utf-8-sig")# r -просмотр
    for rida in fail:
        l.append(rida.strip()) #'\n'
    fail.close()
    return l

def fail_saver(f:str,l:list):
    """
    loetelu salvaestame failisse 
    """
    fail=open(f,'w') ## w - перезапись
    for el in l:
        fail.write(el+'\n')
    fail.close


def rida_salvestamine(f:str,rida:str):
        """uks sona voi lause(rida) salvestamine failisse
        :param str f: fail kuku salvestame
        :param str rida: sona, mis vaja salvestada failisse
        """
        fail=open(f,'a')
        fail.write(rida+"\n")
        fail.close()
    
    
    
def uus_sona(f:str,rida:str)->list:
        """Lisame uus sona failisse ja listisse
        :param str file: Faili nimetus
        :param str x: lisatav sona
        """


def tolkimine(l1:list,l2:list):
    sona=input("Чего перевести")
    if sona in l1:
        tolk=12[l1.index(sona)]
        print(sona+"-"+tolk)
    else:
        print("Слово отсутствует в словаре")

def correction(sona:str,mas:list):
    for i in range(len(mas)):
        if mas[i]==sona:
            uus_sona=sona.replace(sona,input("New Word"))
            mas.insert(i,uus_sona)
            mas.remove(sona)
    return mas

def failisse(mas:list,file:str):
    f=open(file,'w',encoding="utf-8-sig")
    for sona in mas:
        f.write(sona+'\n')
    f.close()

    def viga(l1:list,f1:str,l2:list,f2:str):
        sona=input("Sona veaga")
        if sona not in l1 and sona not in l2:
            print("Слово отсутствует")
        else:
            if sona in l1:
                tolk=l2[l1.index(sona)]
                l1.remove(sona)
                l2.remove(tolk)
            elif sona in l2:
                tolk=l2[l2.index(sona)]
                l2.remove(sona)
                l1.remove(tolk)
            l1.append(input("Введи новое слово: "))
            l2.append(input("Type in new word: "))
            failisse_salvestamine(f1,l1)
            failisse_salvestamine(f2,l2)



import os
from gtts import gTTS

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")
