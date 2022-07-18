class LocalConfig:

    # Подключение Б/Д Database
    SQLALCHEMY_DATABASE_URI  = 'mysql://root:root@localhost/users' #mysql://login:password
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False