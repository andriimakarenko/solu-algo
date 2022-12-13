# Just figuring out how do I make a match-case statement
# that will match to an int var in the case.

longest_str_len = 5
string = 'd'
match len(string):
    case _ as length if length == longest_str_len:
        print('lol')
    case _ as length if length == 0:
        print('kek')
    case _:
        print('Jack The Sparrow? No, Captain Jack The Sparrow!')