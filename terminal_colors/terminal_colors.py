class Colors:
      def __init__(self, color, text):
          self.red = "\033[31m"
          self.green = "\033[32m"
          self.blue = "\033[34m"
          self.cyan = "\033[36m"
          self.purple = "\033[35m"
          self.reset = "\033[0m"
          self.pink = "\033[95m"

          self.bright = "\033[1m"
          self.background_green = "\033[42m"
          self.background_red = "\033[41m"
          self.blink = "\033[5m"
          self.sublime = "\033[4m"

          self.bg = f"{self.bright}{self.green}"
          self.br = f"{self.bright}{self.red}"
          self.bb = f"{self.bright}{self.blue}"
          self.bp = f"{self.bright}{self.purple}"

          self.ok = f"{self.bg}[OK]{self.reset} "
          self.error = f"{self.br}[ERROR]{self.reset} "
          self.check = f"{self.bp}[CHECK]{self.reset} "
          self.warning = f"{self.background_red}[WARN]{self.reset} "
          self.done = f"{self.bb}[END]{self.reset} "

      def __call__(self, color_flag, text):
          code_color = getattr(self, color_flag.lower(), self.reset)
          return f"{code_color}{text}{self.reset}"
