# # Apro e Leggo il file, Linea per Linea

# my_file = open('shampoo_sales.csv','r')  
my_file = open('../Lezione4/empty_file.csv')

def sum_csv(file_nella_funzione):

#creo chart list da usare nell'if
    chart_list=["Date","Sales"]
    # somma=0 #sommare la lista con la funzione append 
    somma = []

    for line in file_nella_funzione:
        # Faccio lo split di ogni riga sulla virgola
        elements = line.split(',') #elements: una lista che contine 2 elementi (1 linea del file)
        
        # Se NON sto processando L'intestazione...
        if elements[0] != 'Date':                                 
            # somma+= float(elements[1]) #float() funzione che trasforma in float 
            somma.append(float(elements[1]))
    return sum(somma)

somma=sum_csv(my_file)
print("Risultato:{}" .format(somma))