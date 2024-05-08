from parser.djLexer import djLexer
from parser.djParser import djParser
from myDjVisitor import MyDjVisitor
from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from myErrorListener import MyErrorListener

class DjCalculator:
    def __init__(self):
        pass
    
    def calculate(self, input: str):
        try:
            # # create lexer and parser
            lexer = djLexer(InputStream(input))
            stream = CommonTokenStream(lexer)
            parser = djParser(stream)
            
            # remove error listeners
            parser.removeErrorListeners()
            # add MyErrorListener
            parser.addErrorListener(MyErrorListener())

            # get the parse tree
            tree = parser.start()

            # create tree visitor
            visitor = MyDjVisitor()

            # visit tree with visitor
            return visitor.visit(tree)
        except Exception as e:
            raise e