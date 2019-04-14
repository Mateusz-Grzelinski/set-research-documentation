from pygments.lexer import RegexLexer, words, bygroups
from pygments.token import *


class TomlLexer(RegexLexer):
    name = 'Toml'
    aliases = ['toml']
    filenames = ['*.toml']

    tokens = {
        'root': [
            (r'^\s*\[\[[\w\.]+\]\]\s*\n', Keyword),
            (r'^\s*\[[\w\.]+\]\s*\n', Keyword),
            (r'#.*\n', Comment.Single),
            (r'(.*)(=)', bygroups(Name.Variable, Operator)),
            (r'[]{}:(),;[]', Punctuation),
            (r'(")(.*?)(")', bygroups(String.Double, String, String.Double)),
            (r'true|false', Keyword.Constant),
            # (words('true', 'false', suffix=r'\b'), Keyword.Constant),
            # (r'.*', Text)
        ],
        'builtins': [
        ]
    }

