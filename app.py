import os
import time

doctor_list = [
    "[1] Dr. John Doe (Pukul 07:00 - 12:00 WIB)",
    "[2] Dr. Jane Smith (Pukul 13:00 - 18:00 WIB)",
    "[3] Dr. Michael Johnson (Pukul 19:00 - 23:59 WIB)",
    "[4] Dr. Sarah Williams (Pukul 00:00 - 05:00 WIB)"
]

doctor_specialist = [
    "[1] Dr. Lisa Davis (Spesialis Jantung)",
    "[2] Dr. Robert Lee (Spesialis Bedah)",
    "[3] Dr. Emily Brown (Spesialis Gigi)"
]

doctor_generalist = [
    "[1] Dr. David Wilson (Senin - Rabu)",
    "[2] Dr. Jennifer Taylor (Kamis - Jum'at)",
    "[3] Dr. Daniel Anderson (Sabtu - Minggu)"
]

def program():
    exit_input = "5"
    user_input = ""

    patient_name = date_birth = address = contact = illness = ""
    total_expenses = 0

    while user_input != exit_input:
        os.system("cls")
        print("==========================================================")
        print("#    Selamat Datang di Program Rumah Sakit Statistika    #")
        print("==========================================================")
        print("Pilih Daftar Menu Untuk Mengakses Program :\n")
        print("[1] Registrasi Pasien")
        print("[2] Pemilihan Dokter")
        print("[3] Pemilihan Rawat")
        print("[4] Pembayaran")
        print("[5] Keluar\n")
        user_input = input("Masukkan Pilihan Menu: ")

        if user_input == "1":
            exit_registration_option = "y"
            registration_option = ""

            while registration_option != exit_registration_option:
                os.system("cls")
                patient_name = input("Masukkan Nama Pasien: ")
                date_birth = input("Masukkan Tempat Tanggal Lahir Pasien: ")
                address = input("Masukkan Alamat Pasien: ")
                contact = input("Masukkan Kontak Pasien: ")
                illness = input("Masukkan Penyakit Pasien: ")

                os.system("cls")
                print(f"Nama Pasien: {patient_name}")
                print(f"Tempat, Tanggal Lahir: {date_birth}")
                print(f"Alamat: {address}")
                print(f"Kontak: {contact}")
                print(f"Penyakit: {illness}")

                registration_option = input("\nLanjut? (y/n) ")

        if user_input == "2":
            exit_select_doctor_option = "4"
            select_doctor = ""

            while select_doctor != exit_select_doctor_option:
                os.system("cls")
                print("Daftar Pilihan Jenis Dokter: ")
                print("1: Semua Dokter")
                print("2: Dokter Spesialis")
                print("3: Dokter Umum")
                print("4: Kembali")
                select_doctor = input("\nPilih Jenis Dokter: ")

                if select_doctor == "1":
                    exit_select_doctor_all = "5"
                    select_doctor_all = ""

                    os.system("cls")
                    print("Daftar Dokter:")
                    for doctor in doctor_list:
                        print(doctor)
                    print("[5] Kembali")

                    select_doctor_all = input("Pilih Dokter: ")

                    while select_doctor_all != exit_select_doctor_all:
                        if select_doctor_all == "1":
                            os.system("cls")
                            print(f"Anda Telah Memilih {doctor_list[0]}")
                            time.sleep(2.5)
                            select_doctor_all = exit_select_doctor_all
                        if select_doctor_all == "2":
                            os.system("cls")
                            print(f"Anda Telah Memilih {doctor_list[1]}")
                            time.sleep(2.5)
                            select_doctor_all = exit_select_doctor_all
                        if select_doctor_all == "3":
                            os.system("cls")
                            print(f"Anda Telah Memilih {doctor_list[2]}")
                            time.sleep(2.5)
                            select_doctor_all = exit_select_doctor_all
                        if select_doctor_all == "4":
                            os.system("cls")
                            print(f"Anda Telah Memilih {doctor_list[3]}")
                            time.sleep(2.5)
                            select_doctor_all = exit_select_doctor_all

                if select_doctor == "2":
                    exit_select_doctor_specialist = "4"
                    select_doctor_specialist = ""

                    os.system("cls")
                    print("Daftar Dokter Spesialis:")
                    for doctor in doctor_specialist:
                        print(doctor)
                    print("[4] Kembali")

                    select_doctor_specialist = input("Pilih Dokter: ")

                    while select_doctor_specialist != exit_select_doctor_specialist:
                        if select_doctor_specialist == "1":
                            os.system("cls")
                            print(f"Anda Telah Memilih {doctor_specialist[0]}")
                            time.sleep(2.5)
                            select_doctor_specialist = exit_select_doctor_specialist
                        elif select_doctor_specialist == "2":
                            os.system("cls")
                            print(f"Anda Telah Memilih {doctor_specialist[1]}")
                            time.sleep(2.5)
                            select_doctor_specialist = exit_select_doctor_specialist
                        elif select_doctor_specialist == "3":
                            os.system("cls")
                            print(f"Anda Telah Memilih {doctor_specialist[2]}")
                            time.sleep(2.5)
                            select_doctor_specialist = exit_select_doctor_specialist

                if select_doctor == "3":
                    exit_select_doctor_generalist = "4"
                    select_doctor_generalist = ""

                    os.system("cls")
                    print("Daftar Dokter Umum:")
                    for doctor in doctor_generalist:
                        print(doctor)
                    print("[4] Kembali")

                    select_doctor_generalist = input("Pilih Dokter: ")

                    while select_doctor_generalist != exit_select_doctor_generalist:
                        if select_doctor_generalist == "1":
                            os.system("cls")
                            print(f"Anda Telah Memilih {doctor_generalist[0]}")
                            time.sleep(2.5)
                            select_doctor_generalist = exit_select_doctor_generalist
                        elif select_doctor_generalist == "2":
                            os.system("cls")
                            print(f"Anda Telah Memilih {doctor_generalist[1]}")
                            time.sleep(2.5)
                            select_doctor_generalist = exit_select_doctor_generalist
                        elif select_doctor_generalist == "3":
                            os.system("cls")
                            print(f"Anda Telah Memilih {doctor_generalist[2]}")
                            time.sleep(2.5)
                            select_doctor_generalist = exit_select_doctor_generalist

        if user_input == "3":
            exit_search = "0"
            search_patient = ""

            os.system("cls")
            print('0: Kembali')
            search_patient = input("Cari Pasien berdasarkan nama: ")

            while search_patient != exit_search:
                if search_patient == patient_name:
                    exit_treatment = "3"
                    treatment = ""

                    os.system("cls")
                    print("Daftar Pilihan Jenis Perawatan: ")
                    print("1: Rawat Inap")
                    print("2: Rawat Jalan")
                    print("3: Kembali")
                    treatment = input("\nPilih Jenis Perawatan: ")

                    while treatment != exit_treatment:
                        if treatment == "1":
                            os.system("cls")
                            treatment_day_count = int(input("Jumlah hari rawat inap yang diinginkan: "))
                            print(f"Pasien dipilih untuk rawat inap selama {treatment_day_count} hari")
                            cost_per_day = 100000
                            total_expenses = cost_per_day * treatment_day_count
                            print(f"Total biaya rawat inap selama {treatment_day_count} hari: {total_expenses}")

                            print("\n\nPilihan:")
                            print("0: Keluar")
                            print("1: Kembali")

                            user_input_treatment = input("\n> ")

                            if user_input_treatment == "0":
                                treatment = exit_treatment
                                search_patient = exit_search

                            if user_input_treatment == "1":
                                treatment = exit_treatment

                        if treatment == "2":
                            os.system("cls")
                            print("Pasien Dipilih Untuk Rawat Jalan.")
                            outpatient_cost = 50000
                            total_expenses = outpatient_cost
                            print(f"Biaya rawat jalan: {total_expenses}")

                            print("\n\nPilihan:")
                            print("0: Keluar")
                            print("1: Kembali")

                            user_input_treatment = input("\n> ")

                            if user_input_treatment == "0":
                                treatment = exit_treatment
                                search_patient = exit_search

                            if user_input_treatment == "1":
                                treatment = exit_treatment
                else:
                    print("Data tidak ditemukan...")
                    time.sleep(1.5)

                    search_patient = exit_search
        if user_input == "4":
            os.system("cls")
            print("==========================================================")
            print("#    Selamat Datang di Program Pembayaran Rumah Sakit    #")
            print("==========================================================")
            print(f"Total Tagihan untuk Pasien {patient_name}: {total_expenses}")
            user_input_payment = input("\n> ")

            if user_input_payment == "0":
                user_input = exit_input

            if user_input_payment == "1":
                os.system("cls")
                print("Pembayaran Anda Berhasil Dilakukan.")
                time.sleep(2.5)
                user_input = exit_input

    os.system("cls")
    print("Terima kasih telah menggunakan program Rumah Sakit Statistika.")

program()
