# Hyper Language
This project was created to make a language that is able to be interpreted
for fast testing, but also compiled for fast execution when deployed.
(Not compiled yet bc windows asm is... fun.)

## Features
### Current
- Functions
- Variables
- Mathmatical Operations
    - Order of operations
- Interpreter
- Timing
    - Optional
- Boolean Values
- Boolean Comparisons
    - &&
    - ||
    - !
- Value Comparisons
    - ==
    - \>
    - <
    - \>=
    - <=
- If statements
    - If
    - Else
    - Elseif

### In Progress
- Nothing, I'm done for today because sleeping is cool sometimes

### Coming Soon
- Loops
    - For
    - While

### Future Plans
- Classes
- External Modules
- Packaging

## Syntax
### Entry Point
In the Hyper langauge, it is necessary to have an entry point. This is because the program needs to
know where to start from when compiled (and exit codes, but thats later).
To begin the program, you need to start with the `main` function, which returns an integer.
```
func int main()
    ret 0
end
```
In this example, we have the main function as an entry point. The function contains a `ret` or return
in order to return an exit code. The exit code just lets you and the system know if your program
executed and finished properly.

### Variables
The next thing to look at is a variable. Variables let you store information to be used in the future.
In this example, we will create an **Integer** variable named `my_integer`. You could name this
anything you want but as an example, I will call it this.
```
func int main()
    int my_integer = 0

    ret 0
end
```
As you can see, I started with my entry point to the program and added in the `int my_integer = 0`
line to create the variable. There are other types of values that can be created and used. In this snippet, I will include the other values types.
```
func int main()
    int my_integer = 0
    float my_float = 0.0
    str my_string = ""
    bool my_boolean = False

    ret 0
end
```
Here, we have the `Integer` type as `int`, the `Floating Point` type as `float`, the `String` type as
`str`, and lastly, the `Boolean` type as `bool`.

### Functions
You can define a function in the same way you defined the entry point, but you have to change the name of it and the type of it, only if you want to return a different type. For instance, if you want a function that returns a float value and you want the function to be called `my_function` you would add the following to your code.
```
func float my_function()
    ret 0.0
end
```
You can then call this function from your main function, we will store the result in a variable, like so:
```
func int main()
    float my_float = my_function()

    ret 0
end
```

### If Statements
#### Basic If
All `If` statements begin with `if` and a conditional in `()` and end with `end` (that's a mouthful). Here is an example:
```
func int main()
    if (1 < 2)

    end

    ret 0
end
```
In that scenario, 1 < 2 is always true, therefore, the body between the `if` and `end` segments will always execute.
#### If Else
For an `If Else` statement, you can follow the same format as an `If` statement, but add an else in the main body, like so:
```
func int main()
    if (2 < 1)

    else

    end

    ret 0
end
```
In this case, 2 is always less than 1, meaning the else segment will always execute.
#### Else If
Lastly, for an `Else If` statement, you can follow the same format as an `If` statement, but add an `else` before the `if` inside of a regular `If` statement, like so:
```
func int main()
    if (2 < 1)

    elseif (3 > 2)

    end

    ret 0
end
```
this will cause the 3 to always be greater than 2, resulting in the `elseif` segment to always execute instead of the `if` segment
