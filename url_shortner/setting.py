import os
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # SQLALCHEMY toolkit for communicate with database
SQLALCHEMY_TRACK_NOTIFICATIONS = False # A configuration to enable or disable tracking modifications of objects. 
                                       # You set it to False to disable tracking and use less memory.
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')

