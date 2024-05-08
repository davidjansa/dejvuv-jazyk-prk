from antlr4.error.ErrorListener import ErrorListener

""" Overridden ErrorListener that raises error instead of printing the message

Raises:
    Exception: parser exception
"""
class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError("line " + str(line) + ":" + str(column) + " " + msg)