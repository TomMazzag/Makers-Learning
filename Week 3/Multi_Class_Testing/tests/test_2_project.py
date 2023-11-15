from lib.diary import *
from lib.contact_finder import *

def test_diary():

    my_diary = diary()
    day1 = my_diary.add_entry("Day One", "This is an example of a diary entry and this is what i did on day one ...")
    day2 = my_diary.add_entry("Day Two", "This is an example of a diary entry and this is what i did on day two ...")
    result = my_diary.read('Day One')
    assert result == "This is an example of a diary entry and this is what i did on day one ..."

def test_what_to_read():

    words_200 = "word " * 200
    words_400 = "word " * 400
    my_diary = diary()
    day1 = my_diary.add_entry("Day One", words_200)
    day2 = my_diary.add_entry("Day Two", "This is an example of a diary entry and this is what i did on day two ...")
    day3 = my_diary.add_entry("Day Three", words_400)
    result = my_diary.read_in_time(5, 40)
    assert result == ['Day One', 'Day Two']

def test_find_contacts():

    my_diary = diary()
    day1 = my_diary.add_entry("Day One", "This is an example of a diary entry and this is what i did on day one ...")
    day2 = my_diary.add_entry("Day Two", "This is an example of a diary entry 01234567891 and this is what i did on day two ...")
    contact = contacts(my_diary.entries)
    result = contact.findContacts()
    assert result == ['01234567891']
