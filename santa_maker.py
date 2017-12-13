"""Build naughty and nice lists for SC."""
from random import randrange

naughty_list = []
nice_list = []


def build_naughty_nice_lists():
    """."""
    for num in range(randrange(0, 100)):
        if num % 2 == 0: <----------- even naughty
            naughty_list.append(num)
        if num % 2 == 1: <----------- odd nice
            nice_list.append(num)
    return


def add_addresses(alist):
    """Put each item with address in a que."""
    for item in alist:
        if item % 2 == 0:
            naughty_list[item]='address from random generator of some sort'
        if item % 2 == 1:
            nice_list[item]='address from random generator of some sort'


def present_note_generator(alist):
    """Generates a note for kids and leaves present."""
    for item in alist:
        if key in alist == even:
            print('Coal for you. There\'s always next year. Cheer up!')
        if key in alist == odd:
            print('A pack of pokemon cards for you and an open invitation of an internship at Santa\'s workshop!')


def route_generator(alist):
    """SC combines the list for one big list of kids, with addresses, and what they get."""
    combined_list = naughtly_list.extend(nice_list)
    return combined_list


def shortest_path(combined_list):
    """djikestra perhaps."""
    visited = []
    path = []
