# myfunctions.py
# 
# library of global helper functions for hpc pipeline
# functionality includes:
#   initializing library
#   logging events (info, errors)
#   logging performance data
#   closing library

from datetime import datetime

#
# initialize()
#
# open eventlog for writing in append mode.  The file is created if it doesn't exist.
# event log format - [date time of event][calling module] msg
# CONSIDER some variation of http format if more is needed:
#     [date time of message][module and severity level][pid][tid][client ip] message string
# 
# open perflog for writing in append mode.  
# output format - datetime,module,metric,measure,unit  (comma deliminated for easy parsing)
#
# CONSIDER - log files can be replace by http or sql servers for scaling out to multiple clients or environments
#
# input: 
# eventlog - the path to the eventlog file
# perflog - the path to the perflog file
# logging level - 0 == write to file;  1 == write to file and console
# 
# return:
# none
#
def initialize(eventlog, perflog, level):   
    global g_eventlog
    global g_perflog
    global g_level
    global g_datetime_format

    g_datetime_format = "%m/%d/%Y, %H:%M:%S"
    g_level = level

    # initialize eventlog
    try:
        g_eventlog = open(eventlog, "a")
    except:
        if g_level:
            print("file open failed for eventlog = " + eventlog)
    else:
        now = datetime.now()
        date_time = now.strftime(g_datetime_format)
        message = "[" + date_time + "] [hpcutil.initialize] Intialized eventlog"
        try: 
            g_eventlog.write(message + "\n")
        except:
            if g_level:
                print("file write failed to eventlog")
        else:
            if g_level:
                print(message)

     # initialize perflog
    try:
        g_perflog = open(perflog, "a")
    except:
        if g_level:
            print("file open failed for perflog = " + perflog)
    else:
        now = datetime.now()
        date_time = now.strftime(g_datetime_format)
        message = "[" + date_time + "] [hpcutil.initialize] Intialized perflog"
        try: 
            g_eventlog.write(message + "\n")
        except:
            if g_level:
                print("file write into perflog failed")
        else:
            if g_level:
                print(message)           

#                  
# loginfo()
# append info to eventlog
# format - [date time of message][module] msg
#           
def loginfo(module, msg):
    now = datetime.now()
    date_time = now.strftime(g_datetime_format)
    message = "[" + date_time + "] [" + module + "] " + msg
    g_eventlog.write(message + "\n")
    if g_level:
        print(message)

#                  
# logperf()
# append info to perflog
# format - datetime,calling_module,metric,measure,unit 
#           
def logperf(module, metric, measure, unit):
    now = datetime.now()
    date_time = now.strftime(g_datetime_format)
    message = date_time + "," + module + "," + metric + "," + measure + "," + unit
    g_eventlog.write(message + "\n")
    if g_level:
        print(message)

#
# close() - closes the eventlog and perflog
#
def close() -> None:
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    message = "[" + date_time + "] [" +  "hpcutil.close" + "] " + "log files closed"
    g_eventlog.write(message + "\n")
    g_eventlog.close()
    g_perflog.close()
    if g_level:
        print(message)

# test code for above functions - 
# use test_myfunctions.py after rebuilding library
# initialize ("", "testperflog", 1)
# initialize ("testeventlog", "", 1)
# initialize("testeventlog", "testperflog", 1)
# loginfo("hpcutil.loginfo", "test msg")
# logperf("hpcutil.logperf", "particle_picking_per_tomo", "6000", "seconds" )
# close()

