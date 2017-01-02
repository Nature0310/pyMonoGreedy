# -*- coding: utf-8 -*-
from InputOutput import InputOutput
import numpy as np


class EncoderDecoder(InputOutput):
    def __init__(self,yaml_filename):
        InputOutput.__init__(self,yaml_filename)
        self.phi_step = [1,] * len(self.phi_min)
        self.phi_max_offset = []
        self.delta_phi = []
        self.encoding_length = []
        self.setV = []

    def init_setting(self,method='linear'):
        if method == 'linear':
            self._linear_init()
        else:
            raise ValueError("no such method: '%s'. Please check your setting!"
                             "method should be one of the following strings:"
                             " 'linear', 'exponetial' ,'weights'" %
                             method)
    def decoding(self,set_coding,method='linear'):
        if method == 'linear':
            self._linear_decoding(set_coding)
        else:
            raise ValueError("no such method: '%s'. Please check your setting!"
                             "method should be one of the following strings:"
                             " 'linear', 'exponetial' ,'weights'" %
                             method)
    def encoding(self,phi,method='linear'):
        if method == 'linear':
            self._linear_encoding(phi)
        else:
            raise ValueError("no such method: '%s'. Please check your setting!"
                             "method should be one of the following strings:"
                             " 'linear', 'exponetial' ,'weights'" %
                             method)

    def _linear_init(self):
        assert len(self.phi_min) == len(self.phi_max)
        self.delta_phi = []
        self.phi_max_offset = []
        self.encoding_length = []
        for i in range(len(self.phi_min)):
            delta = self.phi_max[i] - self.phi_min[i]
            if delta >0:
                step = self.phi_step[i]
                n = np.ceil(delta * 1.0 / step)
            else:
                n = 0
            n = int(n)
            self.encoding_length.append(n)
            self.phi_max_offset.append(n * step - delta)
            self.delta_phi.append(max(n * step, 0))
        for i in range(len(self.phi_min)):
            for j in range(self.encoding_length[i]):
                e = {}
                e['index'] = i
                e['weights'] = self.phi_step[i]
                self.setV.append(e)

    def _linear_encoding(self,phi):
        phi_set = []
        assert len(phi) == len(phi)
        for i in range(len(phi)):
            delta = phi[i] - self.phi_min[i]
            assert delta >=0 and delta <= self.delta_phi[i]
            step = self.phi_step[i]
            n = delta / step
            for j in range(n):
                e = {}
                e['index'] = i
                e['weights'] = step
                phi_set.append(e)

        return phi_set


    def _linear_decoding(self,set_encoding):
        phi = [int(0),] * len(self.phi_min)
        for e in set_encoding:
            index = e['index']
            weights = e['weights']
            phi[index] += weights
        return phi

    def phi_to_name(self,phi):
        return '_'.join(map(str, phi))

    def name_to_phi(self,phi_name):
        return map(int, phi_name.split('_'))

if __name__ == '__main__':
    print 'start'
    ED_MODULE = EncoderDecoder('faster_rcnn_end2end.yml')
    ED_MODULE.init_setting(method='linear')
    print 'end'
