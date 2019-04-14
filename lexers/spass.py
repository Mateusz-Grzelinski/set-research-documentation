from _ast import keyword

from pygments.lexer import RegexLexer, words, bygroups
from pygments.token import *


class SpassLexer(RegexLexer):
    name = 'SPASS'
    aliases = ['spass']
    filenames = ['*.in']

    keywords1 = ('begin_problem', 'end_problem', 'list_of_descriptions', 'list_of_symbols', 'list_of_formulae', 'end_of_list')
    keywords2 = ('author', 'name', 'version', 'logic', 'status', 'description', 'date', 'formula', 'functions', 'predicates', 'cnf', 'dnf')
    keywords3 = ('satisfiable', 'unsatisfiable', 'unknown', 'identifie', 'axioms', 'conjectures')
    word_operators = ('forall', 'or', 'not', 'and', 'implies', 'equiv', 'equal', 'true', 'false', 'exists')

    tokens = {
        'root': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'\{\*.*\*\}', Comment.Multiline),
            (words(word_operators, suffix=r'\b'), Name.Builtin),
            (words(keywords1), Keyword),
            (words(keywords2, suffix=r'\b'), Keyword.Pseudo),
            (words(keywords3, suffix=r'\b'), Keyword.Constant),
        ]
    }
