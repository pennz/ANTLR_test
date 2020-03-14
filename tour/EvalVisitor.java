import java.util.HashMap;
import java.util.Map;

public class EvalVisitor extends LabeledExprBaseVisitor<Integer> { 
    /** "memory" for our calculator;
      variable/value pairs go here */ 
    Map<String, Integer> memory = new HashMap<String, Integer>();
    /** ID '=' expr NEWLINE */
    @Override
    public Integer visitAssign(LabeledExprParser.AssignContext ctx) {
        String id = ctx.ID().getText(); // id is left-hand side of '='
        int value = visit(ctx.expr()); // compute value of expression on right 
        memory.put(id, value); // store it in our memory
        System.out.printf("%s = %d\n", id, value); // print the result
        return value;
    }

    /** expr CLEAR */
    @Override
    public Integer visitClear(LabeledExprParser.ClearContext ctx) {
        System.out.println("Before, memory size is "+ memory.size()+", Clear now"); // print the result
        memory.clear();
        return 0; // return dummy value
    }
    /** expr NEWLINE */
    @Override
    public Integer visitPrintExpr(LabeledExprParser.PrintExprContext ctx) {
        Integer value = visit(ctx.expr()); // evaluate the expr child 
        System.out.println(value); // print the result
        return 0; // return dummy value
    }
    /** INT */
    @Override
    public Integer visitInt(LabeledExprParser.IntContext ctx) {
        return Integer.valueOf(ctx.INT().getText());
    }
    /** ID */
    @Override
    public Integer visitId(LabeledExprParser.IdContext ctx) {
        String id = ctx.ID().getText();
        if ( memory.containsKey(id) ) return memory.get(id);
        System.err.printf("%s cannot be found.\n", id);
        return 0;
    }
    /** expr op=('*'|'/') expr */
    @Override
    public Integer visitMulDiv(LabeledExprParser.MulDivContext ctx) {
        int left = visit(ctx.expr(0)); // get value of left subexpression 
        int right = visit(ctx.expr(1)); // get value of right subexpression 
        if ( ctx.op.getType() == LabeledExprParser.MUL ) return left * right;
        return left / right; // must be DIV
    }
    /** expr op=('+'|'-') expr */
    @Override
    public Integer visitAddSub(LabeledExprParser.AddSubContext ctx) {
        int left = visit(ctx.expr(0)); // get value of left subexpression 
        int right = visit(ctx.expr(1)); // get value of right subexpression 
        if ( ctx.op.getType() == LabeledExprParser.ADD ) return left + right;
        return left - right; // must be SUB
    }
    /** '(' expr ')' */
    @Override
    public Integer visitParens(LabeledExprParser.ParensContext ctx) {
        return visit(ctx.expr()); // return child expr's value 
    }
}
