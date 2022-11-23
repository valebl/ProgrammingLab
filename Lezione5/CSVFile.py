class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            file = open(self.name)
        except:
            print(f"Errore: il file specificato {self.name} non esiste.")
            return
        list_of_lists = []
        for i, line in enumerate(file):
            if i > 0:
                #l = line.strip().split(',')
                l = line.split('\n')[0]
                l = l.split(',')
                list_of_lists.append(l)
        file.close()
        return list_of_lists

# Comment the following lines to test the program with Autograding
# if __name__ == '__main__':

#     file_name = '../Lezione3/shampoo_sales.csv'
#     file_name = 'empty_file.csv'
#     csv_file = CSVFile(file_name)

#     values = csv_file.get_data()
#     print(values)