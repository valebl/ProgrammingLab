# LEZIONE 5 eserizio B

# creare una classe CSV file che ha come attributo il nome del file (name) e una funzione get_data() che salva ciascuna riga del file in una lista di due elementi e salva ciascuna sottolista in una lista più grande che poi verrà stampata in output
# Estendere la classe CSVFile e creare una funziona che converte a float i valori di tutte le colonne esclusa la prima, gestendo i possibili errori

class CSVFile(): # oggetto CSVFile

# funzione di inizializzazione in cui dichiaro l'attributo name, quindi il nome del file
    def __init__(self, name): 
        self.name = name

# funzione get_data()
    def get_data(self):
# creo la lista "grande" values
        values = []
# apro il file in modalità di sola lettura, gestendo il caso di un file non esistente
        try:
            my_file = open(self.name, 'r')
        except:
            print('Errore')       
# se il file è vuoto ritorno None
        if my_file == []:
            return None
# altrimenti opero su ogni riga del file
        for line in my_file:
# creo una nuova lista elements in cui salvo i valori di ciascuna linea, separandoli a livello della virgola, quindi elements[0] conterrà le date, elements[1] conterrà il numero di shampoo venduti
            elements = line.strip('\n').split(',')
# mi assicuro di scartare la prima linea del file in cui ho solo le intestazioni
            if elements[0] != 'Date':
# carico elementi sulla lista values 
                values.append(elements)
        return values

class NumericalCSVFile(CSVFile):
    def get_data(self):
        var = super().get_data()
# NON SO COME FARE: la mia idea è che per ciascuna sottolista elements della lista values, scarto ogni volta la prima colonna quindi elements[0] e poi provo a convertire a float le altre colonne elements[i] con i != 0. Però nella funzione estesa get_data_1, elements e values non sono definiti, quindi non so come operare su di loro. Inoltre, non so la dimensione delle sottoliste, cioè in pratica non so quante colonne ci sono
        for #ciascun elemento in values
            try:
               valore = float(#elements[i] con i!=0)
            except ValueError:
                print('Errore: non posso convertire a                  valore numerico')
                print('Ho avuto un errore di valore.                   "valore" valeva "{}"'.format(valore))
            except TypeError:
                print('Errore: Non posso convertire a                  valore numerico')
                print('Ho avuto un errore di tipo.                     "valore" valeva "{}"'.format(valore))

# ALTRO DUBBIO: per testare questo programma sul file shampoo sales direttamente da replit come si fa? Cioè come faccio ad eseguire le funzioni get_data e get_data_1 per il caso specifico del file shampoo sales?

file_name = "shampoo_sales.csv"
num_csv_file = NumericalCSVFile(file_name)
print(num_csv_file.get_data())