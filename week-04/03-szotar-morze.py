
#elemkettes kista
morzekódok = [
    ('A', '.-'),
    ('B', '-...'),
    ('C', '-.-.'),
    ('D', '-..'),
    ('E', '.'),
    ('F', '..-.'),
    ('G', '--.'),
    ('H', '....'),
    ('I', '..'),
    ('J', '.---'),
    ('K', '-.-'),
    ('L', '.-..'),
    ('M', '--'),
    ('N', '-.'),
    ('O', '---'),
    ('P', '.--.'),
    ('Q', '--.-'),
    ('R', '.-.'),
    ('S', '...'),
    ('T', '-'),
    ('U', '..-'),
    ('V', '...-'),
    ('W', '.--'),
    ('X', '-..-'),
    ('Y', '-.--'),
    ('Z', '--..'),
    ('0', '-----'),
    ('1', '.----'),
    ('2', '..---'),
    ('3', '...--'),
    ('4', '....-'),
    ('5', '.....'),
    ('6', '-....'),
    ('7', '--...'),
    ('8', '---..'),
    ('9', '----.'),
]

karakter_morze_atalakito = dict(morzekódok)
morze_karakter_atalakito = {morzekód[1]: morzekód[0] for morzekód in morzekódok} #megcseréli a karaktert a morzekóddal.

def morze_kodol(szoveg):
    kodolt_szoveg = ''
    for karakter in szoveg:
        kodolt_szoveg += karakter_morze_atalakito[karakter] + ' ' 
    return kodolt_szoveg.strip() #a string elejéről és végéről leszedi a szóközöket.

def morze_dekodol(kodolt):
    eredmeny = ''
    for kod in kodolt.split(): #a szoközöknél darabolja fel a sztringet
        eredmeny += morze_karakter_atalakito[kod]
    return eredmeny

kodolt = morze_kodol('HELLOVILAG')
print(kodolt)
dekodolt = morze_dekodol(kodolt)
print(dekodolt)
