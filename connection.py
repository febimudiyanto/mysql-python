# IP address dari server
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
