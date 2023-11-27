from lib.reminder import *

def test_reminder():
    reminder = Reminder("Tom")
    reminder.remind_me_to("Finish this excersise")
    test = reminder.remind()
    assert test == "Finish this excersise, Tom!"