import os

def decifra_messaggio(testo, chiave):
    risultato = ""
    for i in range(len(testo)):
        char = testo[i]
        key_char = chiave[i % len(chiave)]
        # Sottraiamo i valori numerici per tornare all'originale
        originale = chr((ord(char) - ord(key_char)) % 1114112)
        risultato += originale
    return risultato

print("--- RICEVITORE PRONTO ---")

if os.path.exists("messaggio_cifrato.txt"):
    with open("messaggio_cifrato.txt", "r", encoding="utf-8") as file:
        messaggio_da_file = file.read()
    
    print(f"File trovato! Contenuto cifrato: {messaggio_da_file}")
    chiave = input("Inserisci la chiave di decifratura: ")
    
    testo_chiaro = decifra_messaggio(messaggio_da_file, chiave)
    print(f"\nMessaggio Decifrato: {testo_chiaro}")
else:
    print("Nessun file 'messaggio_cifrato.txt' trovato.")