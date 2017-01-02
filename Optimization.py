import logging
import copy

logging.basicConfig(level=logging.DEBUG)
logging.info('So should this')


class Optimization:

    def __init__(self, full_set, budget):
        self.full_set = full_set  # from phi_max
        self.growing_set = []
        self.rest_set = copy.deepcopy(full_set)
        self.budget = budget

    def run(self):
        

        # [p, t] = get_set_p_and_t(set)
        # deltaX = get_deltaX_minus()  get_deltaX_divide()
        # output: Su or Ss




if __name__ == '__main__':


