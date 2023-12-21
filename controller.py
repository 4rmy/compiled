from parts.lexer import Lexer
from parts.parser import Parser
from parts.interpreter import Interpreter
import parts.builder
from utilities.logger import Logger
import time

# debugging stuff
TIMING = False
OUTPUT = False

# setup output
if OUTPUT:
    out = open("./out/log.txt", 'w')
    Logger.setup(OUTPUT, out)

# file path
path = "./tests/test1.hyp"

# lex the file
if TIMING:
    Logger.info("Lexing file")
start = time.time_ns()
lexer = Lexer(path)
end = time.time_ns()
if TIMING:
    Logger.info(f"Lexing took {(end - start)/1000000} milliseconds")
if OUTPUT:
    print(lexer, file=out)

# parse the file
if TIMING:
    Logger.info("Parsing data")
start = time.time_ns()
parser = Parser(lexer.tokens)
end = time.time_ns()
if TIMING:
    Logger.info(f"Parsing took {(end - start)/1000000} milliseconds")
if OUTPUT:
    print(parser, file=out)

# interpret
Logger.info("Executing...")
start = time.time_ns()
interpreter = Interpreter(parser.ast)
end = time.time_ns()
if TIMING:
    Logger.info(f"Interpreting took {(end - start)/1000000} milliseconds")
if OUTPUT:
    print(interpreter, file=out)
