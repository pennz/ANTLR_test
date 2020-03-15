import java.io.FileInputStream;
import java.io.InputStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class InsertSerialID {
  public static void main(String[] args) throws Exception {
    String inputFile = null;
    if (args.length > 0) inputFile = args[0];
    InputStream is = System.in;
    if (inputFile != null) is = new FileInputStream(inputFile);
    ANTLRInputStream input = new ANTLRInputStream(is);
    JavaLexer lexer = new JavaLexer(input);
    CommonTokenStream tokens = new CommonTokenStream(lexer);
    JavaParser parser = new JavaParser(tokens);
    ParseTree tree = parser.compilationUnit();

    ParseTreeWalker walker =
        new ParseTreeWalker(); // create standard walker ExtractInterfaceListener
    InsertSerialIDListener extractor = new InsertSerialIDListener(tokens); // here we deal with tokens
    walker.walk(extractor, tree); // lazy evaluation

    System.out.println(extractor.rewriter.getText());
  }
}
