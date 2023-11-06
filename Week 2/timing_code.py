import random
import time
from openpyxl import Workbook

test_list = []
for i in range(2500000, 5000000):
    test_list.append(random.randint(0, 100))

test_length = len(test_list)

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "List Size:"
sheet["B1"] = test_length

a = 3
b = 3

sheet[f"A{a}"] = "Process"
sheet[f"B{b}"] = "Time"

def l():
    test_list[-1]

def r():
    reversed(test_list)

def sh():
    random.shuffle(test_list)

def so():
    sorted(test_list)

def add_to_chart(process, result):
    global a
    global b
    a += 1
    b += 1
    sheet[f"A{a}"] = process
    sheet[f"B{b}"] = round(result, 4)

def timeTaken(function):
    ''' 
    Function is used to work out the cpu execution time
    -- st variable is the start time of the process
    the function is then run
    -- et is the end time that is then recorded
    and the result is the start time subtracted from the end time
    '''
    st = time.process_time()
    function()
    et = time.process_time()
    result = et - st
    print('CPU Execution time:', round(result, 4), 'seconds')
    add_to_chart('Last', result)

timeTaken(l)
timeTaken(r)
timeTaken(sh)
timeTaken(so)

workbook.save(filename="Results.xlsx")
