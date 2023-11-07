from rich.console import Console


class LogUtil:
    def __init__(self):
        self.info_console = Console(stderr=False, style="bold green")
        self.warn_console = Console(stderr=True, style="bold yellow")
        self.error_console = Console(stderr=True, style="bold red")

    def info(self, message):
        self.info_console.log(message)

    def warn(self, message):
        self.warn_console.log(message)

    def error(self, message):
        self.error_console.log(message)
