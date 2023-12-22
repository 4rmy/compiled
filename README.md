# Hyper Language
This project was created to make a language that was able to be interpreted
for fast testing, but also compiled for fast execution when deployed.

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

### In Progress
- Nothing rn because I wanna sleep
    - Zzzzzzz

### Coming Soon
- Value Comparisons
    - ==
    - \>
    - <
    - \>=
    - <=
- If statements
- Else statements
- Else-If statements
- Loops
    - For
    - While

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

### There is more to this but I can't be bothered rn