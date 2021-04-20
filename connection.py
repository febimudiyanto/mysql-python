# IP address dari server

'''
untuk terkoneksi dengan mysql secara remote, bisa digunakan command berikut:
mysql -u python-user -h <ip> -P <port> -p
> masukkan passwordnya


* insert

INSERT INTO table_name VALUES (column1_value, column2_value, column3_value, ...);

INSERT INTO logins(username, password) VALUES('administrator', 'adm1n_p@ss');

INSERT INTO logins(username, password) VALUES ('john', 'john123!'), ('tom', 'tom123!');

* ALTER

ALTER TABLE logins ADD newColumn INT;

ALTER TABLE logins RENAME COLUMN newColumn TO oldColumn;

ALTER TABLE logins MODIFY oldColumn DATE;

ALTER TABLE logins DROP oldColumn;

* Update

UPDATE table_name SET column1=newvalue1, column2=newvalue2, ... WHERE <condition>;
UPDATE logins SET password = 'change_password' WHERE id > 1;



'''
HOST = "192.168.122.176"
DATABASE = "data_db"
USER = "python-user"
PASSWORD = "inirahasia"

# Cek koneksi database
db_connect = mysql.connect(host=HOST, user=USER, passwd = PASSWORD)
if db_connect:
    print("koneksi sukses")
else:
    print("koneksi gagal")

# Inisialisasi cursor()
mycursor = db_connect.cursor()

# Menampilkan database
mycursor.execute("Show databases")
#print(type(mycursor))
nama_db=DATABASE
lst=[]
for db in mycursor:
    #mendapatkan list dari database
    lst.append(db[0]) 
    print(db[0])

# cek dan buat database
if nama_db in lst:     
    print("database",nama_db,"sudah ada")                              
else:                                                                  
    print(">database tidak ada")                                       
    mycursor.execute("create database if not exists "+nama_db)         
    print("  >>>database",nama_db,"sudah dibuat")                      
                                                                       
mycursor.execute("use "+nama_db)                                       
                                                                       
                                                                       
for db in mycursor:                                                    
    print(db[0])
