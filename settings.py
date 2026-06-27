# Файл с общими настройками проекта
from pathlib import Path

BASE_DIR = Path(__file__).parent
TRANSLATIONS_DIR = BASE_DIR / 'languages'
HOME_DIR = Path.home()
SCREEN_SIZE = None

# macOS: ~/Library/Application Support/ModTranslationHelper/
# Windows fallback: ~/Documents/ModTranslationHelper/
APP_SUPPORT_DIR = HOME_DIR / 'Library' / 'Application Support' / 'ModTranslationHelper'

PROGRAM_VERSION = '1.4.3'
