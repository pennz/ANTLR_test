import sys
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    tree = parser.startRule()
 
if __name__ == '__main__':
    main(sys.argv)
