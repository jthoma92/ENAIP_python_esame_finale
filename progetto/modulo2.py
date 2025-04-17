import json

def leggi_da_file(filepath):
    """Questa funzione legge dati JSON da un file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(e)
        return None

def elabora_dati_json(dati):
    """
    ISTRUZIONI:
    Questa funzione prende una lista di dizionari (letto da un file JSON)
    e dovrebbe eseguire alcune operazioni sui dati, gestendo anche eventuali
    voci non valide o incomplete.

    Da fare in questa funzione:

    TODO 1. Stampa il numero totale di voci (dizionari) presenti nei dati.
    TODO 2. Crea una nuova lista contenente solo i nomi delle persone che vivono a Roma.
       Gestisci il caso in cui la chiave 'citta' potrebbe non essere presente.
    TODO 3. Calcola l'età media di tutte le persone valide nei dati. Considera valide
       solo le voci che hanno una chiave 'eta' con un valore numerico intero.
       Ignora le voci con 'eta' mancante, non numerica o null.
    TODO 4. Stampa un messaggio che elenca i nomi trovati nel dizionario con dati non validi 
       o mancanti 

    Parametri:
    - dati: Una lista di dizionari, dove ogni dizionario rappresenta una persona
             con (idealmente) le chiavi 'nome', 'eta' e 'citta'.

    Restituisce:
    - None (la funzione stampa direttamente i risultati).
    """
    print(f"\nVoci totali presenti nel dizionario: {len(dati)}\n")

    lista_roma = []

    for persona in dati:
        if "citta" in persona:
            if persona["citta"].lower() == "roma":
                lista_roma.append(persona["nome"])

    print(f"Le persone che vivono a Roma:")
    for persona in lista_roma:
        print(persona)
    
    eta = 0
    count = 0

    for persona in dati:
        if "eta" in persona:
            if type(persona["eta"]) == int:
                eta += persona["eta"]
                count += 1

    print(f"\nL'età media è: {eta/count:.2f}\n") 

    lista_sbagliati = []
    lista_criteri = ["eta", "nome", "citta", "SBAGLIATO"] #definizione dei criteri di una persona per il seguente Ciclo for (include anche la nuova chiave "SBAGLIATO")

    #Questo Ciclo For controlla ogni dizionario del file JSON Per errori, aggiungendo una chiave ai eventuali dizonario problematici
    #La chiave si chiama "SBAGLIATO" e contiene una lista descrittiva del problema (o dei problemi), e viene aggiunta all'invizio
    for persona in dati:
        if len(persona) > 0:  #ignorare dizionari vuoti
            persona["SBAGLIATO"] = []

            #Controllare tutte le chiave presenti per la persona: Se non sono nel gruppo lista_criteri, segna un errore nella lista "SBAGLIATO"
            for chiave in persona:  
                if chiave not in lista_criteri:
                    persona["SBAGLIATO"].append(f'Dati non definiti presenti: "{chiave}" non consentito')

            #Controllare per persone senza criteri e tipi sbagliati dei criteri
            if "eta" not in persona:
                persona["SBAGLIATO"].append('Manca "eta"')
            elif type(persona["eta"]) != int:
                persona["SBAGLIATO"].append('tipo del dato sbagliato: eta')

            if "nome" not in persona:
                persona["SBAGLIATO"].append('Manca "nome"')
            elif type(persona["nome"]) != str:
                persona["SBAGLIATO"].append('tipo del dato sbagliato: nome')

            if "citta" not in persona:
                persona["SBAGLIATO"].append('Manca "citta"')
            elif type(persona["citta"]) != str:
                persona["SBAGLIATO"].append('tipo del dato sbagliato: citta')

            #Finalmente raccogliere tutte le persone con dati problematici
            if len(persona["SBAGLIATO"]) > 0:
                lista_sbagliati.append(persona)

    #Stampa dei problemi, se ci sono:
    if len(lista_sbagliati) > 0:
        print(f"{len(lista_sbagliati)} problemi trovati: queste persone hanno i seguenti problemi:")
        for persona in lista_sbagliati:
            print(persona)
    else: 
        print("NESSUN PROBLEMA CON DATI")

        
if __name__ == "__main__":
    # Codice per provare la funzione "elabora_dati_json"
    elabora_dati_json(leggi_da_file("../dati/test.json"))

