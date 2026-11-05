##  -- Program 9.1 List ---

# KUMPULAN DATA NUMBERS
data_angka = {1,5,2,3}
print (data_angka)

#KUMPULAN DATA STRING
data_string = ["Adit,Codot,Dottoreto"]
print (data_string)

# KUMPULAN DATA BOOLEAN
data_boolean = [True,False,True,True]
print (data_boolean)

# KUMPULAN CAMPURAN
data_campuran = [1,"Hirohito",2,"Stalin",True,"Hitler",False]
print (data_campuran)

# CARA ALTERNATIF MEMBUAT LIST
data_range = range (0,10,2) # range (start,stop,step)
print (data_range)
data_list = list (data_range)
print (data_list)

list_for = [i **2 for i in range(0,10)]
print(list_for)


# MEMBUAT LIST DENGAN FOR LOP,LIST COMPREHENSION
list_for_if = [ i for i in range(0,10) if i !=5]
print(list_for_if) 

list_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_for_if) 

list_for_if = [i for i in range(0,10) if i %2 != 0]
print(list_for_if) 

## --- Program 9.2 Manupulasi List --- 

# index 0(-3) 1(-2) 2(-1) 
data = ["Codot","Adit","Dottoreto"] 

data_0 = data[0]
print(f"data pertama (index 0) = {data_0}") 
data_terakhir = data [-1]
print (f"data terakhir adalah = {data_terakhir}")

panjang_data = len (data)
print (f"Jumlah Data = {panjang_data}")
# manipulasi data list 
 
print (f"data sebelum ditambah =\n{data}")

#data.insert(posisi,item) 
data.insert (1,"Efhan")
print (f"data ditambah lagi = \n {data}")

# menambah di akhir list 
data.append ("Faisal")
print (f"data ditambah lagi = \n {data}")

# menambahkan list dengan list 
data_baru = ["Ronar","Ali","Arjuna"]
data.extend (data_baru)
print (f"data gabungan  = \n{data}")

# menghapus data
data.remove ("Arjuna")
print (f"data hapus = \n {data}")

# merubah data
data[2] = "Kempis"
print(f"data rubah = \n{data}")

# menghapus data palimhbelakang
data.pop ()
print (f"data akhir = \n {data}")

## --- Program 9.3 Operasi List --- ##
# index 0(-3) 1(-2) 2(-1)
data_angka = [2,3,1,4]
print (f"data angka = \n{data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data
data = ["Faisal","Bagus","Irbat","Khafis"]
print(f"data = {data}")
index_Faisal = data.index("Faisal")
index_Bagus = data.index("Bagus")
print(f"index si Faisal = {index_Faisal}")
print(f"index si Bagus = {index_Bagus}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")
print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse \n{data_angka}")
print(f"data di reverse \n{data}")

## --- Program 9.4 Nested List --- ##

data_0 = [1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")
list_2D = [data_0, data_1, 6,7]
print(f"list 2D = {list_2D}")

# contoh penggunaan
peserta_1 = ["Azka", 19, "Laki-laki"]
peserta_2 = ["Nugi", 20, "Laki-laki"]
peserta_3 = ["Chika", 18, "wanita"]
list_peserta = [peserta_1, peserta_2, peserta_3]
print(f"peserta = {list_peserta}")
for peserta in list_peserta:
 print(f"nama\t : {peserta[0]}")
 print(f"umur\t : {peserta[1]}")
 print(f"Gender\t : {peserta[2]}\n")