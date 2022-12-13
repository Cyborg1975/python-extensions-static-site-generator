import sys
import importlib
from pathlib import Path

def load_module(directory, name):
    sys.path.insert(directory, 0)
    import_module(name)
    sys.path.pop(0)
