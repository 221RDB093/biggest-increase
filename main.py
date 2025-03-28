# Skrastiņš Kristaps PD1

"""
Sākotnējā algoritma "brute force" versija bija visai neefektīva,
jo tajā algoritms iterēja caur visiem skaitļiem vairākas reizes,
savstarpēji salīdzinot katru skaitli ar visiem iespējamajiem 
skaitļiem, kas atrodas tam "priekšā".

Jaunais optimizētais algoritms nodrošina to, ka katrs skaitlis ciklā
tiek apskatīts tikai vienu reizi.
"""

ints = [] # saraksts, kurā glabāsies teksta faila vērtības

while True:
    try:
        print("Sveiki! Jums jāievada ierakstu skaits failam, kuru vēlaties pārmeklēt!")
        print("Iespējamās ievades iespējas ir: 10, 100, 1K, 10K, 100K, 1M, 10M")
        file = input("Ievadiet savu izvēli: ")      # pieprasu lietotājam ievadīt ierakstu daudzumu, kas jāapstrādā 
        f = open(f"pd1_data/ints_{file}.txt", "r")  # nolasu attiecīgo failu
        
        for line in f:                              
            ints.append(int(line))                  # katra iterācija (jeb rinda) tiek parsēta uz int tipu un pievienota sarakstam
            
        break
    except FileNotFoundError:                       # izņēmums gadījumam, ja lietotāja ievade ir nederīga
        print("Pārbaudiet ievadi un to, vai fails atrodas tam paredzētajā vietā! (~/pd1_data/ints_[...].txt)")


def biggest_increase(arr):
    startValue = arr[0]  # Pieņemu, ka pirmais elements ir mazākais
    maxRange = 0
    for i in range(1, len(arr)):  # Iterēju caur masīva indeksiem (atskaitot nulto)
        num = arr[i] # num = patreizējā (šīs iterācijas) masīva elementa vērtība
        
        if num - startValue > maxRange: # ja starpība ir starp patreizējo un sākuma skaitli ir lielāka par maksimālo, tad 
            maxRange = num - startValue # turpmāk tā tiks uzskatīta par maksimālo
        if num < startValue: # ja patreizējais skaitlis ir mazāks par sākumskaitli, tad turpmāk šis skaitlis tiks uzskatīts par mazāko
            startValue = num
    return maxRange



print(biggest_increase(ints))