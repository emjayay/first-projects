import os

def nascondi_messaggio(nome_immagine, messaggio_segreto):
    marker = b"---BEGIN HIDDEN MESSAGE---"
    
    with open(nome_immagine, 'ab') as f:
        f.write(marker + messaggio_segreto.encode('utf-8'))

print("--- STEGANO-WRITER ---")
img = input('Inserisci il nome del file immagine (es. foto.jpg): ')
msg = input('Inserisci il messaggio segreto da nascondere: ')

try:
    if os.path.exists(img):
        nascondi_messaggio(img, msg)
        print(f"\nOperazione completata!")
        print(f"Messaggio nascosto con successo in: {img}")
    else:
        print(f"Errore: Il file '{img}' non esiste nella cartella corrente.")

except Exception as e:
    print(f"Si è verificato un errore imprevisto: {e}")