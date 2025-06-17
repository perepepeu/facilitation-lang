import re
from enum import Enum

class TokenType(Enum):
    # Palavras-chave
    ESCREVA = "ESCREVA"
    ENTRADA = "ENTRADA"
    VARIAVEL = "VARIAVEL"
    SE = "SE"
    SENAO = "SENAO"
    FIM = "FIM"
    PARE = "PARE"
    REPITA = "REPITA"
    
    # Tipos
    TEXTO = "TEXTO"
    QUEBRADA = "QUEBRADA"
    NUMERO = "NUMERO"
    BOOL = "BOOL"
    
    # Valores
    STRING = "STRING"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    IDENTIFIER = "IDENTIFIER"
    
    # Operadores
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    ASSIGN = "ASSIGN"
    EQUALS = "EQUALS"
    FOR = "FOR"
    
    # Delimitadores
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    
    # Outros
    COMMENT = "COMMENT"
    NEWLINE = "NEWLINE"
    EOF = "EOF"

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column
    
    def __str__(self):
        return f"Token({self.type}, '{self.value}', linha={self.line}, coluna={self.column})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.current_char = self.text[0] if text else None
    
    def error(self, message):
        raise Exception(f"Erro léxico na linha {self.line}, coluna {self.column}: {message}")
    
    def advance(self):
        if self.current_char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    
    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()
    
    def skip_comment(self):
        if self.current_char == '#':
            while self.current_char and self.current_char != '\n':
                self.advance()
    
    def read_string(self):
        result = ""
        self.advance()  # Pular a primeira aspas
        
        while self.current_char and self.current_char != '"':
            result += self.current_char
            self.advance()
        
        if self.current_char == '"':
            self.advance()  # Pular a última aspas
            return result
        else:
            self.error("String não fechada")
    
    def read_number(self):
        result = ""
        is_float = False
        
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if is_float:
                    self.error("Número inválido: múltiplos pontos decimais")
                is_float = True
            result += self.current_char
            self.advance()
        
        if is_float:
            return Token(TokenType.FLOAT, float(result), self.line, self.column)
        else:
            return Token(TokenType.INTEGER, int(result), self.line, self.column)
    
    def read_identifier(self):
        result = ""
        
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        # Verificar se é uma palavra-chave
        keywords = {
            'escreva': TokenType.ESCREVA,
            'entrada': TokenType.ENTRADA,
            'variavel': TokenType.VARIAVEL,
            'se': TokenType.SE,
            'senão': TokenType.SENAO,
            'fim': TokenType.FIM,
            'pare': TokenType.PARE,
            'repita': TokenType.REPITA,
            'texto': TokenType.TEXTO,
            'quebrada': TokenType.QUEBRADA,
            'numero': TokenType.NUMERO,
            'bool': TokenType.BOOL,
            'verdadeiro': TokenType.BOOLEAN,
            'falso': TokenType.BOOLEAN,
            'true': TokenType.BOOLEAN,
            'false': TokenType.BOOLEAN,
            'for': TokenType.FOR
        }
        
        if result.lower() in keywords:
            token_type = keywords[result.lower()]
            value = result.lower()
            if token_type == TokenType.BOOLEAN:
                value = result.lower() in ['verdadeiro', 'true', '1']
            return Token(token_type, value, self.line, self.column)
        else:
            return Token(TokenType.IDENTIFIER, result, self.line, self.column)
    
    def get_next_token(self):
        while self.current_char:
            # Pular espaços em branco
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            # Pular comentários
            if self.current_char == '#':
                self.skip_comment()
                continue
            
            # Strings
            if self.current_char == '"':
                value = self.read_string()
                return Token(TokenType.STRING, value, self.line, self.column)
            
            # Números
            if self.current_char.isdigit():
                return self.read_number()
            
            # Identificadores e palavras-chave
            if self.current_char.isalpha() or self.current_char == '_':
                return self.read_identifier()
            
            # Operadores e delimitadores
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+', self.line, self.column)
            
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-', self.line, self.column)
            
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULTIPLY, '*', self.line, self.column)
            
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIVIDE, '/', self.line, self.column)
            
            if self.current_char == '=':
                self.advance()
                return Token(TokenType.ASSIGN, '=', self.line, self.column)
            
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(', self.line, self.column)
            
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')', self.line, self.column)
            
            if self.current_char == '{':
                self.advance()
                return Token(TokenType.LBRACE, '{', self.line, self.column)
            
            if self.current_char == '}':
                self.advance()
                return Token(TokenType.RBRACE, '}', self.line, self.column)
            
            self.error(f"Caractere inesperado: {self.current_char}")
        
        return Token(TokenType.EOF, None, self.line, self.column)
    
    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break
        return tokens
