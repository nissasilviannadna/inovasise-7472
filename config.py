"""
Konfigurasi untuk Facebook Scraper
Silakan sesuaikan nilai-nilai sesuai kebutuhan Anda
"""
import os
from dotenv import load_dotenv

# Load environment variables dari .env file
load_dotenv()

# === KONFIGURASI FACEBOOK ===
FACEBOOK_URL = "https://www.facebook.com/"
TARGET_GROUP_URL = os.getenv(
    "TARGET_GROUP_URL", 
    "https://www.facebook.com/groups/BaubauJualBeli"
)

# === KONFIGURASI CHROME/CHROMIUM ===
USER_DATA_DIR = os.path.join(os.getcwd(), "fb_session")
BROWSER_CHANNEL = "chrome"  # Use installed Chrome for better stability on Windows
HEADLESS_MODE = True
BROWSER_TIMEOUT = 120000  # ms - Increased untuk FB yang heavy
PAGE_LOAD_TIMEOUT = 120000  # ms - Increased dari 60000 untuk stabilitas

# Browser arguments untuk stabilitas.
# Hindari flag yang berisiko membuat browser tidak stabil.
BROWSER_ARGS = [
    # "--disable-dev-shm-usage",  # REMOVE - cause crash pada Windows
    # "--no-sandbox",              # REMOVE - unnecessary dan problematic
    # "--disable-gpu",             # REMOVE - Facebook needs GPU
    "--disable-extensions",
    "--disable-plugins",
    "--disable-sync",
    # "--disable-software-rasterizer",
    # "--force-device-scale-factor=1",
    "--disable-default-apps",
    "--disable-breakpad",
    "--disable-background-networking",
    "--window-size=1280,800"
    "--force-color-profile=srgb",
    "--disable-features=DarkMode",
    "--blink-settings=primaryHoverType=2,primaryPointerType=4", # Membantu stabilitas elemen
]

VIEWPORT = {"width": 1280, "height": 800}

# === KONFIGURASI MODE RINGAN ===
# Mengurangi beban render agar tidak mudah "Aw Snap" pada halaman berat.
LIGHTWEIGHT_MODE = False
# BLOCK_RESOURCE_TYPES = ["image", "media", "font"]
BLOCK_RESOURCE_TYPES = []

# === KONFIGURASI SCRAPING ===
NUM_SCROLLS = 100
SCROLL_DEPTH = 2000  # pixel - Reduced dari 3000 untuk stabilitas (less aggressive)
SCROLL_WAIT_TIME = 50000  # ms - INCREASED dari 3000 untuk browser recovery
GROUP_LIST_SCROLLS = 10  # Kurangi waktu tunggu saat mengambil daftar grup
MAX_GROUPS_TO_PROCESS = 8  # Batasi jumlah grup agar proses tidak terasa stuck

# Selector untuk mencari artikel
# ARTICLE_SELECTOR = 'div[role="article"]'
ARTICLE_SELECTOR = 'div[data-ad-comet-preview="message"]'
# ARTICLE_SELECTOR = 'div.x1y1aw1k.xwib8y2'
MAIN_CONTENT_SELECTOR = 'div[role="main"]'

# === KONFIGURASI DELAY & RETRY ===
SLOW_MO = 500  # INCREASED dari 300 - lebih gentle untuk browser (ms)
MAX_RETRIES = 5  # INCREASED dari 3 - lebih banyak retry attempts
RETRY_WAIT = 8000  # INCREASED - beri browser lebih banyak waktu recover (ms)
ESCAPE_KEY_DELAY = 1000  # INCREASED dari 500 untuk popup handling (ms)

# === KONFIGURASI DATA EXTRACTION ===
# Regex patterns untuk ekstraksi data
WHATSAPP_PATTERN = r'(?:\+62|0)\s?(?:8[1-9])\d{7,11}'  # Improved WhatsApp pattern
PRICE_PATTERN = r'(?:Rp\.?|IDR)\s?[\d.,]+'
TEXT_SUMMARY_LENGTH = 250

# Keywords untuk filtering post
REQUIRED_KEYWORDS = []

# === KONFIGURASI DATABASE SPASIAL ===
KECAMATAN_REF = {
    "Betoambari": {"kab": "Baubau", "lat": -5.5144, "lng": 122.5852},
    "Murhum": {"kab": "Baubau", "lat": -5.4746, "lng": 122.6105},
    "Batupoaro": {"kab": "Baubau", "lat": -5.4627, "lng": 122.6015},
    "Wolio": {"kab": "Baubau", "lat": -5.4645, "lng": 122.6158},
    "Kokalukuna": {"kab": "Baubau", "lat": -5.4425, "lng": 122.6321},
    "Bungi": {"kab": "Baubau", "lat": -5.3992, "lng": 122.6825},
    "Lea-Lea": {"kab": "Baubau", "lat": -5.3524, "lng": 122.6874},
    "Sorawolio": {"kab": "Baubau", "lat": -5.5003, "lng": 122.6715}
}

# === KONFIGURASI LOGGING ===
LOG_FILENAME = "fb_scraper.log"
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - [%(funcName)s] - %(message)s"

# === KONFIGURASI OUTPUT ===
OUTPUT_FORMAT = "csv"  # csv atau excel
OUTPUT_DIR = os.getcwd()

# === KONFIGURASI SECURITY ===
# Untuk credentials, gunakan environment variables:
# FACEBOOK_EMAIL atau FACEBOOK_USERNAME
# FACEBOOK_PASSWORD
# Jangan hardcode credentials di file ini!
USE_CREDENTIALS_FILE = False  # Jika True, baca dari .env
CREDENTIALS_FILE = ".env"

async def get_credentials():
    """Get credentials dari .env atau input user"""
    email = os.getenv('FB_EMAIL')
    password = os.getenv('FB_PASSWORD')
    
    if not email or not password:
        email = input("📧 Masukkan email Facebook: ").strip()
        password = input("🔐 Masukkan password Facebook: ").strip()
    
    return {"email": email, "password": password}
