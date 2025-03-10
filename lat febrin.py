class Orang:
    def __init__(self, Nama_depan, Nama_belakang, Nomer_ID):
        self.Nama_depan = Nama_depan
        self.Nama_belakang = Nama_belakang
        self.Nomer_ID = Nomer_ID
    def tampilkan_info(self):
        print(f"Nama Depan: {self.Nama_depan}")
        print(f"Nama Belakang: {self.Nama_belakang}")
        print(f"Nomor ID: {self.Nomer_ID}")

class Mahasiswa(Orang):
    SARJANA, MASTER, DOKTOR = range(3)
    gelar_jenjang = {"S1": "SARJANA", "S2":"MAGISTER", "S3":"DOKTOR"} 

    def __init__(self, Nama_depan, Nama_belakang, Nomer_ID, Jenjang):
        super().__init__(Nama_depan, Nama_belakang, Nomer_ID)
        self.Jenjang = Jenjang
        self.matkul = []  

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

    def tampilkan_info(self):
        print("Mahasiswa")
        print(f"Nama : {self.Nama_depan} {self.Nama_belakang}")
        if self.Jenjang == 0:
            print("Jenjang:", self.gelar_jenjang.get("S1"))
        elif self.Jenjang == 1:
            print("Jenjang:", self.gelar_jenjang.get("S2"))
        else: 
            print("Jenjang:", self.gelar_jenjang.get("S3"))
        print(f"Nomer_ID :{self.Nomer_ID}")
        print(f"Mata Kuliah: {', '.join(self.matkul) if self.matkul else 'Belum ada mata kuliah yang diambil'}")

class Karyawan(Orang):
    TETAP = "Tetap"
    TDK_TETAP = "Tidak Tetap"

    def __init__(self, nama_depan, nama_belakang, nomor_ID, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_ID)
        self.status_karyawan = status_karyawan
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Status Karyawan: {self.status_karyawan}")

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_ID, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_ID, status_karyawan)
        self.matkul_diajar = [] 
        
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Mata Kuliah yang Diajarkan: {', '.join(self.matkul_diajar) if self.matkul_diajar else 'Belum ada mata kuliah yang diajar'}")

bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
bowo.enrol("Basis Data")
bowo.tampilkan_info()

rizki = Dosen("Rizki", "Setiabudi", "456789", Karyawan.TETAP)
rizki.mengajar("Statistik")
rizki.tampilkan_info()

class Pelajar:
    def __init__(self):
        self.matkul = []  

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)  

    def tampilkan_matkul(self):
        if self.matkul:
            print("Mata Kuliah yang Diambil:")
            for mk in self.matkul:
                print(f"- {mk}")
        else:
            print("Belum ada mata kuliah yang diambil.")

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)
    def tampilkan_matkul_diajar(self):
        if self.matkul_diajar:
            print("Mata Kuliah yang Diajarkan:")
            for mk in self.matkul_diajar:
                print(f"- {mk}")
        else:
            print("Belum ada mata kuliah yang diajar.")

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, Nama_depan, Nama_belakang, Nomer_ID):
        super().__init__(Nama_depan, Nama_belakang, Nomer_ID)  
        Pelajar.__init__(self)  
        Pengajar.__init__(self) 
   
uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

uswatun.tampilkan_info()
uswatun.tampilkan_matkul()
uswatun.tampilkan_matkul_diajar()

