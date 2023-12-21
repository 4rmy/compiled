import colorama

class Logger():
    OUTPUT = False
    out = None

    @staticmethod
    def setup(OUTPUT, out=None):
        Logger.OUTPUT = OUTPUT
        Logger.out = out

    @staticmethod
    def info(*args, **kwargs):
        msg = f"{colorama.Fore.CYAN}[HYPER]{colorama.Fore.RESET} "
        for a in args:
            msg += a + " "
        msg = msg[:-1]
        print(msg)
        if Logger.OUTPUT:
            print(msg, file=Logger.out)

    @staticmethod
    def warn(*args, **kwargs):
        msg = f"{colorama.Fore.YELLOW}[HYPER]{colorama.Fore.RESET} "
        for a in args:
            msg += a + " "
        msg = msg[:-1]
        print(msg)
        if Logger.OUTPUT:
            print(msg, file=Logger.out)

    @staticmethod
    def err(*args, **kwargs):
        msg = f"{colorama.Fore.RED}[HYPER]{colorama.Fore.RESET} "
        for a in args:
            msg += a + " "
        msg = msg[:-1]
        print(msg)
        if Logger.OUTPUT:
            print(msg, file=Logger.out)
        exit()
