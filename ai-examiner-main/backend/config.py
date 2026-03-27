import os
from dotenv import load_dotenv

# Load .env
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()


class Config:
    # 🔑 API
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    # 📂 FILES
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', os.path.join(BASE_DIR, 'uploads'))
    MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 16 * 1024 * 1024))
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

    # 🗄️ DATABASE
    MONGO_URI = os.getenv('MONGO_URI')
    MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'ai_examiner')

    # 📄 POPPLER (🔥 IMPORTANT)
    POPPLER_PATH = os.getenv('POPPLER_PATH')

    # ✅ FILE CHECK
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

    # ✅ VALIDATION
    @staticmethod
    def validate():
        if not Config.GEMINI_API_KEY:
            raise Exception("GEMINI_API_KEY is missing")

        if not Config.MONGO_URI:
            raise Exception("MONGO_URI is missing")

    # ✅ INIT
    @staticmethod
    def init_app():
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER)