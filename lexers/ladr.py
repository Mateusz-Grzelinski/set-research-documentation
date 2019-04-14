from pygments.lexer import RegexLexer, words, bygroups
from pygments.token import *


class LadrLexer(RegexLexer):
    name = 'Ladr'
    aliases = ['ladr']
    filenames = ['*.in', '*.p']

    keywords = ('formulas', 'end_of_list', 'op', 'set', 'clear', 'redeclare')
    operators = r'=*\.'

    tokens = {
        'root': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'\{\*.*\*\}', Comment.Multiline),
            (operators, Operator),
            (words(keywords), Keyword),
        ]
    }

