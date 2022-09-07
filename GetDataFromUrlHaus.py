import csv
from datetime import datetime
import time
from UrlHaus.DatabaseConnection import connection, cursor
import socket


# get every existing ID in database
def get_existed_id(id_lst):
    cursor.execute("select id from url_hause_data")
    for row in cursor:
        for field in row:
            id_lst.append(field)
    id_lst = map(str, id_lst)
    id_lst = list(id_lst)
    return id_lst


# open CSV file and return a list of information
def open_csv(information):
    file = open("data.csv")
    csvreader = csv.reader(file)
    for row in csvreader:
        information.append(row)
    del information[0:9]
    return information

#ping get ip from domain name
def get_ip_from_domain_name(domain_name):
    try:
        host_ip = socket.gethostbyname(domain_name)
        return host_ip
    except:
        return domain_name

#get ip and port number from url
def get_ip_port(url):
    url_information = url.split("/")
    ip_information = url_information[2]
    ip_information = ip_information.split(":")
    if len(ip_information) == 1:
        protocol = url_information[0]
        protocol = protocol.strip(":")
        if protocol == "https":
            port = "443"
        elif protocol == "http":
            port = "80"
        else:
            port = "null"
        ip_information = [get_ip_from_domain_name(ip_information[0]), port]
        return ip_information
    elif len(ip_information) == 2:
        return ip_information

def create_table():
    query = "CREATE TABLE IF NOT EXISTS url_hause_data ("
    query += "id           INTEGER       PRIMARY KEY,"
    query += "dateadded   DATETIME,"
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

# up list information to database
def update_database(information, existed_id):
    for line in information:
        id = line[0]
        dateadded = line[1]
        url = line[2]
        url_status = line[3]
        last_online = line[4]
        threat = line[5]
        tags = line[6]
        urlhaus_link = line[7]
        reporter = line[8]
        id_port_list = get_ip_port(url)
        ip_address = id_port_list[0]
        port = id_port_list[1]
        # check whether if ID already existed
        if id not in existed_id:
            query = "insert into url_hause_data (id, dateadded, url, ip_address, port, url_status, last_online, threat, tags, urlhaus_link, reporter) values ("
            query += id + ", datetime('" + dateadded + "'), '"
            query += url + "', '" + ip_address + "', " + port + ", '" + url_status + "', '"
            query += last_online + "', '" + threat + "', '"
            query += tags + "', '" + urlhaus_link + "', '" + reporter + "');"
            cursor.execute(query)
        connection.commit()

# Main function
if __name__=="__main__":
    while True:
        create_table()
        information = []
        existed_id = []
        update_database(open_csv(information), get_existed_id(existed_id))
        now = datetime.now()
        now = now.strftime("%Y/%m/%d, %H:%M:%S")
        print(now)
        time.sleep(86400)