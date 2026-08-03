from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

TOP_K = 3

API_TITLE = "Enterprise AI Gateway"

API_VERSION = "1.0.0"