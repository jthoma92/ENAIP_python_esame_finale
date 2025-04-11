import json

def leggi_da_file(filepath):
    """Questa funzione legge dati JSON da un file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def elabora_dati_json1(dati):
    return len(dati)

def elabora_dati_json2(dati):
  
    residenti_Roma = [persona["nome"] for persona in dati if persona.get("citta") == "Roma"]
    return residenti_Roma

def elabora_dati_json3(dati):
    eta_persone = []
    for persona in dati:
        try:
            eta_num = float(persona.get("eta"))
            eta_persone.append(eta_num)
        except:
           pass
    return sum(eta_persone) / len(eta_persone)
      
        
       

    
            


    
# """
#     ISTRUZIONI:
#     Questa funzione prende una lista di dizionari (letto da un file JSON)
#     e dovrebbe eseguire alcune operazioni sui dati, gestendo anche eventuali
#     voci non valide o incomplete.

#     Da fare in questa funzione:

#     TODO 1. Stampa il numero totale di voci (dizionari) presenti nei dati.
    
#     TODO 2. Crea una nuova lista contenente solo i nomi delle persone che vivono a Roma.
#        Gestisci il caso in cui la chiave 'citta' potrebbe non essere presente.
    
#     TODO 3. Calcola l'età media di tutte le persone valide nei dati. Considera valide
#        solo le voci che hanno una chiave 'eta' con un valore numerico intero.
#        Ignora le voci con 'eta' mancante, non numerica o null.
#     TODO 4. Stampa un messaggio che elenca i nomi trovati nel dizionario con dati non validi 
#        o mancanti 

#     Parametri:
#     - dati: Una lista di dizionari, dove ogni dizionario rappresenta una persona
#              con (idealmente) le chiavi 'nome', 'eta' e 'citta'.

#     Restituisce:
#     - None (la funzione stampa direttamente i risultati).
# """

if __name__ == "__main__":
    # Codice per provare la funzione "elabora_dati_json"
    dizionario = leggi_da_file("dati/test.json")
    print(elabora_dati_json1(dizionario))
    print(elabora_dati_json2(dizionario))
    print(elabora_dati_json3(dizionario))
    

