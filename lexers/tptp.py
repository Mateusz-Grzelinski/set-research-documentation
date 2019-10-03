from pygments.lexer import RegexLexer, words, bygroups
from pygments.token import *


class TptpLexer(RegexLexer):
    name = 'TPTP'
    aliases = ['tptp']
    filenames = ['*.p']

    keywords = ('cnf', 'fof', 'thf', 'axiom')
    operators = (r'!', r'\?', '~', '=>', '<=', '<=>')

    tokens = {
        'root': [
            (r'%.*\n', Comment.Single),
            # (r'\{\*.*\*\}', Comment.Multiline),
            # (r'\n', Text),
            # (r'\s+', Text),
            (words(operators), Operator),
            (words(keywords), Keyword),
        ]
    }

