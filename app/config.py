import os

class Config:
  SECRET_KEY = os.environ.get("SECRET_KEY", "devkey")
  SQLALCHEMY_DATABASE_URI = os.environ.get(
  "DATABASE_URL",
  "sqlite:///xgram.db"
  )
  SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_FOLDER = "uploads"
MAX_CONTENT_LENGHT = 500 * 1024 * 1024 # 500 MB
