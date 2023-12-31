import json

# lexer token
class Token():
    def __init__(self, type: str, value: str = "") -> None:
        self.type = type
        self.value = value

    # stringify for debugging
    def __str__(self) -> str:
        ret = ""
        if self.value != "":
            ret = f"[{self.type}: {self.value}]"
        else:
            ret = f"[{self.type}]"
        return ret

    # printing class
    def __repr__(self) -> str:
        ret = ""
        if self.value != "":
            ret = f"[{self.type}: {self.value}]"
        else:
            ret = f"[{self.type}]"
        return ret

# ast tokens
class ast_token_super:
    pass

# types
class ast_float(ast_token_super):
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Float: {self.value}]"
class ast_int(ast_token_super):
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Int: {self.value}]"
class ast_str(ast_token_super):
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Str: {self.value}]"
class ast_bool(ast_token_super):
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Bool: {self.value}]"
# type
class ast_type(ast_token_super):
    def __init__(self, t) -> None:
        self.type = t
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Type: {self.type}]"
# parentheses
class ast_paren(ast_token_super):
    def __init__(self, body: list) -> None:
        self.body = body
        super().__init__()

    def __str__(self) -> str:
        return f"[Paren: {self.body}]"
# operations
class ast_add(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Add: {self.left}, {self.right}]"
class ast_sub(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Sub: {self.left}, {self.right}]"
class ast_mult(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Mult: {self.left}, {self.right}]"
class ast_div(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Div: {self.left}, {self.right}]"
class ast_mod(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Mod: {self.left}, {self.right}]"
class ast_pow(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Power: {self.left}, {self.right}]"
class ast_floor(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    
    def __str__(self) -> str:
        return f"[Floor: {self.left}, {self.right}]"
class ast_inc(ast_token_super):
    def __init__(self, id) -> None:
        self.id = id
        super().__init__()
    def __str__(self) -> str:
        return f"[Inc: {self.id}]"
class ast_dec(ast_token_super):
    def __init__(self, id) -> None:
        self.id = id
        super().__init__()
    def __str__(self) -> str:
        return f"[Dec: {self.id}]"
# comparisons
class ast_and(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    def __str__(self) -> str:
        return f"[And: {self.left}, {self.right}]"
class ast_or(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    def __str__(self) -> str:
        return f"[Or: {self.left}, {self.right}]"
class ast_not(ast_token_super):
    def __init__(self, target) -> None:
        self.target = target
        super().__init__()
    def __str__(self) -> str:
        return f"[Not: {self.target}]"
class ast_g(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    def __str__(self) -> str:
        return f"[Greater: {self.left}, {self.right}]"
class ast_ge(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    def __str__(self) -> str:
        return f"[GreaterOrEqual: {self.left}, {self.right}]"
class ast_l(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    def __str__(self) -> str:
        return f"[Less: {self.left}, {self.right}]"
class ast_le(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    def __str__(self) -> str:
        return f"[LessOrEqual: {self.left}, {self.right}]"
class ast_equ(ast_token_super):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        super().__init__()
    def __str__(self) -> str:
        return f"[Equal: {self.left}, {self.right}]"
# assignments
class ast_assign(ast_token_super):
    def __init__(self, var, val) -> None:
        self.id = var
        self.value = val
        super().__init__()
    def __str__(self) -> str:
        return f"[Assign: {self.id}, {self.value}]"
class ast_assign_init(ast_token_super):
    def __init__(self, type, var, val) -> None:
        self.type = type
        self.id = var
        self.value = val
        super().__init__()
    def __str__(self) -> str:
        return f"[Assign: {self.type}, {self.id}, {self.value}]"
# return
class ast_ret(ast_token_super):
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()
    def __str__(self) -> str:
        return f"[Return: {self.value}]"
# function
class ast_func(ast_token_super):
    def __init__(self, type, name, perams, body) -> None:
        self.type = type
        self.name = name
        self.perams = perams
        self.body = body
        super().__init__()
    def __str__(self) -> str:
        return f"[Func: {self.type}, {self.name}]"
# peramteters
class ast_peram(ast_token_super):
    def __init__(self, type, id) -> None:
        self.type = type
        self.id = id
        super().__init__()
# call
class ast_call(ast_token_super):
    def __init__(self, id, perams) -> None:
        self.id = id
        self.perams = perams
        super().__init__()
    def __str__(self) -> str:
        return f"[Call: {self.id}, {self.perams}]"
# if statement
class ast_if(ast_token_super):
    def __init__(self, bodies) -> None:
        self.bodies = bodies
        super().__init__()
    
    def __str__(self) -> str:
        return f"[If: {len(self.bodies)}]"