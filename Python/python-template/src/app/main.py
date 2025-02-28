from src.util.logging.logger import Logger
from src.util.logging.logging_config import setup_logging
import logging


def main() -> str:
    setup_logging()
    logger = Logger(__name__, level=logging.DEBUG)
    logger.log_data(
        logging.INFO,
        data_id="123",
        service="main",
        caller="src/app/main.py",
        request_uri="/",
        message="main function was called",
    )
    return "main"


if __name__ == "__main__":
    main()
