import ast
import os

GRUVBOX_COLORS = {
    "primary": "#427b58",
    "secondary": "#3c3836",
    "accent": "#d3869b",
    "dark": "#282828",
    "dark_page": "#282828",
    "positive": "#b5bd68",
    "negative": "#fb4934",
    "info": "#668cc0",
    "warning": "#f2c037",
}

STORAGE_SECRET = os.environ.get("STORAGE_SECRET", "NOSECRET")
RELOAD = ast.literal_eval(os.environ.get("RELOAD", "True").capitalize())
