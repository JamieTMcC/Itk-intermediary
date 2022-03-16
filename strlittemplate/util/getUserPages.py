import os
import sys
import inspect
# used to get the userpages directory above the mainApp.py file so that mainApp.py can be included
# in strlittemplate

# KetZoomer -
# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
currentdir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)

import userPages
print("success importing userPages")
