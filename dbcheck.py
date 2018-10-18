import threading
import time
import backdbcheck
import sys



class dbcheckc(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Background thread initialized")
        lastchecktime = time.time()-86400
        try:
            while(True):
                if((time.time()-lastchecktime)>=86400):             #checking if a day had passed
                    lastchecktime=time.time()
                    backdbcheck.backdbcheck()

        except KeyboardInterrupt:
            sys.exit(0)
