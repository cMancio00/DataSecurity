# Esercizi di approfondimento
## Un crittogramma di Vigenere
Dato il sequente ciphertext:
```Python
ciphertext = \
"OKZARVGLNSLFOQRVVBPHHZAMOMEVHLBAITLZOWSXCSZFEQFICOOVDXCIISOOVXEIYWNHHLVQHSOWD"+\
"BRPTTZZOWJIYPJSAWQYNOYRDKBQKZPHHTLIHDEMICGYMSEVHKVXTQPBWMEWAZZKHLJMOVEVHJYSJR"+\
"ZTUMCVDGLZVBUIWOCPDZVEIGSOGZRGGOTAHLCSRSCXXAGPDYPSYMECRVPFHMYWZCYHKMCPVBPHYIF"+\
"WDZTGVIZEMONVYQYMCOOKDVQIMSOKLBUEBFZISWSTVFEWVIAWACCGHDRVVZOOBANRYHSSQBUIMSDW"+\
"VBNRXSSOGLVWKSCGHLNRYHSSQLVIYCFHVWJMOVEKRKBQMOOSVQAHDGLGWMEOMCYOXMEEIRTZBCFLZ"+\
"BVCVPRQVBLUHLGSBSEOUWHRYHSSEIEVDSCGHZRGOSOPBBUIQWNHRZFEIRPBWMEXCSPASBLXZFCWWW"+\
"EMZGLDDBUIOWNTHVPICOOTRZOMYRPBKMEIIHCOQKRWCSNFRAFIYWEKLBUSPHEVHAYMBVESVBGVZAZ"+\
"FVPRAJIWRQMIIMUZPDKXXJHSSRBUIMGTRHBUIMSHCXTQFZBZFHBHVIOYRWPRXCFPSRNGLZAVBHEVX"+\
"OVPMZMEIAIWZBIJEMSEVDBGLZMHSUMGVVWWWQOGLZCCPLARWYSNZLVRXCOEHKMLAZFPGLVXMIUHWW"+\
"PVXDBECWPRJDBLZQQTLOALFHBUIKOEVZWHPYPPRLNSMXIWHWPNXOCZHKMLOISH"
```
decifrare il testo tratto dalla lingua inglese utilizzando il metodo degli **indici di coincidenza**, eventualmente accoppiato con il metodo di **Kasiski**. Illustrare i vari passaggi in particolare:
1. ripetizioni nel testo, le loro distanze e i valori di $m$ (lunghezza della chiave) da esse suggerite;
2. i valori degli indici di coincidenza che si ottengono per il valore corretto di $m$;
3. per ciascuna delle $m$ lettere della chiave, indicare come  è stato individuato lo shift che dà il valore della chiave.

Per aiutarmi con la decrifrazione ho implementato i passaggi dell'attacco in Python.

Iniziamo l'attacco prendendo il `ciphertext` e dividendolo in tri-grammi con la funzione `split_text(ciphertext, m_gram_len)`. Ora che abbiamo una lista di tri-grammi dobbiamo individuare contare quali sono quelli che appaiono più di 2 volte nel testo. Uttilizzando la funzione `get_high_frequency_m_grams(m_grams)` otteniamo un dizionario con i tri-grammi frequenti.

Stampando il dizionario restituito dalla funzione otteniamo:
```
High frequency m_grams:
{'BUI': 4, 'HKM': 3}
```

Sappiamo quindi che i tri-grammi più frequenti sono **BUI** e **HKM**, con rispettivamente 4 e 3 ripetizioni.
Applichiamo il metodo di **Kasiski** per avere un canditato alla lunghezza della chiave $m$.
Dobbiamo quindi calcolare le distanze tra questi tri-grammi, in particolare dal primo tri-gramma con le sue ripetizioni.
Fatto ciò, calcoliamo il **MCD** tra queste distanze. Il risultato ci suggerirà l'ipotetica lunghezza della chiave.

Il problema descritto sopra è facilmente risolvibile con un **ciclo for** che in questo caso ha solo 2 iterazioni. Ad ogni iterazione dobbiamo calcolare le posizioni del tri-gramma all'interno della lista con `get_positions(m_grams, key)`,
calcolarci le distanze tra la prima occorreza con le altre, tramite la funzione `get_distances(positions, key)` ed infine eseguire il **MCD** tra queste distanze con `gcd.reduce(distances`.

Il codice finale è il seguente:
```Python
key_lenghts = list()
for key in high_frequency.keys():
    positions = get_positions(m_grams, key)
    distances = get_distances(positions, key)
    key_lenght = gcd.reduce(distances)
    key_lenghts.append(key_lenght)
print("Possible key lenghts:\n{key_lenghts}".format(key_lenghts=key_lenghts))
```
L'output è:
```
Element BUI positions:
[55, 143, 191, 239]
Elemt BUI distances:
[88, 136, 184]
Element HKM positions:
[73, 225, 249]
Elemt HKM distances:
[152, 176]
Possible key lenghts:
[8, 8]
```
In entrami i casi, questo metodo ci suggerisce una lunghezza della chiave pari a 8.

Ora che abbiamo un valore di $m$ possiamo calcolare gli indici di coincidenza.
Per farlo dobbiamo prima convertire il `ciphertext` in una matrice di dimensione $m*(n/m)$ dove n è la lungezza del `ciphertext` e utilizziamo la funzione `build_matrix(chypertext, m)` che è la seguente:
```Python
def build_matrix(text: str, m: int) -> np.ndarray:
    text = add_padding(text, m)
    matrix = np.array([sring_to_number(text[i:i+m]) for i in range(0,len(text),m)])
    return np.transpose(matrix)
```
Nel testo è stato aggiunto del padding per far tornare la divisione.
Per ogni riga della matrice (8) possiamo calcolare l'indice di coincidenza, calcolabile con la funzione `coincidence_index(row)`.
Ciclando su ogni riga della matrice otteniamo il seguente risultato:
```
Row 0: 0.064501679731243
Row 1: 0.07592385218365062
Row 2: 0.08085106382978725
Row 3: 0.05688689809630459
Row 4: 0.07928331466965287
Row 5: 0.07569988801791715
Row 6: 0.05867861142217245
Row 7: 0.0815229563269877
```
Questi numeri sono abbastanza vicini al valore atteso 0.065, quindi concludiamo che 8 è il valore corretto della chiave.

A questo punto possiamo determinare i singoli valori della chiave utilizzando la seguente formula:
$$M^g(y_i)=\sum_{j=0}^{25}{p_j}(\frac{f_{g+j}}{n/m})$$
Per ciascuma delle 8 righe delle matrice calcoliamo $M^g$.
```Python
key = list()
for row in cyphertext:
    max_list = list()
    for g in range(26):
        sum = 0
        for j in range(26):
            sum += p[j]*(frequency_vector(row)[(g+j)%26]/(len(row)/m))
        max_list.append(sum)
    key.append(max_list.index(max(max_list)))
print(key)
print(number_to_string(key))
```
Otteniamo quindi i massimi valori raggiunti per ogni carattere della chiave, che corrisponde alla lettera in numeri.

L'output è:
```
[21, 14, 11, 14, 3, 8, 13, 4]
VOLODINE
```
Possiamo ora decifrare il testo con `ciphertext[i]-key[i%m])%26`.
Il codice completo è:
```Python
ciphertext = np.transpose(cyphertext)
ciphertext = ciphertext.ravel()
decripted = list()
for i in range(len(ciphertext)):
    decripted.append((ciphertext[i]-key[i%m])%26)
print(number_to_string(decripted))
```
Che da come output il seguente testo:
```
TWOMONTHSEARLIERANETERNITYTHEDOWNFALLOFTHEORBISEHADHAPPENEDASPREDICTEDIMMEDIATELY
FOLLOWEDBYEXODUSANDACOMPLETELYEMPTYFUTURETHECITYCENTERSFLOWEDWITHTHEBLOODOFREPRIS
ALSTHEBARBARIANSHADRECLAIMEDPOWERJUSTLIKEEVERYWHEREELSEONTHEPLANETVASSILISSAMARAC
HVILIHADWANDEREDWITHAGROUPOFPARTISANSFORSEVERALDAYSANDTHENTHERESISTANCEHADDISPERS
EDANDTHENDIEDOUTSOWITHTWOCOMRADESINDISASTERKRONAUERANDILYUSHENKOSHEMANAGEDTOGETAR
OUNDTHEBARRIERSERECTEDBYTHEVICTORSANDENTERTHEEMPTYTERRITORIESAPATHETICFENCEHADFOR
BIDDENHERENTRANCESHECROSSEDITWITHOUTTHESLIGHTESTTREMORSHEWOULDNEVERGOBACKTOTHEOTH
ERSIDETHEREWOULDBENORETURNANDTHETHREEOFTHEMKNEWITTHEYWEREFULLYAWARETHATTHEYWERETR
AILINGTHEORBISESDECLINETHATTHEYWERESINKINGWITHITINTOTHEFINALNIGHTMARETHEPATHWOULD
BEDIFFICULTTHATTOOTHEYKNEWJUPKT
```
## Enigma
# Esercizi di programmazione
## Analisi delle frequenze di un testo
## Cifrario di Hill