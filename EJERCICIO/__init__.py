###AÑADIDO PARA MYSQL
import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)  #sobreescribimos la sesion q nos pide
pymysql.install_as_MySQLdb()