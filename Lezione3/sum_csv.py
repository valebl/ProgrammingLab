def sum_csv(file_name):
    
    file = open(file_name, 'r')
    values = []
    
    for i, line in enumerate(file):
        if i > 0:
            elements = line.split(",")
            try:
                values.append(float(elements[1]))
            except:
                continue
    
    if len(values) > 0:
        sum_values = sum(values)
        file.close()
        return sum_values
    else:
        file.close()
        return None

# Comment the following lines to test the program with Autograding
if __name__ == "__main__":

    file_name = "shampoo_sales.csv"
    sum_sales = sum_csv(file_name)

    print(f"The total sales are {sum_sales:.2f}")