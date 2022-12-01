import tempfile
import datetime
from dateutil.relativedelta import relativedelta

class CSVFile():

    def __init__(self, name):
        if type(name) is not str:
            raise Exception("Initialize the CSVFile object with a string, not with a {} object.".format(type(name)))
        else:
            self.name = name

    def get_data(self, start=None, end=None):
        try:
            file = open(self.name)
        except Exception:
            print(f'Errore: il file specificato "{self.name}" non esiste.')
            return

        file_lines = file.readlines()

        # Controllo che il file non sia vuoto (o che non contenga solo l'intestazione)
        if len(file_lines) <= 1:
            return []

        # Controllo che start sia convertibile in int
        if start is None:
            start_clean = 2
        else:
            start_clean = int(start)
            #try:
            #    start_clean = int(start)
            #except:
            #    raise Exception("Errore: {}".format(e))

        # Controllo che end sia convertibile in int
        if end is None:
            end_clean = len(file_lines)
        else:
            end_clean = int(end)
            # try:    
            #     end_clean = int(end)
            # except:
            #     raise Exception ("Errore: Couldn't convert to integer: {}".format(e))

        # Ora start e end sono due interi, ma servono altri controlli
        if start_clean <= 0:
            raise Exception("start should be greater than 0.")
        elif start_clean > len(file_lines):
            raise Exception("start should be smaller than the file lenght.")
        elif end_clean > len(file_lines):
            raise Exception("end should be smaller than the file lenght.")
        elif end_clean < start_clean:
            raise Exception("end should be larger than start.") 
        else:
            start_clean -= 1
        # except Exception as e:
        #     print("Errore: {}".format(e))
        #     return None
            
        data = []
        #print(start_clean, end_clean)
        for i, line in enumerate(file_lines):
            if i >= start_clean and i < end_clean:
                    l = line.strip().split(',')
                    data.append(l)
        file.close()
        return data

class NumericalCSVFile(CSVFile):

    def __init__(self, name):
        super().__init__(name)
    
    def get_data(self, *args, **kwargs):
        numerical_data = super().get_data(*args, **kwargs)
        for values in numerical_data:
            for i, value in enumerate(values):
                if i > 0:
                    try:
                        values[i] = float(value)
                    except Exception as e:
                        print(f'Errore: {e}.')
        return numerical_data


# Comment the following lines to test the program with Autograding
# # file_name = 'shampoo_sales.csv'
# file_name = 'test.csv'
# # file_name = 'empty.csv'
# # file_name = 'tmp_file.csv'

# csv_file = CSVFile(file_name)
# values = csv_file.get_data(start=0)
# print(values)
# # print(len(values))

# numerical_csv_file = NumericalCSVFile(file_name)
# values = numerical_csv_file.get_data(start=1.0, end=5)
# print(values)

# with open("test_2.csv", 'w') as file:

#     file.write('Date,Sales\n') # 1
#     file.write('1949-01,1\n')  # 2
#     file.write('1949-02,2\n')  # 3
#     file.write('1949-03,3\n')  # 4
#     file.write('1949-04,4\n')  # 5
#     file.write('1949-05,5\n')  # 6
#     file.write('1949-06,6\n')  # 7