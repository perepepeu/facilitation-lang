"""
Facilitation Language - Uma linguagem de programação em português
"""

__version__ = "1.0.0"
__author__ = "Pedro"
__email__ = "pedrohenriquerios00@gmail.com"

from .lexer import Lexer, Token, TokenType
from .parser import Parser, ASTNode, NodeType
from .interpreter import Interpreter, interpretar

__all__ = [
    'Lexer', 'Token', 'TokenType',
    'Parser', 'ASTNode', 'NodeType', 
    'Interpreter', 'interpretar'
] 