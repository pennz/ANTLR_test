## Parse-Tree Visitor
Page 20

### Parsing Terms
Key Concepts

# A Starter ANTLR Project
Java example, array initializers as a sequence of explicit array-element initializers,
and java class file size limit, by converting array initializers to strings, it is
more compact.

## Tool, Runtime, and Generated Code

## 5.3 Common Language Patterns
### Sequence
```
retr    :   'RETR' INT '\n' ; // match keyword integer newline sequence

files   :   (row '\n') *    ; // * also works, and with a '\n' terminator
```
\* + or ? have their meaning
### Choice(Alternatives)

\| as the "or" operator.
Grammars are full of choices.

### Token Dependency

```
vector : '[' INT+ ']'   ;

```
() {} or ternary operator a?b:c

### Nested Phrase

life is a loop...

As we saw in Section 2.1, Let's Get Meta!, on page 9, the internal tree nodes are rule references, and the leaves are token references. A path from the root of the tree to any node represents the rule invocation stack for that element (or call stack for an ANTLR-generated recursive-descent parser).

## 5.4 Dealing with Precedence, Left Rcursion, and Associativity
e.g. 1 + 2 * 3 ( * has higher precdence)
2^3^4 as 2^(3^4) ( exponentiation group right to left, i.e., right association)

## 5.5 Recognizing Common Lexical Structures
parsers recognize grammatical Structures in a token stream and lexers recognize
grammatical structures in a character stream.

In ANTLR, we differ lexing and parsing by starting lexer rule names with
uppercase letters and parser rule names with lowercase letters.

common lexical constructs: identifiers, numbers, strings, comments, and
whitespace.

### Matching Identifiers
ANTLR lexers resolve ambiguities between lexical rules by favoring the rule
specified first. That is to say, ID lexical rule put after keyword rules.

### Matching Numbers ...
### Matching String Literals
Comments and Whitespace

... SKIP it, later we will read this.
## 5.6 Drawing the Line Between Lexer and Parser
rules of thumb:
- match and discard anything in the lexer that the parser does not need to see
    at all
- match common tokens.
- lump together into a single token type those lexical structures that parser
    does not need to distinguish
- lump together ... can be treated as a single entity.kk

e.g. switch lexer rule IP to parser rule ip

## Exploring Some Real Grammars

### CSV
### JSON
fragment is used to reduce duplication and make the grammar easier to read.
fragment is the component of tokens. not token itself.
### DOT
What we have learn?
we often have to look at multiple sources to unmask an entire language.
We also have to decide what is properly part of the parsing process and what should be processed later as a separate phase.
e.g., port rule in DOT, HTML_STRING

