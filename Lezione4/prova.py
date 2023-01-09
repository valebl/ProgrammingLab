class CSVFile():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        elements = []
        my_file = open(self.name, 'r')
        for line in my_file:
            if line != 'Date,Sales\n':
                elements.append(line.split(','))
        my_file.close()
        return elements

# csv_file = CSVFile("../Lezione3/shampoo_sales.csv")
# print(csv_file.get_data())