# -*- coding: utf-8 -*-

class EvaluatePhi(object):
    def __init__(self,eva_times_upperbound=2):
        self.history={}

    def get_p_and_t(self,activity,phi):
        return activity(phi)

    def sort_by_item(self,key,reverse=False,whole_history=True,dic={}):
        if whole_history:
            return sorted(self.history.iteritems(),key=lambda d:d[1][key],reverse=reverse)
        else:
            if dic is None:
                return []
            else:
                return sorted(dic.iteritems(),key=lambda d:d[1][key],reverse=reverse)

    def sort_sub_by_item(self,key,thresh,reverse=False,under=True):
        sub_dic = self.get_subDic(key=key,thresh=thresh,under=under)
        sort_list = self.sort_by_item(key=key,reverse=reverse,whole_history=False,dic=sub_dic)
        return sort_list

    def get_subDic(self,key,thresh,under=True):
        sub_dic={}
        for k_phi in self.history.keys():
            if under :
                if self.history[k_phi][key] <= thresh:
                    sub_dic[k_phi] = self.history[k_phi]
            else:
                if self.history[k_phi][key] >= thresh:
                    sub_dic[k_phi] = self.history[k_phi]
        return sub_dic

if __name__ == '__main__':
    print 'start'
    EV_phi = EvaluatePhi()
    print 'end'