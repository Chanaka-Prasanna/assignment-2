import os, shutil
from datetime import datetime

try:
    from colorama import init as colorama_init, Fore, Style
    colorama_init(autoreset=True)
    COLOR_ENABLED = True
except Exception:
    COLOR_ENABLED = False
    class _Dummy: 
        RESET_ALL = ""
    class _Fore(_Dummy):
        CYAN=GREEN=YELLOW=MAGENTA=BLUE=WHITE=RED=""
    class _Style(_Dummy):
        BRIGHT=""
    Fore, Style = _Fore(), _Style()

APP_NAME = "TaskMate Task Tracker"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def greeting():
    h = datetime.now().hour
    if h < 12: return "Good morning"
    if h < 18: return "Good afternoon"
    return "Good evening"

def banner_line(char: str, width: int) -> str:
    return char * width

def center_line(text: str, width: int) -> str:
    return text.center(width)

def print_banner(subtext: str = "",name: str = "there"):
    cols = max(60, shutil.get_terminal_size((80, 20)).columns) 
    title = f" {APP_NAME} "
    greet = f"{greeting()} {name}! {subtext}".strip()

    top    = "╔" + "═"*(cols-2) + "╗"
    bottom = "╚" + "═"*(cols-2) + "╝"

    # Calculate inner width (total width minus 2 border characters)
    inner_width = cols - 2

    # Title styling
    title_str = title.center(inner_width)
    if COLOR_ENABLED:
        title_str = Style.BRIGHT + Fore.CYAN + title_str + Style.RESET_ALL

    greet_str = greet.center(inner_width)
    if COLOR_ENABLED:
        greet_str = Fore.YELLOW + greet_str + Style.RESET_ALL

    print(top)
    print("║" + title_str + "║")
    print("║" + greet_str + "║")
    print(bottom)

def print_menu_header():
    cols = max(60, shutil.get_terminal_size((80, 20)).columns)
    line = "─" * (cols-2)
    if COLOR_ENABLED:
        line = Fore.BLUE + line + Style.RESET_ALL
    print("\n" + line)
    m = "1) Add  2) List  3) View  4) Update  5) Delete  6) Sort 7) Change name  0) Quit"
    print(center_line(m, cols))
    print(line)

def render_home(svc,user_name=None):
    name = user_name or "there"
    clear_screen()
    count = len(svc.list())
    print_banner(subtext=f"Tasks loaded: {count}",name=name)
    print_menu_header()