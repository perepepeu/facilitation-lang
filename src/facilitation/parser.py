from enum import Enum

class NodeType(Enum):
    PROGRAM = "PROGRAM"
    ESCREVA = "ESCREVA"
    ENTRADA = "ENTRADA"
    VARIAVEL = "VARIAVEL"
    IF = "IF"
    ELSE = "ELSE"
    ASSIGNMENT = "ASSIGNMENT"
    BINARY_OP = "BINARY_OP"
    IDENTIFIER = "IDENTIFIER"
    LITERAL = "LITERAL"
    REPEAT = "REPEAT"
    BLOCK = "BLOCK"

class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type
        self.value = value
        self.children = children or []
    
    def add_child(self, child):
        self.children.append(child)
    
    def __str__(self, level=0):
        ret = "  " * level + f"{self.node_type.value}: {self.value}\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.current_token = tokens[0] if tokens else None
    
    def error(self, message):
        if self.current_token:
            raise Exception(f"Erro de sintaxe na linha {self.current_token.line}, coluna {self.current_token.column}: {message}")
        else:
            raise Exception(f"Erro de sintaxe: {message}")
    
    def advance(self):
        self.current += 1
        if self.current < len(self.tokens):
            self.current_token = self.tokens[self.current]
        else:
            self.current_token = None
    
    def peek(self, offset=1):
        peek_pos = self.current + offset
        if peek_pos < len(self.tokens):
            return self.tokens[peek_pos]
        return None
    
    def match(self, expected_type):
        if self.current_token and self.current_token.type == expected_type:
            token = self.current_token
            self.advance()
            return token
        else:
            expected = expected_type.value if hasattr(expected_type, 'value') else expected_type
            actual = self.current_token.type.value if self.current_token else "EOF"
            self.error(f"Esperado {expected}, encontrado {actual}")
    
    def parse(self):
        program = ASTNode(NodeType.PROGRAM, "program")
        
        while self.current_token and self.current_token.type.value != "EOF":
            statement = self.parse_statement()
            if statement:
                program.add_child(statement)
        
        return program
    
    def parse_statement(self):
        if not self.current_token:
            return None
        
        if self.current_token.type.value == "ESCREVA":
            return self.parse_escreva()
        elif self.current_token.type.value == "ENTRADA":
            return self.parse_entrada()
        elif self.current_token.type.value == "VARIAVEL":
            return self.parse_variavel()
        elif self.current_token.type.value == "SE":
            return self.parse_if()
        elif self.current_token.type.value == "REPITA":
            return self.parse_repeat()
        elif self.current_token.type.value == "IDENTIFIER":
            return self.parse_assignment()
        else:
            self.error(f"Declaração inesperada: {self.current_token.value}")
    
    def parse_escreva(self):
        node = ASTNode(NodeType.ESCREVA, "escreva")
        self.match(TokenType.ESCREVA)
        
        # Pode ser uma string literal ou uma expressão
        if self.current_token.type.value == "STRING":
            value = self.match(TokenType.STRING)
            node.add_child(ASTNode(NodeType.LITERAL, value.value))
        else:
            # Expressão (como variável + string)
            expr = self.parse_expression()
            node.add_child(expr)
        
        return node
    
    def parse_entrada(self):
        node = ASTNode(NodeType.ENTRADA, "entrada")
        self.match(TokenType.ENTRADA)
        
        # Tipo da entrada (opcional)
        if self.current_token.type.value in ["TEXTO", "QUEBRADA", "NUMERO"]:
            tipo = self.current_token
            self.advance()
            node.add_child(ASTNode(NodeType.LITERAL, tipo.value.lower()))
        
        # Nome da variável
        if self.current_token.type.value == "IDENTIFIER":
            var_name = self.match(TokenType.IDENTIFIER)
            node.add_child(ASTNode(NodeType.IDENTIFIER, var_name.value))
        
        # Prompt (opcional)
        if self.current_token.type.value == "STRING":
            prompt = self.match(TokenType.STRING)
            node.add_child(ASTNode(NodeType.LITERAL, prompt.value))
        
        return node
    
    def parse_variavel(self):
        node = ASTNode(NodeType.VARIAVEL, "variavel")
        self.match(TokenType.VARIAVEL)
        
        # Tipo da variável
        if self.current_token.type.value in ["BOOL", "TEXTO", "QUEBRADA", "NUMERO"]:
            tipo = self.current_token
            self.advance()
            node.add_child(ASTNode(NodeType.LITERAL, tipo.value.lower()))
        
        # Nome da variável
        if self.current_token.type.value == "IDENTIFIER":
            var_name = self.match(TokenType.IDENTIFIER)
            node.add_child(ASTNode(NodeType.IDENTIFIER, var_name.value))
        
        # Atribuição
        if self.current_token.type.value == "ASSIGN":
            self.match(TokenType.ASSIGN)
            value = self.parse_expression()
            node.add_child(value)
        
        return node
    
    def parse_if(self):
        node = ASTNode(NodeType.IF, "if")
        self.match(TokenType.SE)
        
        # Condição
        condition = self.parse_condition()
        node.add_child(condition)
        
        # Bloco do if
        if_block = self.parse_block()
        node.add_child(if_block)
        
        # Else (opcional)
        if self.current_token and self.current_token.type.value == "SENAO":
            self.match(TokenType.SENAO)
            else_block = self.parse_block()
            node.add_child(ASTNode(NodeType.ELSE, "else", [else_block]))
        
        return node
    
    def parse_condition(self):
        # Condição simples: identifier FOR value
        if self.current_token.type.value == "IDENTIFIER":
            left = ASTNode(NodeType.IDENTIFIER, self.current_token.value)
            self.advance()
            
            if self.current_token.type.value == "FOR":
                self.match(TokenType.FOR)
                
                # Pode ser == para comparação
                if self.current_token.type.value == "ASSIGN" and self.peek().type.value == "ASSIGN":
                    self.match(TokenType.ASSIGN)  # Primeiro =
                    self.match(TokenType.ASSIGN)  # Segundo =
                    right = self.parse_expression()
                    return ASTNode(NodeType.BINARY_OP, "==", [left, right])
                else:
                    right = self.parse_expression()
                    return ASTNode(NodeType.BINARY_OP, "for", [left, right])
        
        return self.parse_expression()
    
    def parse_repeat(self):
        node = ASTNode(NodeType.REPEAT, "repeat")
        self.match(TokenType.REPITA)
        
        # Número de repetições
        if self.current_token.type.value in ["INTEGER", "FLOAT"]:
            times = self.current_token
            self.advance()
            node.add_child(ASTNode(NodeType.LITERAL, times.value))
        
        # Bloco a ser repetido
        repeat_block = self.parse_block()
        node.add_child(repeat_block)
        
        return node
    
    def parse_assignment(self):
        # Nome da variável
        var_name = self.match(TokenType.IDENTIFIER)
        node = ASTNode(NodeType.ASSIGNMENT, "=")
        node.add_child(ASTNode(NodeType.IDENTIFIER, var_name.value))
        
        # Operador de atribuição
        if self.current_token.type.value == "ASSIGN":
            self.match(TokenType.ASSIGN)
        elif self.current_token.type.value == "FOR":
            self.match(TokenType.FOR)
            if self.current_token.type.value == "ASSIGN" and self.peek().type.value == "ASSIGN":
                self.match(TokenType.ASSIGN)
                self.match(TokenType.ASSIGN)
        
        # Valor
        value = self.parse_expression()
        node.add_child(value)
        
        return node
    
    def parse_expression(self):
        left = self.parse_term()
        
        while self.current_token and self.current_token.type.value in ["PLUS", "MINUS"]:
            op = self.current_token.value
            self.advance()
            right = self.parse_term()
            left = ASTNode(NodeType.BINARY_OP, op, [left, right])
        
        return left
    
    def parse_term(self):
        left = self.parse_factor()
        
        while self.current_token and self.current_token.type.value in ["MULTIPLY", "DIVIDE"]:
            op = self.current_token.value
            self.advance()
            right = self.parse_factor()
            left = ASTNode(NodeType.BINARY_OP, op, [left, right])
        
        return left
    
    def parse_factor(self):
        if self.current_token.type.value == "IDENTIFIER":
            value = self.match(TokenType.IDENTIFIER)
            return ASTNode(NodeType.IDENTIFIER, value.value)
        elif self.current_token.type.value in ["INTEGER", "FLOAT", "STRING", "BOOLEAN"]:
            value = self.current_token
            self.advance()
            return ASTNode(NodeType.LITERAL, value.value)
        else:
            self.error(f"Fator inesperado: {self.current_token.value}")
    
    def parse_block(self):
        block = ASTNode(NodeType.BLOCK, "block")
        
        # Se encontrar {, ler até }
        if self.current_token and self.current_token.type.value == "LBRACE":
            self.match(TokenType.LBRACE)
            while self.current_token and self.current_token.type.value != "RBRACE":
                statement = self.parse_statement()
                if statement:
                    block.add_child(statement)
            self.match(TokenType.RBRACE)
        else:
            # Bloco de uma linha
            statement = self.parse_statement()
            if statement:
                block.add_child(statement)
        
        return block 