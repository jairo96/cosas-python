

class style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    
    CURSIVE = '\033[3m'
    UNDERLINE = '\033[4m'
    BOLD = "\033[1m"
    END = '\033[0m'


def printColor(text, type, fin='', line = ''):
    result = {
        'title': lambda text:  print(style.MAGENTA + style.BOLD + text + style.END,end=fin),
        'subtitle': lambda text:  print(style.OKCYAN + text + f"(Line {line})" + style.END,end=fin),
        'text': lambda text:  print(text,end=fin),
        'code': lambda text:  print(style.YELLOW + style.CURSIVE + text + style.END,end=fin),
        'result': lambda text:  print(style.OKGREEN + text + style.END,end=fin),
        'line': lambda text: print("This is line 5, python says line ", cf.f_lineno ),
        # 'titulo': lambda text:  cprint(text, 'red', 'on_cyan'),
        # 'titulo': lambda text:  cprint(text, 'red', 'on_cyan'),
        # 'titulo': lambda text:  cprint(text, 'red', 'on_cyan'),
        # 'titulo': lambda text:  cprint(text, 'red', 'on_cyan'),
        # 'titulo': lambda text:  cprint(text, 'red', 'on_cyan'),
    }[type](text)