class Model():

    def fit(self, data):
        raise NotImplementedError("Metodo non implementato.")

    def predict(self, data):
        raise NotImplementedError("Metodo non implementato.")


class IncrementModel(Model):

    def predict(self, data):
        if type(data) is not list:
            raise TypeError
        if len(data) > 1:
            sum_increments = 0
        else:
            raise Exception
        for i, item in enumerate(data):
            if i > 0:
                sum_increments += item - data[i-1]
        mean_increment = sum_increments / (len(data)-1)
        prediction = data[-1] + mean_increment
        return prediction

values = [50, 52, 40]
# values = {'1': 1}
increment_model = IncrementModel()
print(increment_model.predict(values))