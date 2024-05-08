from parser.djParser import djParser
from parser.djVisitor import djVisitor

class MyDjVisitor(djVisitor):
    def visitStart(self, ctx: djParser.StartContext):
        return self.visitExpression(ctx.expression())

    def visitExpression(self, ctx: djParser.ExpressionContext):  
        operator = ctx.OPERATION().getText()
        operands = self.visit(ctx.getChild(2))
        return self.handleOperation(operator, operands)
        
    def visitOperands(self, ctx: djParser.OperandsContext):
        opCount = ctx.getChildCount()
        operands = list()
        for i in range(0,opCount,2):
            operands.append(self.visit(ctx.getChild(i)))
        return operands
        
    def visitValue(self, ctx: djParser.ValueContext):
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        
    def handleOperation(self, operator: str, operands: list):
        if operator == '+':
            return self.handleSum(operands)
        elif operator == '*':
            return self.handleProduct(operands)
        elif operator == '~':
            return self.handleCount(operands)
        elif operator == '/':
            return self.handleInverse(operands)
        
    def handleSum(self, operands: list):
        return sum(operands)
    
    def handleProduct(self, operands: list):
        result = 1
        for op in operands:
            result = result * op
        return result
    
    def handleCount(self, operands: list):
        return len(operands)
    
    def handleInverse(self, operands: list):
        return (1 / self.handleProduct(operands))