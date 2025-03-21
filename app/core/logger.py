from loguru import logger
import sys

# Remove default logger
logger.remove()

# Add console logger
logger.add(
    sys.stdout,
    format="{time} | {level} | {message}",
    level="INFO",
    colorize=True
)

# Add file logger [Rotating logs, JSON Format]
logger.add(
    "logs/app.log",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    level="INFO",
    serialize=True
)

def get_logger():
    return logger