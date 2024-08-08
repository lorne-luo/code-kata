# pytest configuration file
import sys
from pathlib import Path

ROOT_FOlDER = str(Path(__file__).parent.parent)

# resolve import error for pytest
sys.path.append(ROOT_FOlDER)
