import java.io.InputStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Col {
  public static void main(String[] args) throws Exception {
    if (args.length < 1) {
      System.out.println("Usage: java Col COL_NUM");
      return;
    }
    InputStream is = System.in;
    ANTLRInputStream input = new ANTLRInputStream(is);
    RowsLexer lexer = new RowsLexer(input);
    CommonTokenStream tokens = new CommonTokenStream(lexer);
    int col = Integer.valueOf(args[0]);
    RowsParser parser = new RowsParser(tokens, col);

    parser.setBuildParseTree(false);
    parser.file();
  }
}
