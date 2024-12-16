import os
import sys


def resource_path(relative_path):
    """Get the absolute path to a resource, works for dev and PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base_path, relative_path)
