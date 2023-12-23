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
- Value Comparisons
    - ==
    - \>
    - <
    - \>=
    - <=

### In Progress
- If statements
- If-Else statements
- Else-If statements

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