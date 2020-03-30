## Parse-Tree Visitor
Page 20

### Parsing Terms
Key Concepts

# A Starter ANTLR Project
Java example, array initializers as a sequence of explicit array-element initializers,
and java class file size limit, by converting array initializers to strings, it is
more compact.

## Tool, Runtime, and Generated Code


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
But it must consume one token now, and the resync set contains just `int`, so it goes to the 
3rd test, these time, it got right.
