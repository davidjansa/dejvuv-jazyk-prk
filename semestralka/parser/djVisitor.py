# Generated from c:/Users/David/Documents/.ja/skola/ing/PRK/dejvuv-jazyk-prk/semestralka/dj.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .djParser import djParser
else:
    from djParser import djParser

# This class defines a complete generic visitor for a parse tree produced by djParser.

class djVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by djParser#start.
    def visitStart(self, ctx:djParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by djParser#expression.
    def visitExpression(self, ctx:djParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by djParser#operands.
    def visitOperands(self, ctx:djParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by djParser#value.
    def visitValue(self, ctx:djParser.ValueContext):
        return self.visitChildren(ctx)



del djParser