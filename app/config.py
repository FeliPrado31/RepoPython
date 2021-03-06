# Statement for enabling the development environment
import os
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Server Variables
MYSQL_ADDON_URI = 'mysql://uzrzxcidqtbg5y9p:FbTlSjxS5QB8aLuAjpcb@bydpsjw6ywkpffve7vfb-mysql.services.clever-cloud.com:3306/bydpsjw6ywkpffve7vfb'

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = MYSQL_ADDON_URI
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
UPLOADED_IMAGES_DEST = 'uploads/images'

UPLOAD_FOLDER = "public/img"
