import json
from utilities.token import *
from utilities.constants import *
import colorama

class Parser:
    def __init__(self, tokens: list) -> None:
        self.ast = self.parse(tokens.copy())
    
    # WARNING:
    # RECURSIVE
    # (LARGE STACK)
    def parse(self, tkns: list):
        ast = tkns.copy()
        
        # convert constants
        for t in range(len(ast)):
            if isinstance(ast[t], Token):
                if ast[t].type == "int":
                    ast[t] = ast_int(ast[t].value)
                elif ast[t].type == "float":
                    ast[t] = ast_float(ast[t].value)
                elif ast[t].type == "str":
                    ast[t] = ast_str(ast[t].value)
                elif ast[t].type == "bool":
                    ast[t] = ast_bool(ast[t].value)

        # convert types
        for t in range(len(ast)):
            if isinstance(ast[t], Token):
                if ast[t].type == "id":
                    if ast[t].value == "int":
                        ast[t] = ast_type("int")
                    elif ast[t].value == "float":
                        ast[t] = ast_type("float")
                    elif ast[t].value == "str":
                        ast[t] = ast_type("str")
                    elif ast[t].value == "bool":
                        ast[t] = ast_type("bool")
        
        # form parentheses
        building = False
        paren_body = []
        start = 0
        index = 0
        t = 0
        while t < len(ast):
            if isinstance(ast[t], Token):
                if ast[t].type == "LParen":
                    if index == 0:
                        building = True
                        start = t
                    else:
                        paren_body.append(ast[t])
                    index += 1
                elif ast[t].type == "RParen":
                    index -= 1
                    if index == 0:
                        building = False
                        ptok = ast_paren(paren_body)
                        ast[start] = ptok
                        ast[start].body = self.parse(ast[start].body)
                        paren_body = []
                        ast = ast[:start+1] + ast[t+1:]
                    else:
                        paren_body.append(ast[t])
                else:
                    if building:
                        paren_body.append(ast[t])
            else:
                if building:
                    paren_body.append(ast[t])
            
            # next token
            t += 1
        
        # create functions
        t = 0
        func_body = []
        start = 0
        end = 0
        index = 0
        building = False
        while t < len(ast):
            if isinstance(ast[t], Token):
                if ast[t].type == "id":
                    if not building:
                        if ast[t].value == "func":
                            func_body = []
                            start = t
                            building = True
                    else:
                        if ast[t].value == "end":
                            if index == 0:
                                building = False
                                func_body = func_body[3:]
                                ast[start] = ast_func(ast[start+1], ast[start+2], self.functionPerams(ast[start+3]), func_body)
                                end = t

                                t = start
                                for _ in range(end - start):
                                    ast.pop(t + 1)
                                
                                ast[t].body = self.parse(ast[t].body)
                            else:
                                index -= 1
                                func_body.append(ast[t])
                        else:
                            if ast[t].value == "if":
                                index += 1
                            func_body.append(ast[t])
                else:
                    if building:
                        func_body.append(ast[t])
            else:
                if building:
                    func_body.append(ast[t])
            t += 1
        
        # if statements
        t = 0
        while t < len(ast):
            if isinstance(ast[t], Token):
                if ast[t].type == "id":
                    if ast[t].value == "if":
                        ast = self.ifStatement(ast, t).copy()
            t += 1

        # function calls
        t = 0
        while t < len(ast):
            if isinstance(ast[t], ast_paren):
                if isinstance(ast[t-1], Token):
                    if ast[t-1].type == "id" and ast[t-1].value not in KEYWORDS:
                        
                        t1 = 0
                        while t1 < len(ast[t].body):
                            if isinstance(ast[t].body[t1], Token):
                                if ast[t].body[t1].type == "Seperator":
                                    ast[t].body.pop(t1)
                                    continue
                            t1 += 1
                        
                        ast[t-1] = ast_call(ast[t-1].value, ast[t].body)
                        ast.pop(t)
                        t -= 1
            t += 1

        # order of operations
        ## increment and decrement
        t = 0
        while t < len(ast):
            if isinstance(ast[t], Token):
                if ast[t].type == "Operator":
                    if ast[t].value == "Increment":
                        ast[t] = ast_inc(ast[t-1])
                        t -= 1
                        ast.pop(t)
                    elif ast[t].value == "Decrement":
                        ast[t] = ast_dec(ast[t-1])
                        t -= 1
                        ast.pop(t)
            t += 1
        
        ## multi + div + mod + pow + floor
        t = 0
        while t < len(ast):
            if isinstance(ast[t], Token):
                if ast[t].type == "Operator":
                    if ast[t].value == "Multiply":
                        ast[t] = ast_mult(ast[t-1], ast[t+1])
                        t -= 1
                        ast.pop(t)
                        ast.pop(t+1)
                    elif ast[t].value == "Divide":
                        ast[t] = ast_div(ast[t-1], ast[t+1])
                        t -= 1
                        ast.pop(t)
                        ast.pop(t+1)
                    elif ast[t].value == "Mod":
                        ast[t] = ast_mod(ast[t-1], ast[t+1])
                        t -= 1
                        ast.pop(t)
                        ast.pop(t+1)
                    elif ast[t].value == "Power":
                        ast[t] = ast_pow(ast[t-1], ast[t+1])
                        t -= 1
                        ast.pop(t)
                        ast.pop(t+1)
                    elif ast[t].value == "Floor":
                        ast[t] = ast_floor(ast[t-1], ast[t+1])
                        t -= 1
                        ast.pop(t)
                        ast.pop(t+1)
            t += 1
        ## add + sub
        t = 0
        while t < len(ast):
            if isinstance(ast[t], Token):
                if ast[t].type == "Operator":
                    if ast[t].value == "Add":
                        ast[t] = ast_add(ast[t-1], ast[t+1])
                        t -= 1
                        ast.pop(t)
                        ast.pop(t+1)
                    elif ast[t].value == "Subtract":
                        ast[t] = ast_sub(ast[t-1], ast[t+1])
                        t -= 1
                        ast.pop(t)
                        ast.pop(t+1)
            t += 1
        
        # comparisons
        t = 0
        while t < len(ast):
            if isinstance(ast[t], Token):
                if ast[t].type == "Comp":
                    if ast[t].value == "and":
                        ast[t] = ast_and(ast[t-1], ast[t+1])
                        ast.pop(t-1)
                        t -= 1
                        ast.pop(t+1)
                    elif ast[t].value == "or":
                        ast[t] = ast_or(ast[t-1], ast[t+1])
                        ast.pop(t-1)
                        t -= 1
                        ast.pop(t+1)
                    elif ast[t].value == "not":
                        ast[t] = ast_not(ast[t+1])
                        ast.pop(t+1)
                    elif ast[t].value == "equals":
                        ast[t] = ast_equ(ast[t-1], ast[t+1])
                        ast.pop(t-1)
                        t -= 1
                        ast.pop(t+1)
                    elif ast[t].value == "g":
                        ast[t] = ast_g(ast[t-1], ast[t+1])
                        ast.pop(t-1)
                        t -= 1
                        ast.pop(t+1)
                    elif ast[t].value == "l":
                        ast[t] = ast_l(ast[t-1], ast[t+1])
                        ast.pop(t-1)
                        t -= 1
                        ast.pop(t+1)
                    elif ast[t].value == "ge":
                        ast[t] = ast_ge(ast[t-1], ast[t+1])
                        ast.pop(t-1)
                        t -= 1
                        ast.pop(t+1)
                    elif ast[t].value == "le":
                        ast[t] = ast_le(ast[t-1], ast[t+1])
                        ast.pop(t-1)
                        t -= 1
                        ast.pop(t+1)
            t += 1

        # assignments
        t = 0
        while t < len(ast):
            if isinstance(ast[t], Token):
                if ast[t].type == "Operator":
                    if ast[t].value == "assign":
                        if isinstance(ast[t-2], ast_type):
                            ast[t] = ast_assign_init(ast[t-2], ast[t-1], ast[t+1])
                            t -= 2
                            ast.pop(t)
                            ast.pop(t)
                            ast.pop(t+1)
                        else:
                            ast[t] = ast_assign(ast[t-1], ast[t+1])
                            t -= 1
                            ast.pop(t)
                            ast.pop(t+1)
            t += 1

        # returns
        t = 0
        while t < len(ast):
            if isinstance(ast[t], Token):
                if ast[t].type == "id":
                    if ast[t].value == "ret":
                        ast[t] = ast_ret(ast[t+1])
                        ast.pop(t+1)
            t += 1

        return ast

    def functionPerams(self, tkn:ast_paren):
        peramlist = []
        t=0
        while t < len(tkn.body):
            if isinstance(tkn.body[t], ast_type):
                peramlist.append(ast_peram(tkn.body[t].type, tkn.body[t+1].value))
            t += 1
        return peramlist

    def ifStatement(self, ast: list, tkn_index: int):
        tknlist = ast.copy()
        bodies = []

        conditional = tknlist[tkn_index+1]
        body = []
        building = True
        start = tkn_index
        index = 0
        
        t = tkn_index + 2
        while t < len(tknlist):
            if isinstance(tknlist[t], Token):
                if tknlist[t].type == "id":
                    if tknlist[t].value == "if":
                        if not building:
                            start = t
                            building = True

                            body = []
                            conditional = tknlist[t+1]

                            t = t + 1
                        else:
                            body.append(tknlist[t])
                            index += 1
                    elif tknlist[t].value == "end":
                        if building:
                            if index == 0:
                                building = False
                                bodies.append((conditional, body))

                                while t > start:
                                    tknlist.pop(t)
                                    t -= 1

                                for i in range(len(bodies)):
                                    bodies[i] = (bodies[i][0], self.parse(bodies[i][1]))
                                
                                tknlist[tkn_index] = ast_if(bodies)
                            else:
                                index -= 1
                                body.append(tknlist[t])
                    elif tknlist[t].value == "else":
                        if building:
                            if index == 0:
                                bodies.append((conditional, body))
                                while t > start:
                                    tknlist.pop(t)
                                    t -= 1
                                body = []
                                conditional = None
                            else:
                                body.append(tknlist[t])
                    elif tknlist[t].value == "elseif":
                        if building:
                            if index == 0:
                                bodies.append((conditional, body))
                                while t > start:
                                    tknlist.pop(t)
                                    t -= 1
                                body = []
                                conditional = tknlist[t+1]

                                t = t + 1
                            else:
                                body.append(tknlist[t])
                    else:
                        if building:
                            body.append(tknlist[t])
                else:
                    if building:
                        body.append(tknlist[t])
            else:
                if building:
                    body.append(tknlist[t])

            t += 1

        return tknlist

    # printing class
    def __repr__(self) -> str:
        ast = self.ast.copy()
        for i in range(len(self.ast)):
            self.ast[i] = str(self.ast[i])
        data = json.dumps(self.__dict__, indent=4)
        self.ast = ast
        return data