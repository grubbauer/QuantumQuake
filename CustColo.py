def debug(arg):
    import colorama
    colorama.init()
    print(f"{colorama.Fore.CYAN}DEBUG: {arg}")

def info(arg):
    import colorama
    colorama.init()
    print(f"{colorama.Fore.GREEN}INFO: {arg}")

def warning(arg):
    import colorama
    colorama.init()
    print(f"{colorama.Fore.YELLOW}WARNING: {arg}")

def error(arg):
    import colorama
    colorama.init()
    print(f"{colorama.Fore.MAGENTA}ERROR: {arg}")

def critical(arg):
    import colorama
    colorama.init()
    print(f"{colorama.Fore.RED}CRITICAL: {arg}")