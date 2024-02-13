# MODULE 1 CAPSTONE PROJEK PURWADHIKA
# Membuat Program CRUD (Create, Read, Update, Delete)

# Data awal
data = {
    "akmaldzaki" : {
        "ID" : "A1",
        "Nama Lengkap" : "Akmal Dzaki",
        "Jenis Kelamin" : "Pria",
        "Kota" : "Mataram",
        "Pekerjaan" : "Mahasiswa",
        "Peminjaman" : {
            "Buku 1" : {
                "Judul Buku" : "Matematika Dasar", 
                "Tanggal Pinjam" : "21 Agustus 2022", 
                "Tanggal Kembali" : "28 Agustus 2022"
            },
            "Buku 2": {
                "Judul Buku" : "Fisika Dasar",
                "Tanggal Pinjam" : "13 Juni 2022",
                "Tanggal Kembali" : "20 Juni 2022"
            }
        }
    } 
}

# Fungsi untuk SECTION #1
def biodata(data):
    """
    Fungsi untuk menampilkan Biodata Anggota
    Arg :
        data = Data Collection tipe Dictionary

    return : -
    """

    if len(data) == 0:
        print("Tidak Ada Anggota")
    else:
        for key in data.keys():
            print(f"""
            ID\t\t\t:{data[key]['ID']}
            Nama Lengkap\t:{data[key]['Nama Lengkap']}
            Jenis Kelamin\t:{data[key]['Jenis Kelamin']}
            Kota\t\t:{data[key]['Kota']}
            Pekerjaan\t\t:{data[key]['Pekerjaan']}
            """)
    return data

def peminjaman(data):
    """
    Fungsi untuk menampilkan Buku Pinjaman Anggota
    Arg :
        data = Data Collection tipe Dictionary

    return : -
    """
    
    id = input("Masukkan ID Anggota : ").upper()

    list_id = []
    for key1 in data.keys():
        if data[key1]['ID'] == id:
            print(f"Nama Anggota : {data[key1]['Nama Lengkap']}")
            temp = data[key1]["Peminjaman"]
            if len(temp) == 0:
                print("Tidak Ada Pinjaman Buku")
            else:
                for key2 in temp.keys():
                    print(f"""
                    Judul Buku\t\t:{temp[key2]['Judul Buku']}
                    Tanggal Pinjam\t:{temp[key2]['Tanggal Pinjam']}
                    Tanggal Kembali\t:{temp[key2]['Tanggal Kembali']}
                    """)
        list_id.append(data[key1]['ID'])
    if id not in list_id:
        print("ID Tidak Ditemukan")
        
    return data

# Fungsi untuk SECTION #2
def add_bio(data):
    """
    Fungsi untuk menambahkan anggota baru
    Arg : 
        data = Data Collection tipe Dictionary

    return : -
    """

    name_check = input("Masukkan Nama Lengkap : ")
    check = name_check.replace(" ", "")
    if check.lower() not in data.keys():
        n = len(data)
        id = f"A{n+1}"
        print(f"Anggota Baru akan ditambahkan dengan ID : {id}")
		
        # new_id = input("Masukkan ID : ")
        # new_name = input("Masukkan Nama Lengkap : ")
        new_gender = input("Masukkan Jenis Kelamin : ")
        new_kota = input("Masukkan Kota : ")
        new_job = input("Masukkan Pekerjaan : ")

        confirm = input("Data akan ditambahkan ? (Y/N): ").lower()
        if confirm == "y":
            data[check.lower()] = {
                "ID" : id,
                "Nama Lengkap" : name_check,
                "Jenis Kelamin" : new_gender,
                "Kota" : new_kota,
                "Pekerjaan" : new_job,
                "Peminjaman" : {}
            }
            print("Data Berhasil Ditambahkan.")
        else:
            print("Data Tidak Jadi Ditambahkan")
    else:
        print("Data Sudah Ada !")
    return data
		
def add_buku(data):
    """
    Fungsi untuk menambahkan buku pinjaman baru
    Arg : 
        data = Data Collection tipe Dictionary

    return : -
    """

    id = input("Masukkan ID Anggota : ").upper()
    list_id = []
    for key1 in data.keys():
        if data[key1]['ID'] == id:
            print(data[key1]['Nama Lengkap']+'\n')
            temp = data[key1]["Peminjaman"]

            # data buku yang akan dipinjam
            new_title = input("Masukkan Judul Buku : ")
            go_date = input("Masukkan Tanggal Peminjaman : ")
            in_date = input("Masukkan Tanggal Kembali : ")
            confirm = input("Apakah buku akan dipinjamkan ? (Y/N) : ").lower()

            if confirm == "y":
                n = len(temp)
                temp[f"Buku {n+1}"] = {
                    "Judul Buku" : new_title,
                    "Tanggal Pinjam" : go_date,
                    "Tanggal Kembali" : in_date
                }
            else:
                print("Buku Tidak Jadi Dipinjamkan")
        list_id.append(data[key1]['ID'])
    if id not in list_id:
        print("ID Tidak Ditemukan")
    return data

# Fungsi untuk SECTION #3
def update_bio(data):
    """
    Fungsi untuk mengupdate biodata anggota.
	Arg :
	    data = Dictionary Collection Data Type
		
	return : data
    """
    
    id = input("Masukkan ID Anggota : ").upper()
    for key in data.keys():
        if data[key]['ID'] == id:
            print(f"Data {data[key]['Nama Lengkap']} akan dirubah")
            confirm = input("Apakah anda yakin ? (Y/N) : ").lower()
            if confirm == "y":
                while True:
                    print("""
                    Ingin update apa ? :
                    1. Nama Lengkap.
                    2. Jenis Kelamin.
                    3. Kota
                    4. Pekerjaan
                    """)
                    akses = input("Masukkan input : ")
                    if akses == str(1):
                        new_name = input("Nama Lengkap yang Baru : ")
                        confirm = input("Apakah anda yakin untuk mengubahnya? (Y/N) : ").lower()
                        if confirm == "y":
                            data[key]['Nama Lengkap'] = new_name
                            print("Nama Lengkap Telah Diperbaharui")
                            break
                        else:
                            print("Nama Lengkap Tidak Jadi Diperbaharui")
                            break
                    elif akses == str(2):
                        new_gender = input("Jenis Kelamin yang Baru : ")
                        confirm = input("Apakah anda yakin untuk mengubahnya? (Y/N) : ").lower()
                        if confirm == "y":
                            data[key]['Jenis Kelamin'] = new_gender
                            print("Jenis Kelamin Telah Diperbaharui")
                            break
                        else:
                            print("Jenis Kelamin Tidak Jadi Diperbaharui")
                            break
                    elif akses == str(3):
                        new_kota = input("Kota yang Baru : ")
                        confirm = input("Apakah anda yakin untuk mengubahnya? (Y/N) : ").lower()
                        if confirm == "y":
                            data[key]['Kota'] = new_kota
                            print("Kota Telah Diperbaharui")
                            break
                        else:
                            print("Kota Tidak Jadi Diperbaharui")
                            break
                    elif akses == str(4):
                        new_job = input("Pekerjaan yang Baru : ")
                        confirm = input("Apakah anda yakin untuk mengubahnya? (Y/N) : ").lower()
                        if confirm == "y":
                            data[key]['Pekerjaan'] = new_job
                            print("Pekerjaan Telah Diperbaharui")
                            break
                        else:
                            print("Pekerjaan Tidak Jadi Diperbaharui")
                            break
                    else:
                        print("Menu Tidak Ada")
                        break
            else:
                print("Ternyata anda tidak yakin")

    return data

def update_buku(data):
    """
    Fungsi untuk mengupdate buku pinjaman
    Arg : 
        data = Data Collection tipe Dictionary

    return : data
    """

    id = input("Masukkan ID Anggota : ").upper()
    list_id = []
    for key in data.keys():
        if data[key]['ID'] == id:
            print(f"Data Peminjaman Buku {data[key]['Nama Lengkap']} akan dirubah.")
            confirm = input("Apakah anda yakin ? (Y/N) : ").lower()
            temp = data[key]["Peminjaman"]            
            if confirm == "y":
                print(f"""
                    {data[key]['Nama Lengkap']} memiliki {len(temp)} pinjaman buku.
                    Buku Mana yang ingin anda rubah?
                    """)
                for i in range(len(temp)):
                    print(f"{i+1}. Buku_{i+1} dengan judul {temp[f'Buku {i+1}']['Judul Buku']}")
                inp = input("Masukkan Judul Buku yang Ingin Anda Rubah : ").lower()
                # list_inp = []
                for key1 in temp.keys():
                    if temp[key1]['Judul Buku'].lower() == inp:
                        while True:
                                print("""
                                Ingin update apa ? :
                                1. Judul Buku.
                                2. Tanggal Pinjam.
                                3. Tanggal Kembali.
                                """)
                                akses = input("Masukkan input : ")
                                if akses == str(1):
                                    new_title = input("Judul Buku yang Baru : ")
                                    confirm = input("Apakah anda yakin untuk mengubahnya? (Y/N) : ").lower()
                                    if confirm == "y":
                                        temp[key1]['Judul Buku'] = new_title
                                        print("Judul Buku Telah Diperbaharui")
                                        break
                                    else:
                                        print("Judul Buku Tidak Jadi Diperbaharui")
                                        break
                                elif akses == str(2):
                                    new_in_date = input("Tanggal Pinjam yang Baru : ")
                                    confirm = input("Apakah anda yakin untuk mengubahnya? (Y/N) : ").lower()
                                    if confirm == "y":
                                        temp[key1]['Tanggal Pinjam'] = new_in_date
                                        print("Tanggal Pinjam Telah Diperbaharui")
                                        break
                                    else:
                                        print("Tanggal Pinjam Tidak Jadi Diperbaharui")
                                        break
                                elif akses == str(3):
                                    new_out_date = input("Tanggal Kembali yang Baru : ")
                                    confirm = input("Apakah anda yakin untuk mengubahnya? (Y/N) : ").lower()
                                    if confirm == "y":
                                        temp[key1]['Tanggal Kembali'] = new_out_date
                                        print("Tanggal Kembali Telah Diperbaharui")
                                        break
                                    else:
                                        print("Tanggal Kembali Jadi Diperbaharui")
                                        break
                                else:
                                    print("Menu Tidak Ada")
                                    break
                    #list_inp.append(temp[key1]['Judul Buku'])
                #if inp not in list_inp:
                    #print("Judul Buku Tidak Ditemukan")
            else:
                print("Ternyata anda tidak yakin")
        list_id.append(data[key]['ID'])
    if id not in list_id:
        print("ID Tidak Ditemukan")
    return data


# Fungsi untuk SECTION #4
def delete_bio(data):
    """
    Fungsi untuk menghapus data pinjaman buku anggota.
    Arg : 
        data = Dictionary Collection Data Type
    
    return : data
    """
    
    id = input("Masukkan ID Anggota : ").upper()
    for key in list(data.keys()):
        if len(data[key]) == 0:
            print("Data Kosong")
        elif data[key]['ID'] == id:
            print(f"""
            Anggota Dengan ID : {id}, Bernama : {data[key]['Nama Lengkap']}.
            Tindakan ini akan menghapus histori data beserta data pinjaman bukunya. 
            """)
            confirm = input("Apakah Anda Yakin Untuk Menghapusnya? (Y/N) : ").lower()
            if confirm == "y":
                del data[key]
                print("Data Berhasil Dihapus")
            else:
                print("Data Tidak Jadi Dihapus")
    return data

def delete_buku(data):
    """
    Fungsi untuk menghapus data pinjaman buku anggota.
    Arg : 
        data = Dictionary Collection Data Type
    
    return : data
    """

    id = input("Masukkan ID Anggota : ").upper()
    for key in data.keys():
        if data[key]['ID'] == id:
            print(f"Data Peminjaman Buku {data[key]['Nama Lengkap']} akan dihapus.")
            confirm = input("Apakah anda yakin ? (Y/N) : ").lower()
            temp = data[key]["Peminjaman"] 
            if confirm == "y":
                print(f"""
                    {data[key]['Nama Lengkap']} memiliki {len(temp)} pinjaman buku.
                    Buku Mana yang ingin anda hapus?
                    """)
                for i in range(len(temp)):
                    print(f"{i+1}. Buku_{i+1} dengan judul {temp[f'Buku {i+1}']['Judul Buku']}")
                inp = input("Masukkan Judul Buku yang Ingin Anda Rubah : ").lower()
                for key1 in list(temp.keys()):
                    if temp[key1]['Judul Buku'].lower() == inp:
                        print(f"Data Pinjaman Buku {temp[key1]['Judul Buku']} berhasil dihapus.")
                        del temp[key1] 
            else:
                print("Data Pinjaman Buku Tidak Jadi Dihapus.")
    return data

		
# MAIN PROGRAM
while True:
	print("""
	=====Data Peminjaman Anggota Perpustakaan=====
	1. Report Data Anggota.
	2. Menambahkan Data Anggota.
	3. Mengubah Data Anggota.
	4. Menghapus Data Anggota.
	5. Exit
	""")
	akses = input("Akses Menu Utama [1-5] : ")
	
	# SECTION 1 : Report Data Anggota.
	if akses == str(1):
		while True:
			print(
			"""
			==Report Data Anggota==
			1. Report Biodata Anggota.
			2. Report Peminjaman Buku Anggota.
			3. Kembali ke Menu Utama.
			"""
			)
			akses1 = input("Menu Report Data Anggota [1-3] : ")
			if akses1 == str(1):
				data = biodata(data)
				data
			elif akses1 == str(2):
				data = peminjaman(data)
				data
			elif akses1 == str(3):
				break
			else:
				print("Menu Tidak Ditemukan")
		
	
	# SECTION 2 : Menambah Data Anggota.
	elif akses == str(2):
		while True:
			print(
			"""
			==Menambahkan Data Anggota==
			1. Menambahkan Anggota Baru.
			2. Menambah Buku Pinjaman Anggota.
			3. Kembali ke Menu Utama.
			"""
			)
			akses2 = input("Menu Menambahkan Data Anggota [1-3] : ")
			if akses2 == str(1):
				data = add_bio(data)
				data
			elif akses2 == str(2):
				data = add_buku(data)
				data
			elif akses2 == str(3):
				break
			else:
				print("Menu Tidak Ditemukan")
	
	# SECTION 3 : Edit Data Anggota.
	elif akses == str(3):
		while True:
			print(
			"""
			==Update Data Anggota==
			1. Update Biodata Anggota.
			2. Update Data Buku Pinjaman Anggota.
			3. Kembali ke Menu Utama.
			"""
			)
			akses3 = input("Menu Update Data Anggota [1-3] : ")
			if akses3 == str(1):
			    data = update_bio(data)
			    data
			elif akses3 == str(2):
				data = update_buku(data)
				data
			elif akses3 == str(3):
				break
			else:
				print("Menu Tidak Ditemukan")
		
	# SECTION 4 : Menghapus Data Anggota
	elif akses == str(4):
		while True:
			print(
			"""
			==Menghapus Data Anggota==
			1. Menghapus Data Anggota.
			2. Menghapus Data Pinjaman Anggota.
			3. Kembali ke Menu Utama.
			"""
			)
			akses4 = input("Menu Menambahkan Data Anggota [1-3] : ")
			if akses4 == str(1):
				data = delete_bio(data)
				data
			elif akses4 == str(2):
				data = delete_buku(data)
				data
			elif akses4 == str(3):
				break
			else:
				print("Menu Tidak Ditemukan")
		
	# SECTION 5 : Exit Program.
	elif akses == str(5):
		break
	
	# SECTION 6.
	else:
		print("Masukkan Nomor Akses yang Benar")
	