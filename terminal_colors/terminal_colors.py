class Colors:
    def __init__(self):
        self.black = "\033[30m"
        self.red = "\033[31m"
        self.green = "\033[32m"
        self.yellow = "\033[33m"
        self.blue = "\033[34m"
        self.purple = "\033[35m"
        self.cyan = "\033[36m"
        self.white = "\033[37m"

        self.bright_black = "\033[90m"
        self.bright_red = "\033[91m"
        self.bright_green = "\033[92m"
        self.bright_yellow = "\033[93m"
        self.bright_blue = "\033[94m"
        self.bright_purple = "\033[95m"
        self.bright_cyan = "\033[96m"
        self.bright_white = "\033[97m"

        self.background_black = "\033[40m"
        self.background_red = "\033[41m"
        self.background_green = "\033[42m"
        self.background_yellow = "\033[43m"
        self.background_blue = "\033[44m"
        self.background_purple = "\033[45m"
        self.background_cyan = "\033[46m"
        self.background_white = "\033[47m"

        self.background_bright_black = "\033[100m"
        self.background_bright_red = "\033[101m"
        self.background_bright_green = "\033[102m"
        self.background_bright_yellow = "\033[103m"
        self.background_bright_blue = "\033[104m"
        self.background_bright_purple = "\033[105m"
        self.background_bright_cyan = "\033[106m"
        self.background_bright_white = "\033[107m"

        self.reset = "\033[0m"
        self.bright = "\033[1m"
        self.dim = "\033[2m"
        self.italic = "\033[3m"
        self.sublime = "\033[4m"
        self.blink = "\033[5m"
        self.reverse = "\033[7m"
        self.hidden = "\033[8m"
        self.strike = "\033[9m"

        self.pink = self.bright_purple

        self.by = f"{self.bright}{self.yellow}"
        self.bg = f"{self.bright}{self.green}"
        self.br = f"{self.bright}{self.red}"
        self.bb = f"{self.bright}{self.blue}"
        self.bp = f"{self.bright}{self.purple}"

        senf.trying = f"{self.by}[TRYING]{self.reset} "
        self.ok = f"{self.bg}[OK]{self.reset} "
        self.error = f"{self.br}[ERROR]{self.reset} "
        self.check = f"{self.bp}[CHECK]{self.reset} "
        self.warning = f"{self.background_red}[WARN]{self.reset} "
        self.done = f"{self.bb}[END]{self.reset} "

    def __call__(self, color_flag, text):
        code_color = getattr(self, color_flag.lower(), self.reset)
        return f"{code_color}{text}{self.reset}"
