
#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

class Component():

    # mttf is a Distribution, so is mttr
    # type is either 'np' or 'p' which means
    # either non-producing or producing
    def __init__(self, mttf, mttr, name='', comp_type='np'):
        self.name = name
        self.mttf = mttf
        self.mttr = mttr
        self.running = True
        self.runtime = 0
        self.repairtime = 0
        self.comp_type = comp_type
        self.next_failure = self.mttf.get_from_distribution()
        self.next_repair_time = self.mttr.get_from_distribution()
        self.total_runtime = 0
        self.total_repairtime = 0

    def switch_state(self):
        if self.running == True:
            self.running = False
        else:
            self.running = True

    def get_next_failure(self):
        return self.mttf.get_from_distribution

    def get_availability(self):
        return self.total_runtime/(self.total_runtime+self.total_repairtime)

class Distribution():

    # For normal distribution, var_a is mu and var_b is sigma
    # For gamma distribution, var_a is k and var_b is theta
    def __init__(self, var_a=0, var_b=1, dist_type='Normal'):
        self.dist_type = dist_type
        self.var_a = var_a
        self.var_b = var_b

    def create_plot(self, n=100000):
        if self.dist_type == 'Normal':
            x = self.var_a + self.var_b*np.random.randn(n)
        elif self.dist_type == 'Gamma':
            x = np.random.gamma(self.var_a, self.var_b, n)
        else:
            print('Please modify distribution type')
        # the histogram of the data
        n, bins, patches = plt.hist(x, 50, normed=1)
        plt.grid(True)
        plt.show()

    def get_from_distribution(self):
        if self.dist_type == 'Normal':
            x = self.var_a + self.var_b*np.random.randn()
            return x
        elif self.dist_type == 'Gamma':
            x = np.random.gamma(self.var_a, self.var_b)
            return x
        else:
            print('Please modify distribution type')