# Skrastiņš Kristaps PD1

"""
Algoritma loģikai iesākumā tika izmantots masīvs "test",
kurš saturēja failā "ints_10.txt" esošās vērtības.

Par failu nolasīšanu uztraukšos vēlāk
"""

test = [
        56,
        53,
        74,
        59,
        11,
        41,
        47,
        46,
        57,
        41
        ]

maxRange = 0                                # mainīgais, kas saglabās maksimālo iespējamo intervālu
for i in range(0, len(test)):
    for j in range(i+1, len(test)):         # iterēju cauri visiem skaitļiem, no kuriem būs jāatņem skaitlis test[i] no iepriekšējā cikla  
        currentRange = test[j] - test[i]
        if currentRange > maxRange:         # pārbaudu, vai patreizējās iterācijas starpība ir lielāka par patreizējo lielāko starpību
            mazinamais = test[i]
            mazinatajs = test[j]            # ja jā, tad piefiksēju skaitļus, starp kuriem ir šī starpība
            maxRange = currentRange         # un atjauninu lielāko starpību
            
print(f"lielākais intervāls ir {maxRange} starp skaitļiem {mazinamais} un {mazinatajs}")