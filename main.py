# Skrastiņš Kristaps PD1

"""
Algoritma loģikai iesākumā tika izmantots masīvs "test",
kurš saturēja failā "ints_10.txt" esošās vērtības.

Par failu nolasīšanu uztraukšos vēlāk
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
        print("Nepareiza ievade!")
    

    

maxRange = 0                                # mainīgais, kas saglabās maksimālo iespējamo intervālu
for i in range(0, len(ints)):
    for j in range(i+1, len(ints)):         # iterēju cauri visiem skaitļiem, no kuriem būs jāatņem skaitlis test[i] no iepriekšējā cikla  
        currentRange = ints[j] - ints[i]
        if currentRange > maxRange:         # pārbaudu, vai patreizējās iterācijas starpība ir lielāka par patreizējo lielāko starpību
            mazinamais = ints[i]
            mazinatajs = ints[j]            # ja jā, tad piefiksēju skaitļus, starp kuriem ir šī starpība
            maxRange = currentRange         # un atjauninu lielāko starpību
            
print(f"lielākais intervāls ir {maxRange} starp skaitļiem {mazinamais} un {mazinatajs}")