SECRET_KEY = 'you-will-never-guess'
DEBUG=True
DB_USERNAME = 'root'
DB_PASSWORD = 'test'
BLOG_DATABASE_NAME = 'cb'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@mysql:3306/%s' % (DB_USERNAME, DB_PASSWORD, BLOG_DATABASE_NAME)
UPLOADED_IMAGES_DEST = '/opt/chef_browser/static/images'
UPLOADED_IMAGES_URL = '/static/images/'