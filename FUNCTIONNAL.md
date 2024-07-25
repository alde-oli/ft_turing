# Guidelines to Respect Functional Paradigm in the Code (with Scala)

1. **Use Immutable Data Structures (e.g., `val` instead of `var`):**
   - `val` is a constant; it can't be reassigned.
   - `var` is a variable; it can be reassigned.
   - **Goal:** Make new values instead of changing existing ones.

2. **Use Pure Functions:**
   - A function is pure if it has no side effects.
   - A function is pure if it always returns the same output for the same input.
   - A function is pure if it doesn't modify the input.
   - A function is pure if it doesn't depend on external state.
   - **Goal:** Avoid side effects and make the code easier to reason about.

3. **Use Expressions Instead of Statements:**
   - An expression is a piece of code that returns a value.
   - A statement is a piece of code that performs an action.
   - **Goal:** Make the code more concise and readable.

4. **Use First-Class Functions:**
   - A function is first-class if it can be passed as an argument to another function.
   - A function is first-class if it can be returned as a value from another function.
   - A function is first-class if it can be assigned to a variable.
   - **Goal:** Make the code more modular and reusable.
   - In Scala, we can use functions as values: `val add = (x: Int, y: Int) => x + y`.

5. **Use Higher-Order Functions:**
   - A higher-order function is a function that takes other functions as arguments.
   - A higher-order function is a function that returns a function.
   - **Goal:** Use functions like `map`, `flatMap`, `filter`, or `fold` to work with collections.

6. **Use Recursion Instead of Loops:**
   - A recursive function is a function that calls itself.
   - A recursive function is a function that breaks down a problem into smaller subproblems.
   - **Goal:** Make the code more declarative and easier to understand.

7. **Use Monads to Handle Side Effects:**
   - A monad is a container type that represents a computation.
   - A monad is a container type that can be used to chain computations.
   - A monad is a container type that can be used to handle side effects.
   - **Goal:** Make the code more modular and easier to test.
   - Examples of monads: `Option`, `Try`, `Future`, `List`, etc.

8. **Use Pattern Matching Instead of If/Else:**
   - Pattern matching is a powerful feature of Scala that allows matching values against patterns.
   - Pattern matching is a powerful feature of Scala that allows destructuring complex data structures.
   - **Goal:** Make the code more concise and readable.

9. **Model with Traits and Case Classes:**
   - A trait is a type that defines a set of methods that a class must implement.
   - A case class is a class that is optimized for pattern matching.
   - **Goal:** Make the code more modular and easier to extend.

## To Avoid

- Mutable data structures (e.g., `var`).
- Side effects (e.g., `println`).
- Null values (e.g., `null`).
- Exceptions (e.g., `try/catch`).
- Loops (e.g., `for`, `while`).
- If/Else statements (e.g., `if`, `else`).
- Imperative programming (e.g., `var`, `while`, `for`, `if`, `else`).
- Null pointer exceptions (e.g., `NullPointerException`).
- Runtime errors (e.g., `ArrayIndexOutOfBoundsException`).
