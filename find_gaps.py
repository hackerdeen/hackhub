from hackhub import *
from member import *
from itertools import *
from datetime import date


def find_gaps(num_months):
    res  = {}
    for m in active_members():
        M = Member(m)
        t = date.today()
        months = ["%4d/%02d"%(p[0], p[1]) for p in
                  [(t.year+(t.month-i)/12, (t.month-i)%12+1) for i in xrange(2,num_months+2)]]
        payments = ["%4d/%02d"%(p[0], p[1]) for p in M.get_payments()]
        if len(payments) > 0:
            gaps = [month for month in months if (month not in payments
                                                  and month > payments[-1])]
            if len(gaps) > 0 and len(gaps) < num_months:
                res[m] = gaps
                print m, gaps
    return res

if __name__=="__main__":
    print find_gaps(6)


