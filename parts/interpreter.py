import json
from utilities.token import *
from utilities.logger import Logger
from parts.default_functions import Builtins

class Interpreter:
    def __init__(self, ast) -> None:
        self.interpret(ast)
    
    # setup globals and main func
    def interpret(self, ast):
        self.ast = ast
        self.scopes = []

        self.scopes.append({})

        # setup global scope
        for t in self.ast:
            if isinstance(t, ast_func):
                self.scopes[0][t.name.value] = (t.perams, t.body)
            elif isinstance(t, Token):
                if t.type == "EOF":
                    break
        
        # check for entry
        if self.scopes[0].get("main", False):
            exitcode = self.execFunc(self.scopes[0].get("main"), [])
            Logger.info(f"Exited with status code {exitcode}")
        else:
            Logger.err("Missing File Entrypoint")
    
    # recursive
    def execFunc(self, ast, perams):
        # exit info
        exit = None

        # create new function scope
        
        # set peram values
        vals = {}
        for p in range(len(ast[0])):
            if ast[0][p].type == "int":
                vals[ast[0][p].id] = (ast[0][p].type, int(self.execToken(perams[p])))
            elif ast[0][p].type == "float":
                vals[ast[0][p].id] = (ast[0][p].type, float(self.execToken(perams[p])))
            elif ast[0][p].type == "str":
                vals[ast[0][p].id] = (ast[0][p].type, str(self.execToken(perams[p])))
            elif ast[0][p].type == "bool":
                vals[ast[0][p].id] = (ast[0][p].type, bool(self.execToken(perams[p])))

        self.scopes.append(vals)

        # exec tokens in tree
        for t in ast[1]:
            if isinstance(t, ast_ret):
                exit = self.execToken(t)
                break
            else:
                self.execToken(t)

        # remove last scope
        self.scopes.pop(len(self.scopes)-1)
        return exit

    def execToken(self, token):
        if isinstance(token, Token):
            if token.type == "NewLine":
                return
            elif token.type == "id":
                if self.scopes[len(self.scopes)-1].get(token.value, False):
                    return self.scopes[len(self.scopes)-1].get(token.value)[1]
                else:
                    if self.scopes[0].get(token.value, False):
                        return self.scopes[0].get(token.value)[1]
                    else:
                        Logger.err(f"Variable \"{token.value}\" is undefined")
            else:
                #print(token)
                return 0
        elif isinstance(token, ast_assign_init):
            if token.type.type == "int":
                self.scopes[len(self.scopes)-1][token.id.value] = (token.type, int(self.execToken(token.value)))
            elif token.type.type == "float":
                self.scopes[len(self.scopes)-1][token.id.value] = (token.type, float(self.execToken(token.value)))
            elif token.type.type == "str":
                self.scopes[len(self.scopes)-1][token.id.value] = (token.type, str(self.execToken(token.value)))
            elif token.type.type == "bool":
                self.scopes[len(self.scopes)-1][token.id.value] = (token.type, bool(self.execToken(token.value)))
        elif isinstance(token, ast_assign):
            if self.scopes[len(self.scopes)-1].get(token.id.value, False):
                self.scopes[len(self.scopes)-1][token.id.value] = (self.scopes[len(self.scopes)-1][token.id.value][0], self.execToken(token.value))
            else:
                Logger.err(f"Variable \"{token.id.value}\" is undefined")
        elif isinstance(token, ast_int):
            return int(token.value)
        elif isinstance(token, ast_float):
            return float(token.value)
        elif isinstance(token, ast_str):
            return str(token.value)
        elif isinstance(token, ast_bool):
            if token.value == "True":
                return True
            elif token.value == "False":
                return False
            else:
                Logger.err(f"Unexpected boolean value \"{token.value}\"")
        elif isinstance(token, ast_add):
            return self.execToken(token.left) + self.execToken(token.right)
        elif isinstance(token, ast_sub):
            return self.execToken(token.left) - self.execToken(token.right)
        elif isinstance(token, ast_mult):
            return self.execToken(token.left) * self.execToken(token.right)
        elif isinstance(token, ast_div):
            return self.execToken(token.left) / self.execToken(token.right)
        elif isinstance(token, ast_mod):
            return self.execToken(token.left) % self.execToken(token.right)
        elif isinstance(token, ast_pow):
            return self.execToken(token.left) ** self.execToken(token.right)
        elif isinstance(token, ast_floor):
            return self.execToken(token.left) // self.execToken(token.right)
        elif isinstance(token, ast_inc):
            if self.scopes[len(self.scopes)-1].get(token.id.value, False):
                self.scopes[len(self.scopes)-1][token.id.value] = (self.scopes[len(self.scopes)-1][token.id.value][0], self.scopes[len(self.scopes)-1][token.id.value][1]+1)
            else:
                Logger.err(f"Variable \"{token.id.value}\" is undefined")
        elif isinstance(token, ast_dec):
            if self.scopes[len(self.scopes)-1].get(token.id.value, False):
                self.scopes[len(self.scopes)-1][token.id.value] = (self.scopes[len(self.scopes)-1][token.id.value][0], self.scopes[len(self.scopes)-1][token.id.value][1]-1)
            else:
                Logger.err(f"Variable \"{token.id.value}\" is undefined")
        elif isinstance(token, ast_and):
            return self.execToken(token.left) and self.execToken(token.right)
        elif isinstance(token, ast_or):
            return self.execToken(token.left) or self.execToken(token.right)
        elif isinstance(token, ast_not):
            return not self.execToken(token.target)
        elif isinstance(token, ast_g):
            return self.execToken(token.left) > self.execToken(token.right)
        elif isinstance(token, ast_ge):
            return self.execToken(token.left) >= self.execToken(token.right)
        elif isinstance(token, ast_l):
            return self.execToken(token.left) < self.execToken(token.right)
        elif isinstance(token, ast_le):
            return self.execToken(token.left) <= self.execToken(token.right)
        elif isinstance(token, ast_equ):
            return self.execToken(token.left) == self.execToken(token.right)
        elif isinstance(token, ast_paren):
            return self.execToken(token.body[0])
        elif isinstance(token, ast_ret):
            return self.execToken(token.value)
        elif isinstance(token, ast_call):
            methods = []
            for i in dir(Builtins):
                if not i.startswith("_"):
                    methods.append(i)

            if token.id in methods:
                args = []
                for t in token.perams:
                    args.append(self.execToken(t))
                if token.id == "print":
                    Builtins.print(args)
            elif self.scopes[0].get(token.id, False):
                return self.execFunc(self.scopes[0].get(token.id), token.perams)
            else:
                return 0
        elif isinstance(token, ast_if):
            for i in range(len(token.bodies)):
                if token.bodies[i][0] == None or self.execToken(token.bodies[i][0]):
                    for t in token.bodies[i][1]:
                        self.execToken(t)
                    break
        else:
            print(token)
            return 0

    # printing class
    def __repr__(self) -> str:
        # change data
        if self.__dict__.get("ast", False):
            ast = self.ast.copy()
            for i in range(len(self.ast)):
                self.ast[i] = str(self.ast[i])

        # dump data
        data = json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=4)
        
        # revert data
        if self.__dict__.get("ast", False):
            self.ast = ast
        return data
