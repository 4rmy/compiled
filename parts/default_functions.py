class Builtins:
    @staticmethod
    def print(args):
        message = ""
        for a in args:
            message += str(a) + " "
        print(message[:-1])