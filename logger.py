import logging


logging.basicConfig(level=logging.INFO)

main_logger = logging.getLogger("main")

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log.txt')

console_handler.setFormatter(logging.Formatter("%(levelname)s : %(asctime)s : %(message)s"))
file_handler.setFormatter(logging.Formatter("%(levelname)s : %(asctime)s : %(message)s"))

main_logger.addHandler(console_handler)
main_logger.addHandler(file_handler)
