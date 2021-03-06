Scriptable is a sand-boxed scripting engine which can be used safely in an embedded environment.

Its canonical abstract syntax tree model is designed to support various syntax forms.
At the moment the typescript syntax as well as the hypothesis syntax 
(a typescript syntax subset used for logical reasoning) and the mustache syntax are supported.

The scripting engine forbids endless loops and has a recursion guard, which detects loops in
a function call stack. In addition to that scriptable allows to define more detailed AST
restrictions. At the moment following restrictions are supported:

 * max_precision # The max allowed number of digits in a number. 
 * max_scale     # The max allowed digits to the right of the decimal point in a number.
 * max_loops     # The max allowed number of loop iterations.

**Usage**

TypescriptEngine
```typescript
engine = TypescriptEngine.parse("""
   function fibonacci(n:number) {
      if (n == 0) return 0
      if (n == 1) return 1
      if (n == 2) return 1
      return fibonacci(n - 1) + fibonacci(n - 2)
   }
   
   fibonacci(8) // returns 21
""")
    
engine.execute()
```

HypothesisEngine
```typescript
engine = HypothesisEngine.parse("x > 0")
engine.execute({"x": 1}) // returns True
```

MustacheEngine
```typescript
engine = MustacheEngine.parse("text {{x}} text")
engine.execute({"x": 1}) // returns "text 1 text"
```