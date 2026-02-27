def estrai_messaggio(nome_immagine):
    marker = b"---BEGIN HIDDEN MESSAGE---"

    try:
        with open(nome_immagine, 'rb') as f:
            data = f.read()

        start_index = data.find(marker)

        if start_index == -1:
            return "Nessun messaggio nascosto trovato."
        
        messaggio_index = start_index + len(marker)
        messaggio_byte = data[messaggio_index:]
        
        return messaggio_byte.decode('utf-8')

    except FileNotFoundError:
        return "File non trovato."
    except Exception as e:
        return f"Errore durante l'estrazione: {e}"

print("--- STEGANO DECODER ---")
file_da_leggere = input("Inserisci il nome del file immagine (es. foto.jpg): ")
risultato = estrai_messaggio(file_da_leggere)

print("\n" + "="*30)
print(f"Messaggio nascosto: {risultato}")
print("="*30)