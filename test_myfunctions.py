# test_myfunctions.py
#

import hpcutil
from hpcutil import myfunctions

def test_init():
    myfunctions.initialize("testeventlog", "testperflog", 1)
    
def test_loginfo():
    myfunctions.loginfo("test_loginfo", "test_msg")

def test_logperf():
    myfunctions.logperf("hpcutil.logperf", "particle_picking_per_tomo", "6000", "seconds" )

def test_close():
    myfunctions.close()

# run the suite of tests
test_init()
test_loginfo()
test_logperf()
test_close()


     
