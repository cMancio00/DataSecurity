# Relazione set 2
## Common modulus failure
Un utente A possiede due coppie di chiavi pubbliche-private RSA, relative allo stesso modulo
n dato da
$$n = 825500608838866132701444300844117841826444264266030066831623$$
Le due chiavi pubbliche sono $K_1^+ = ⟨3, n⟩$ e $K_2^+ = ⟨11, n⟩$. Un secondo utente invia ad A, in
tempi diversi, lo stesso messaggio m, cifrato prima con la chiave K1 e poi con la chiave K2 .
Un attaccante intercetta i relativi plaintext, $c_1 = E_{K_1^+} [m]$ e $c_2 = E_{K_2^+}[m]$, che numericamente
valgono
$$c_1 = 41545998005971238876458051627852835754086854813200489396433$$
$$c_2 = 88414116534670744329474491095339301121066308755769402836577$$
Ricavare m a partire dalle informazioni disponibili, senza fattorizzare n o ricavare gli esponenti
privati.

### Soluzione

Sapendo che $c_1 = m^{e_1} \mod{n}$ e $c_2 = m^{e_2} \mod{n}$ posso moltiplicarli tra di loro ottenendo:
$$c_1 * c_2 = m^{e_1}*m^{e_2} = m^{e_1 + e_2} \mod{n}$$
Se $e_1 + e_2 = 1$ allora ho trovato $m$.

Se $MCD(e_1,e_2)=1$, cioè se $e_1$ e $e_2$ sono coprimi, Posso esprimere $xe_1 + ye_2 = 1$.

Il problema precedente diventerà:
$$c_1^x * c_2^y = (m^{e_1})^x*(m^{e_2})^y = m^{xe_1 + ye_2} = m^1 = m \mod{n}$$

Effettivamente $3$ e $5$ sono coprimi e posso trovare $x$ e $y$ tramite l'algoritmo di Euclide esteso:
$$
\begin{align*}
    11 &= 3*3 +2\\
    3 &= 1+2 + 1
\end{align*}
$$
$$1=3-1+2=3-1*(11-3)=-1*11+4+3$$
La $x$ è negativa, ma sapendo che $-1 \equiv 11^{-1} \mod 3$, posso scrivere $-1 + 3 = 2$, quindi ho:
$$
\begin{align*}
    x &= 2\\
    y &= 4
\end{align*}
$$

Sostituendo i valori si ottiene: $c_1^4 * c_2^2$ (sono stati invertiti i valori per rispettare i relativi inversi).

Effettuando i calcoli otteniamo:
$$
\begin{align*}
&41545998005971238876458051627852835754086854813200489396433^4 \\ 
&* 88414116534670744329474491095339301121066308755769402836577^2 \\ 
& \mod 825500608838866132701444300844117841826444264266030066831623 \\
&= 564140501104607297831987135512845214089854084977820388226740
\end{align*}$$
