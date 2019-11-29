import sys
import traceback
from datetime import datetime
import dm_Channel
from random import uniform


class Utils:

    def errorHandlerStdscr(self, stdscr):
        try:
            traceback.print_exc(file=sys.stdout)
            txt = traceback.format_exc()
            tm = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            # print(txt)
            stdscr.addstr(35, 0, tm + ": " + txt)
            stdscr.refresh()
        except Exception as ex:
            print("errorHandler fout: ", ex)

    def errorHandler(self):
        try:
            txt = traceback.format_exc()
            traceback.print_exc(file=sys.stdout)
            print(txt)
        except Exception as ex:
            print("errorHandler fout: ", ex)
