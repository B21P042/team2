# --- RaspberryPi main script --- #

import datetime
import dateutil.praser

# --- import functions --- #
from .functions import time_re as time # これどうやってやるん => できたわ

# -- main function -- #
def main():
    # object
    lect_dat = {}
    result = {}
    # read save file
    while True:
        idm, result['time'] = cardreader()
        result['attendance'] = time.my_time(result['time'], lect_dat['time'])
        result['inStudent'] = studentof(idm, lect_dat['students']['idms'])
        # comp(idm:str, students:[str], lect_time:{start:datetime,end:datetime,late:datetime})
        # monitor
        # datawrite()

# -- onexec -- #
if __name__ == '__main__':
    main()
