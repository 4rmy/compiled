import json
from utilities.logger import Logger
from utilities.token import Token
from utilities.constants import *

# Lexer class
class Lexer:
    # construct
    def __init__(self, path: str):
        # init defaults
        self.path = ""
        self.code = ""

        self.character = 0
        self.line = 0

        self.tokens = []

        # update true values
        self.path = path
        with open(path, 'r') as f:
            for l in f.readlines():
                self.code += l

        self.lex()

    def getTokens(self):
        return self.tokens

    def lex(self):
        self.tokens = []

        # loop all characters in the code
        while self.character < len(self.code):
            if self.code[self.character] in [*"\t "]:
                self.character += 1
                continue
            
            # tokenizing info
            # comments
            if self.code[self.character] == "#":
                while self.character < len(self.code) and self.code[self.character] != "\n":
                    self.character += 1
            # line builder
            elif self.code[self.character] in [*"\n;"]:
                # "new line" token
                self.tokens.append(Token("NewLine"))

                # only "\n" increments the line
                if self.code[self.character] == "\n":
                    self.line += 1

            # id builder
            elif self.code[self.character] in [*LETTERS]:
                self.build_id() # build corresponding id
            
            # number builder
            elif self.code[self.character] in [*NUMBERS]:
                self.build_numeric() # build corresponding number constant
            
            # string builder
            elif self.code[self.character] in [*"'\"`"]:
                self.build_string() # build corresponding string constant

            # Additive operators
            elif self.code[self.character] == "+":
                # special
                if self.code[self.character+1] == "+":
                    self.tokens.append(Token("Operator", "Increment"))
                    self.character += 1
                # normal
                else:
                    self.tokens.append(Token("Operator", "Add"))
            
            # Subtractive operators
            elif self.code[self.character] == "-":
                # special
                if self.code[self.character+1] == "-":
                    self.tokens.append(Token("Operator", "Decrement"))
                    self.character += 1
                # normal
                else:
                    self.tokens.append(Token("Operator", "Subtract"))

            # Multiplicative operators
            elif self.code[self.character] == "*":
                # special
                if self.code[self.character+1] == "*":
                    self.tokens.append(Token("Operator", "Power"))
                    self.character += 1
                # normal
                else:
                    self.tokens.append(Token("Operator", "Multiply"))
            
            # Division operators
            elif self.code[self.character] == "/":
                # special
                if self.code[self.character+1] == "/":
                    self.tokens.append(Token("Operator", "Floor"))
                    self.character += 1
                # normal
                else:
                    self.tokens.append(Token("Operator", "Divide"))

            # Mod operators
            elif self.code[self.character] == "%":
                # special
                if self.code[self.character+1] == "%%":
                    self.tokens.append(Token("Operator", "Remainder"))
                    self.character += 1
                # normal
                else:
                    self.tokens.append(Token("Operator", "Mod"))

            # Parenthesis
            elif self.code[self.character] in [*"()"]:
                if self.code[self.character] == "(":
                    self.tokens.append(Token("LParen"))
                elif self.code[self.character] == ")":
                    self.tokens.append(Token("RParen"))

            # Seperator
            elif self.code[self.character] == ",":
                self.tokens.append(Token("Seperator"))

            # And Operator
            elif self.code[self.character] == "&":
                if self.code[self.character+1] == "&":
                    self.character += 1
                    self.tokens.append(Token("Comp", "and"))
            
            # Or Operator
            elif self.code[self.character] == "|":
                if self.code[self.character+1] == "|":
                    self.character += 1
                    self.tokens.append(Token("Comp", "or"))
            
            # Not Operator
            elif self.code[self.character] == "!":
                self.tokens.append(Token("Comp", "not"))

            # Equals & Assign Operator
            elif self.code[self.character] == "=":
                if self.code[self.character+1] == "=":
                    self.character += 1
                    self.tokens.append(Token("Comp", "equals"))
                else:
                    self.tokens.append(Token("Operator", "assign"))

            # increment character
            self.character += 1
        
        # "end of file" token
        self.tokens.append(Token("EOF"))
    
    def build_id(self):
        # empty id value
        id = ""

        # loop while still in an id
        while self.character < len(self.code) and self.code[self.character] in [*LETTERS] + [*NUMBERS]:
            id += self.code[self.character]

            # keep incrementing
            self.character += 1
        
        # create token and add it to the list
        self.tokens.append(Token("id", id))

        # adjust for offset
        self.character -= 1

    def build_numeric(self):
        # empty id value
        id = "int"
        val = ""

        # loop while still in an id
        while self.character < len(self.code) and self.code[self.character] in [*(NUMBERS+".")]:
            val += self.code[self.character]
            # floating points
            if self.code[self.character] == ".":
                if id == "int":
                    id = "float"
                else:
                    Logger.err(f"Line {self.line}: floating point has decimal")

            # increment character
            self.character += 1
        
        # create token and add it to the list
        self.tokens.append(Token(id, val))

        # adjust for offset
        self.character -= 1

    def build_string(self):
        starter = self.code[self.character]
        value = ""

        # offset string starter
        self.character += 1
        # loop for string
        while self.character < len(self.code) and self.code[self.character] != starter:
            # update value
            value += self.code[self.character]
            # increment character
            self.character += 1

        # add token
        self.tokens.append(Token("str", value))

        # no subtraction needed bc of string closer

    # printing class
    def __repr__(self) -> str:
        tks = self.tokens.copy()
        for i in range(len(self.tokens)):
            self.tokens[i] = str(self.tokens[i])
        data = json.dumps(self.__dict__, indent=4)
        self.tokens = tks
        return data
