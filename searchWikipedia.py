import wikipedia as wik
import argparse


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


def get_parser():
    parser = argparse.ArgumentParser(
        description='search Wikipedia in command line'
    )
    parser.add_argument('query', metavar='QUERY',
                        type=str,
                        nargs='*',
                        help='The words you want to search Wikipedia'
                        )
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if not args['query']:
        parser.print_help()
        return

    else:
        print_wiki_search(args['query'])


if __name__=='__main__':
    command_line_runner()
