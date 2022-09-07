from UrlHaus.DatabaseConnection import connection, cursor

query = "CREATE TABLE IF NOT EXISTS a ("
query += "id           INTEGER       PRIMARY KEY,"
query += "dateaddded   DATETIME,"
query += "url          VARCHAR (255),"
query += "ip_address   VARCHAR (255),"
query += "port         INTEGER,"
query += "url_status   VARCHAR (255),"
query += "last_online  VARCHAR (255),"
query += "threat       VARCHAR (255),"
query += "tags         VARCHAR (255),"
query += "urlhaus_link VARCHAR (255),"
query += "reporter     VARCHAR (255));"
cursor.execute(query)
connection.commit