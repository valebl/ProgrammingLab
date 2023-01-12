class MovingAverage():

    def __init__(self, finestra):     
        if finestra is None:
            raise ExamException("Errore: la lunghezza finestra è None.")
        if type(finestra) is not int:
            raise ExamException("Errre: la lunghezza finestra deve essere un intero.")
        if finestra <= 0:
            raise ExamException("Errore: la lunghezza finestra deve essere maggiore di zero.")
        else:
            self.finestra = finestra        

    def compute(self, serie):
        # conrolli sull'input
        if type(serie) is not list:
            raise ExamException(f'Errore: l\'input di compute deve essere una lista e non {type(serie)}.')
        elif len(serie) == 0:
            raise ExamException(f'Errore: lista valori vuota.')
        elif len(serie) < self.finestra:
            raise ExamException("Errore: lunghezza lista minore della lunghezza finestra.")
        else:
            for valore in serie:
                if type(valore) is str and valore.isnumeric() is False:
                    raise ExamException(f"Errore: la lista contiene il valore non numerico {valore}.")
                    
        # calcolo media mobile
        lista_medie = []
        for i in range(len(serie)-self.finestra+1):
            valori_da_mediare = serie[i:i+self.finestra]
            media = sum(valori_da_mediare) / len(valori_da_mediare)
            lista_medie.append(media)
        return lista_medie

class ExamException(Exception):
    pass

# moving_average = MovingAverage(3)
# # result = moving_average.compute([2,4,8,16])
# result = moving_average.compute([1,2])
# print(result)