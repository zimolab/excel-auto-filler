import enum
import string
from datetime import datetime

DEFAULT_BACKGROUND_COLOR = "#380C2A"
DEFAULT_FONT_SIZE = 16

COLOR_INFO = "#00FF00"
COLOR_DEBUG = "#FFFFFF"
COLOR_WARNING = "#FFFF00"
COLOR_CRITICAL = "#FF0000"
COLOR_FATAL = "#FF0000"

TERMINAL_STYLESHEET = """
QTextBrowser{
    background-color: ${bg_color}; 
    color: white; 
    font-size: ${font_size}px;
}
QScrollBar::vertical{
    background:transparent;
    width: 6px;
    margin: 0px;
 }
QScrollBar::handle:vertical{
    background-color:rgb(158,158,158);
    border: none;
    border-radius: 3px;
 }
QScrollBar::handle:vertical:pressed{
    background:#EC693C;
}
QScrollBar::sub-line:vertical{
    border:none;
}
QScrollBar::add-line:vertical{
    border:none;
}
QScrollBar::sub-page:vertical{
    border:none;
}
QScrollBar::add-page:vertical{
    border:none;
}
"""

COLORED_MSG_TPL = "<font color=%s><tt>%s</tt></font>"


class LogLevel(enum.Enum):
    INFO = 0
    DEBUG = 1
    WARNING = 2
    CRITICAL = 3
    FATAL = 4


def stylesheet(bg_color: str = DEFAULT_BACKGROUND_COLOR, font_size: int = DEFAULT_FONT_SIZE):
    return string.Template(TERMINAL_STYLESHEET).substitute(bg_color=bg_color, font_size=font_size)


def message(msg: str, color: str) -> str:
    return COLORED_MSG_TPL % (color, msg)


def log(level: LogLevel, msg: str, timestamp: bool = False, timestamp_format: str = "%Y-%m-%d %H:%M:%S",
        additional_nl: bool = False) -> str:
    if level == LogLevel.INFO:
        msg = message(msg, COLOR_INFO)
    elif level == LogLevel.DEBUG:
        msg = message(msg, COLOR_DEBUG)
    elif level == LogLevel.WARNING:
        msg = message(msg, COLOR_WARNING)
    elif level == LogLevel.CRITICAL:
        msg = message(msg, COLOR_CRITICAL)
    elif level == LogLevel.FATAL:
        msg = message(msg, COLOR_FATAL)
    else:
        pass
    if timestamp:
        timestamp_str = datetime.now().strftime(timestamp_format)
        msg = f"[{timestamp_str}] {msg}"
    if additional_nl:
        msg += "<br>"

    return msg
