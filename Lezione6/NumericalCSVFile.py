class CSVFile():

    def __init__(self, name):
        if type(name) is not str:
            raise Exception("Initialize the CSVFile object with a string, not with a {} object.".format(type(name)))
        else:
            self.name = name

    def get_data(self, start=None, end=None):
        try:
            file = open(self.name)
        except:
            print(f'Errore: il file specificato "{self.name}" non esiste.')
            return

        file_lines = file.readlines()

        if len(file_lines) == 1:
            return []
            
        if start is None:
            start_clean = 2
        else:
            try:
                start_clean = int(start)
                # if start_clean % start != 0:
                # print("Warning - Start was numerical but not integrer: {} given but {} used.".format(start, start_clean))
            except Exception as e:
                print("Errore: {}".format(e))
                return None
                
        if end is None:
            end_clean = len(file_lines)
        else:
            try:    
                end_clean = int(end)
                # if end_clean % end != 0:
                # print("Warning - Start was numerical but not integrer: {} given but {} used.".format(end, end_clean))
            except Exception as e:
                print("Errore: Couldn't convert to integer: {}".format(e))
                return None

            #start_clean = 0

        try:
            if start_clean <= 0:
                raise Exception("start should be greater than 0.")
            elif start_clean > len(file_lines):
                raise Exception("start should be smaller than the file lenght.")
            elif end_clean > len(file_lines):
                raise Exception("end should be smaller than the file lenght.")
            elif end_clean <= start_clean:
                raise Exception("end should be strictly larger than start.") 
            else:
                start_clean -= 1
        except Exception as e:
            print("Errore: Couldn't convert to integer: {}".format(e))
            return None
            
        data = []
        print(start_clean, end_clean)
        for i, line in enumerate(file_lines):
            if i >= start_clean and i < end_clean:
                    l = line.strip().split(',')
                    #l = line.split('\n')[0]
                    #l = l.split(',')
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
file_name = 'shampoo_sales.csv'
# file_name = 'test.csv'
# file_name = 'empty.csv'

csv_file = CSVFile(file_name)
values = csv_file.get_data()
print(values)

# numerical_csv_file = NumericalCSVFile(file_name)
# values = numerical_csv_file.get_data(start=1.0, end=5)
# print(values)