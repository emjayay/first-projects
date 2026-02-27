import os

def cifra_messaggio(messaggio, chiave):
    risultato = ""
    for i in range(len(messaggio)):
        char = messaggio[i]
        key_char = chiave[i % len(chiave)]
        # Sommiamo i valori per ottenere il carattere cifrato
        nuovo_char = chr((ord(char) + ord(key_char)) % 1114112) 
        risultato += nuovo_char
    return risultato

print('--- LM MESSENGER PRO ---')
testo = input("Scrivi il messaggio: ")
chiave = input("Scegli la chiave segreta: ")

cifrato = cifra_messaggio(testo, chiave)

# Salva il file
with open("messaggio_cifrato.txt", "w", encoding="utf-8") as file:
    file.write(cifrato)

print("\n" + "="*50)
print("TESTO CIFRATO DA COPIARE:")
print("-" * 50)
print(cifrato)  # <--- Qui puoi selezionare il testo con il mouse e copiarlo
print("-" * 50)

print(f"\nFile salvato in: {os.path.abspath('messaggio_cifrato.txt')}")

# Comando per aprire automaticamente la cartella (Solo per Windows)
os.startfile(os.path.dirname(os.path.abspath("messaggio_cifrato.txt")))

print("="*50)
print("OPERAZIONE COMPLETATA: Cartella aperta e testo pronto!")