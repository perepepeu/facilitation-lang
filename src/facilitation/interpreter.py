from .lexer import Lexer, TokenType
from .parser import Parser, NodeType, ASTNode

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.scope_stack = []
    
    def error(self, message):
        raise Exception(f"Erro de execução: {message}")
    
    def interpret(self, code):
        try:
            # Lexical analysis
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            
            # Parsing
            parser = Parser(tokens)
            ast = parser.parse()
            
            # Execution
            return self.execute(ast)
        except Exception as e:
            print(f"Erro: {e}")
            return None
    
    def execute(self, node):
        if node.node_type == NodeType.PROGRAM:
            for child in node.children:
                self.execute(child)
        
        elif node.node_type == NodeType.ESCREVA:
            return self.execute_escreva(node)
        
        elif node.node_type == NodeType.ENTRADA:
            return self.execute_entrada(node)
        
        elif node.node_type == NodeType.VARIAVEL:
            return self.execute_variavel(node)
        
        elif node.node_type == NodeType.IF:
            return self.execute_if(node)
        
        elif node.node_type == NodeType.ASSIGNMENT:
            return self.execute_assignment(node)
        
        elif node.node_type == NodeType.BINARY_OP:
            return self.execute_binary_op(node)
        
        elif node.node_type == NodeType.IDENTIFIER:
            return self.get_variable(node.value)
        
        elif node.node_type == NodeType.LITERAL:
            return node.value
        
        elif node.node_type == NodeType.BLOCK:
            for child in node.children:
                self.execute(child)
        
        elif node.node_type == NodeType.REPEAT:
            return self.execute_repeat(node)
        
        return None
    
    def execute_escreva(self, node):
        if node.children:
            value = self.execute(node.children[0])
            if isinstance(value, str):
                print(value)
            else:
                print(str(value))
    
    def execute_entrada(self, node):
        tipo = "texto"  # padrão
        var_name = None
        prompt = ""
        
        for child in node.children:
            if child.node_type == NodeType.LITERAL:
                if child.value in ["texto", "quebrada", "numero"]:
                    tipo = child.value
                else:
                    prompt = child.value
            elif child.node_type == NodeType.IDENTIFIER:
                var_name = child.value
        
        if prompt:
            user_input = input(prompt)
        else:
            user_input = input()
        
        # Converter para o tipo apropriado
        if tipo == "numero":
            try:
                value = int(user_input)
            except ValueError:
                self.error(f"Não foi possível converter '{user_input}' para número inteiro")
        elif tipo == "quebrada":
            try:
                value = float(user_input)
            except ValueError:
                self.error(f"Não foi possível converter '{user_input}' para número decimal")
        else:  # texto
            value = user_input
        
        if var_name:
            self.variables[var_name] = value
        
        return value
    
    def execute_variavel(self, node):
        tipo = None
        var_name = None
        value = None
        
        for child in node.children:
            if child.node_type == NodeType.LITERAL:
                if child.value in ["bool", "texto", "quebrada", "numero"]:
                    tipo = child.value
                else:
                    value = child.value
            elif child.node_type == NodeType.IDENTIFIER:
                var_name = child.value
        
        if var_name:
            if value is not None:
                # Converter valor para o tipo apropriado
                if tipo == "numero":
                    value = int(value)
                elif tipo == "quebrada":
                    value = float(value)
                elif tipo == "bool":
                    value = bool(value)
                
                self.variables[var_name] = value
            else:
                # Inicializar com valor padrão
                if tipo == "numero":
                    self.variables[var_name] = 0
                elif tipo == "quebrada":
                    self.variables[var_name] = 0.0
                elif tipo == "bool":
                    self.variables[var_name] = False
                else:
                    self.variables[var_name] = ""
    
    def execute_if(self, node):
        if len(node.children) < 2:
            self.error("Estrutura 'se' inválida")
        
        condition = self.execute(node.children[0])
        if_block = node.children[1]
        
        if condition:
            self.execute(if_block)
        elif len(node.children) > 2 and node.children[2].node_type == NodeType.ELSE:
            else_block = node.children[2].children[0]
            self.execute(else_block)
    
    def execute_assignment(self, node):
        if len(node.children) != 2:
            self.error("Atribuição inválida")
        
        var_name = node.children[0].value
        value = self.execute(node.children[1])
        
        self.variables[var_name] = value
        return value
    
    def execute_binary_op(self, node):
        if len(node.children) != 2:
            self.error("Operação binária inválida")
        
        left = self.execute(node.children[0])
        right = self.execute(node.children[1])
        
        if node.value == "+":
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        elif node.value == "-":
            return left - right
        elif node.value == "*":
            return left * right
        elif node.value == "/":
            if right == 0:
                self.error("Divisão por zero!")
            return left / right
        elif node.value == "==":
            return left == right
        elif node.value == "for":
            return left == right
        
        self.error(f"Operador não suportado: {node.value}")
    
    def execute_repeat(self, node):
        if len(node.children) != 2:
            self.error("Estrutura 'repita' inválida")
        
        times = self.execute(node.children[0])
        block = node.children[1]
        
        for _ in range(times):
            self.execute(block)
    
    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        else:
            self.error(f"Variável '{name}' não definida")

def interpretar(codigo):
    interpreter = Interpreter()
    return interpreter.interpret(codigo) 