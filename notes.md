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


# 7 Decoupling grammars from application specific code

## 7.5 Sharing Information Among Event Methods

## 8.1 Loading CSV Data
use listener, save data to loader attributes. actions are done in exit~enter nodes state.

## 8.2 Translating JSON to XML
Use listener too, attach the translated string for each subtree to the root of that subtree. Final result is the root node with sub-node data combined in the right way.

## Generating a Call Graph
key: Use Graph class to handle logics about Graph relationship, exporting to DOT. Good abstraction, isolation.


## 8.4 Validating Program Symbol Usage
build a Cymbol validator that checks the following conditions
- Variable references in scope
- Function references have corresponding definitions
- Variables are not used as functions
- Functions are not used as variables

key: *symbol table*
symbol table groups symbols into *scopes*. A scope is just a set of symbols such as a list of parameters for a function or the list of variables and functions in a global scope.
The symbol table is just a repository for symbol definitions.

Two fundamental operations for symbol validation: *defining* symbols and *resolving* symbols.
defining: adding a symbol to a scope
resolving: figuring out which definition the symbol refers to

*data structure*:
- BaseScope
- GlobalScope
- LocalScope
- Symbol
- FunctionSymbol
- VariableSymbol


### Error REcovery Fail-Safe
e.g. for Simple.g4, this input:
```
class T {
  int int x;
}
```

'int int'-(sync-and-return)->emit error
detail:
'int int' doesn't fit , resynchronization set for [prog, classDef, member], but for `classDef+` and `member+` loops,
for `member` parser could loop back and find another member or exit the loop and find the '}'.
for `classDef`, to see the start of another class or simply exit `prog`.
so the resynchronization set now is {'int', '}', 'class'} // for member, exit prog and class.

`int` is in the resynchronization set, so parser recovers without consuming a token.
return to the caller: the `member+` loop. The parser detects another error when it retries to match
another `member`.
