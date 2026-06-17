from pathlib import Path
from dotenv import load_dotenv
import os

# cargar .env
load_dotenv()

# ==========
# RUTA RAÍZ
# ==========

ROOT_PATH = Path(__file__).resolve().parents[2]

# ==========
# DATA
# ==========

DATA_PATH = ROOT_PATH / "data"

LEYES_PATH = DATA_PATH / "leyes"

REPORTES_PATH = DATA_PATH / "reportes_pdf"

PROCESADOS_PATH = DATA_PATH / "procesados"

# ==========
# CHROMA
# ==========

CHROMA_PATH = ROOT_PATH / "chroma_db"

CHROMA_COLLECTION = "seguridad_yucatan"

# ==========
# MODELOS IA
# ==========

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "qwen2.5:1.5b"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "all-MiniLM-L6-v2"
)

TOP_K_RESULTS = int(
    os.getenv("TOP_K_RESULTS", 2)
)

# ==========
# MYSQL
# ==========

MYSQL_HOST = os.getenv("MYSQL_HOST")

MYSQL_USER = os.getenv("MYSQL_USER")

MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

MYSQL_DB = os.getenv("MYSQL_DB")

MYSQL_PORT = os.getenv("MYSQL_PORT", 3307)