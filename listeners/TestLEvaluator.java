public static class Evaluator extends LExprBaseListener {
  Stack<Integer> stack = new Stack<Integer>();

  public void exitMult(LExprParser.MultContext ctx) {
    int right = stack.pop();
    int left = stack.pop();
    stack.push(left * right);
  }

  public void exitAdd(LExprParser.AddContext ctx) {
    int right = stack.pop();
    int left = stack.pop();
    stack.push(left + right);
  }

  public void exitInt(LExprParser.IntContext ctx) {
    stack.push(Integer.valueOf(ctx.INT().getText()));
  }
}
