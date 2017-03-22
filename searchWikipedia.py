import wikipedia as wik

def print_wiki_search(*args):
    try:
        result = wik.search(*args)
        print(result)
        return result
    except ValueError:
        print("args don't make sense")


def pretty_print(*args):
    for i in range(len(args)):
        print(args[i])


