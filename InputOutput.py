# -*- coding: utf-8 -*-
from easydict import EasyDict as edict
import yaml
import logging

class InputOutput(object):
    def __init__(self,yaml_filename):
        with open(yaml_filename, 'r') as f:
            cfg = edict(yaml.load(f))
        self.cfg = cfg
        self.phi_min = map(int, cfg.PHI_MIN[1:-1].split(','))
        self.phi_max = map(int, cfg.PHI_MAX[1:-1].split(','))
        assert len(self.phi_min) == len(self.phi_max)

        self.budget = cfg.BUDGET

    def get_config(self,filename):
        pass

    def get_phi_min(self):
        return map(int, self.cfg.PHI_MIN[1:-1].split(','))

    def get_phi_max(self):
        return map(int, self.cfg.PHI_MAX[1:-1].split(','))

    def save_output(self,out_dict,output_filename):
        with open(output_filename,'w') as f:
            yaml.dump(out_dict,f)

    def write_log(log_path='example.log', message='message'):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=log_path,
                            filemode='w')
        logging.info(message)

if __name__ == '__main__':
    GLB = InputOutput('faster_rcnn_end2end.yml')
    a={}
    a['TRE']= 'sad'
    a['Q'] = 1
    a['W'] = 234.9
    a['E'] = [2,3,4,5]
    a['R'] = {'1':23,'2':'sst','a':(1,2,3)}
    a['T'] = (1,2,3)
    GLB.save_output(a,'test')
    print 'end'