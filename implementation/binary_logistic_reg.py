__author__ = 'Jorge Cotillo'

import entity.training_set_entity as _tse
import helpers.helpers as _helpers
import interfaces.i_logistic_regression as interface
import numpy.core as np


class BinaryLogisticRegression(interface.ILogisticRegression):

    _alpha = 1.0

    def __init__(self, alpha=None):
        if alpha is not None:
            _alpha = alpha

    def predict(self):
        training_set_list = self.retrieve_training_set()
        cost = self.get_cost(training_set_list)
        return 1

    def retrieve_training_set(self):
        x_input_variables = ['x0', 'wind_speed_mph']
        training_set_list = _helpers.Helpers.get_binary_training_data_from_csv(self,
                                                                               'data/binary_training_set.csv',
                                                                               x_input_variables,
                                                                               'binary')
        return training_set_list

    def get_cost(self, training_set_list):
        cost = 0.0
        for i in range(len(training_set_list)):
            training_set = training_set_list[i]
            cost += self.__get_cost_intern(training_set.get_x, training_set.get_y)
        # final cost equation -1/m sum(cost)
        return -(1.0 / len(training_set_list)) * cost

    def __get_cost_intern(self, x, y):
        # -y * log(h(x)) - (1-y) * log(1-h(x))
        # since x is an array (n + 1) features, loop as many times as needed
        x_cost = 0.0
        for i in range(len(x)):
            x_cost += -y * np.log(self.set_hypothesis(x[i])) - (1-y) * np.log(1 - self.set_hypothesis(x[i]))
        return x_cost

    def set_hypothesis(self, param1):
        return self.__sigmoid_function(param1)

    @staticmethod
    def __set_hypothesis_intern(self, param1, param2, param3):
        return 3.0

    def get_gradient_descent(self):
        return self.get_gradient_descent_intern(1, 2, 3)

    @staticmethod
    def __get_gradient_descent_intern(self, param1, param2, param3):
        return 5.0

    def __sigmoid_function(self, x):
        return 1.0 / (1.0 + np.exp(-x))
