
import wikipedia as wik
import argparse


def get_wiki_search(*args):
    try:
        result = wik.search(*args)
        # print result
        return result
    except ValueError:
        print "args don't make sense"


def get_summary(*args):
    try:
        result =  wik.summary(*args)
        return result
    except ValueError:
        print "args don't make sense"


def pretty_print(*args):
    print '\n'
    for i in range(len(args)):
        print args[i]
    print '\n'


def get_parser():
    parser = argparse.ArgumentParser(
        description='search Wikipedia in command line'
    )
    parser.add_argument('query', metavar='QUERY',
                        type=str,
                        nargs='*',
                        help='The words you want to search Wikipedia returns\
                        simmular topics'
    )
    parser.add_argument('-s', '--summary',
                        action='store_true',
                        default=False,
                        dest='get_summary',
                        help='Print the summary of your query'
    )
    return parser


def get_page(*args):
    request = wik.page(*args)
    title = request.title
    content = request.content
    output = '\n' \
        + title + '\n' \
        + content + '\n'
    return content


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if not args['query']:
        parser.print_help()
        return
    if args['get_summary']:
        print get_summary(args['query'])
        return
    else:
        pretty_print(*get_wiki_search(args['query']))


if __name__=='__main__':
    command_line_runner()
