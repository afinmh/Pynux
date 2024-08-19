from datetime import datetime
from colorama import init, Fore
import time
import sys

init()
logo = f"""{Fore.LIGHTCYAN_EX}
                ██████╗ ██╗   ██╗███╗   ██╗██╗   ██╗██╗  ██╗
                ██╔══██╗╚██╗ ██╔╝████╗  ██║██║   ██║╚██╗██╔╝
                ██████╔╝ ╚████╔╝ ██╔██╗ ██║██║   ██║ ╚███╔╝ 
                ██╔═══╝   ╚██╔╝  ██║╚██╗██║██║   ██║ ██╔██╗ 
                ██║        ██║   ██║ ╚████║╚██████╔╝██╔╝ ██╗
                ╚═╝        ╚═╝   ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ 
                       Simulation System Operation     {Fore.RESET}                                   
"""
status = 0
params = ''
kode = 'root'
root = {
    'tanggal': ['20/11/2020', '21/11/2020', '22/11/2020', '24/11/2020', '25/11/2020', '26/11/2020', '27/11/2020'],
    'jam': ['13:30', '14:25', '15:45', '16:30', '18:00', '19:45', '20:30'],
    'jenis': ['<DIR>', '<DIR>', '<DIR>', '<DIR>', '<DIR>', '<DIR>', '<DIR>'],
    'size': [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    'nama': ['Download', 'Music', 'Pictures', '.conf', '.etc', '.lib', '.boot']
}

download = {
    'tanggal': ['20/12/2020', '30/12/2020', '1/1/2021', '15/2/2021', '8/3/2021', '20/4/2021', '5/5/2021'],
    'jam': ['11:30', '09:25', '14:45', '10:20', '12:30', '18:15', '21:00'],
    'jenis': [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    'size': ['2.738', '88.237', '1024', '2048', '4096', '8192', '16384'],
    'nama': ['text.txt', 'tugas.pdf', 'rangkuman.docx', 'presentation.pptx', 'data.xlsx', 'code.py', 'image.png']
}

music = {
    'tanggal': ['20/12/2020', '30/12/2020', '1/1/2021', '15/2/2021', '8/3/2021', '20/4/2021', '5/5/2021'],
    'jam': ['11:30', '09:25', '14:45', '10:20', '12:30', '18:15', '21:00'],
    'jenis': [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    'size': ['2.738', '88.237', '2048', '4096', '8192', '16384', '32768'],
    'nama': ['jedagjedugnonstop.mp3', 'djpalpalepalpale.mp3', '123.mp3', 'djangkot.mp3', 'tarikmang.mp3', 'djistridua.mp3', 'srepet.mp3']
}

pictures = {
    'tanggal': ['10/1/2022', '15/2/2022', '20/3/2022', '25/4/2022', '30/5/2022'],
    'jam': ['08:30', '12:45', '15:20', '18:10', '22:00'],
    'jenis': [' ', ' ', ' ', ' ', ' '],
    'size': ['512', '1024', '2048', '4096', '8192'],
    'nama': ['landscape.jpg', 'portrait.png', 'vacation.jpg', 'family_photo.jpeg', 'sunset.png']
}

help = {
    ' dir': 'Untuk melihat direktori saat ini',
    ' dir name_file': 'Membuka Direktori yang dituju',
    ' mkdir name_file': 'Membuat Direktori baru',
    ' cd': 'kembali ke Direktori',
    ' rm name_file': 'Menghapus Direktori',
    ' logout': 'Keluar dari akun',
    ' cla': 'Membersihkan Layar',
    ' perm': 'Memberikan Keterangan terkait izin atau proteksi file',
    ' date': 'Menampilkan tanggal saat ini',
    ' time': 'Menampilkan waktu atau jam saat ini',
    ' checkdiv': 'Melakukan identifikasi atau testing apakah perangkat tersedia dan bekerja'
}

helplogin_info = {
    ' login': 'Perintah untuk masuk ke halaman login',
    ' shutdown': 'Untuk keluar dari perangkat',
    ' cla': 'Untuk membersihkan terminal',
    ' user': 'Memberikan informasi terkait akun',
    ' logo': 'Menampilkan Logo',
    ' date': 'Menampilkan tanggal saat ini',
    ' time': 'Menampilkan waktu atau jam saat ini'
}

checkdiv_info = {
    ' checkdiv': 'Harus menggunakan paramater, dan berikut parameternya',
    ' contoh':'checkdiv all',
    ' all': 'Melakukan pengujian untuk semua perangkat keras',
    ' memory': 'Melakukan pengujian untuk memory atau RAM',
    ' output': 'Melakukan pengujian untuk perangkat output',
    ' input': 'Melakukan pengujian untuk perangkat input',
    ' graphic': 'Melakukan pengujian untuk memory grafis',
    ' storage': 'Melakukan pengujian untuk penyimpanan',
}

hardware = {
    "Memory": "Corsair Vengeance LPX 16GB DDR4 3200MHz (DDR4)",
    "Storage": "SSD0: Samsung 970 EVO 500GB",
    "Graphics": "NVIDIA GeForce GTX 1660 Ti",
    "Input Devices": {
        "Keyboard": "Logitech G512 CarbonIDX",
        "Mouse": "Logitech G520 Hero",
        "Microphone": "Blue Yeti USB Microphone"
    },
    "Output Devices": {
        "Display": "ASUS VG279Q",
        "Speaker": "Logitech Z623 2.1 Channel Speaker System"
    }
}

userlogin_info = {
    ' Akun Login': 'Username: kelompok5, Password: 1234',
}

def proses(main_text, additional_text=""):
    for percentage in range(101):
        if percentage < 100:
            print(f"\r{main_text} {percentage}% {additional_text}", end='', flush=True)
            time.sleep(0.05)
        else:
            print(f"\r{main_text}               OK {additional_text}", end='', flush=True)
    print()

def print_with_delay(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

input(" Tekan Enter untuk Menyalakan Komputer:")
# Intro
print()
main_text = " Checking Hardware Connections"
print_with_delay(main_text, 0.3)
proses(main_text)
print_with_delay(" All hardware connections secure", 0.05)
time.sleep(0.8)
print()
print()
print()
print(f" {Fore.YELLOW}   =================================================================== ")
print(f"    -------------------- Power On Self Test (POST) -------------------- ")
print(f"    =================================================================== {Fore.RESET}")
print()
print()
print()
main_text = " Post Started:      "
print_with_delay(main_text, 0.1)
print()
print()
main_text = '  Checking Memory:  '
print_with_delay(main_text, 0.05)
print()
main_text = '   Dual-Channel Memory:     '
print_with_delay(main_text, 0.05)
time.sleep(0.3)
print()
main_text = '    Channel 1:      16384MB '
print_with_delay(main_text, 0.05)
proses(main_text)
main_text = '    Channel 2:          0MB '
print_with_delay(main_text, 0.05)
proses(main_text)
main_text = '   Total Memory:    16384MB '
print_with_delay(main_text, 0.05)
print()
print()
main_text = '  Checking Storage:         '
print_with_delay(main_text, 0.05)
print()
main_text = '   Storage:         SSD0: Samsung 970 EVO 500GB '
print_with_delay(main_text, 0.05)
proses(main_text)
print()
main_text = '  Checking Input Devices:   '
print_with_delay(main_text, 0.05)
print()
main_text = '   Keyboard:        Logitech G512 CarbonIDX     '
print_with_delay(main_text, 0.05)
proses(main_text)
main_text = '   Mouse:           Logitech G520 Hero          '
print_with_delay(main_text, 0.05)
proses(main_text)
main_text = '   Microphone:      Blue Yeti USB Microphone    '
print_with_delay(main_text, 0.05)
proses(main_text)
main_text = '  Checking Output Devices:  '
print_with_delay(main_text, 0.05)
print()
main_text = '   Monitor:         ASUS VG270Q                 '
print_with_delay(main_text, 0.05)
proses(main_text)
main_text = '   Speaker:         Logitech Z623               '
print_with_delay(main_text, 0.05)
proses(main_text)
time.sleep(5)
print('\n' * 50)
print('\033[H')
print(f" {Fore.YELLOW}   =================================================================== ")
print(f"    ----------------------- All Hardware Data ------------------------ ")
print(f"    =================================================================== {Fore.RESET}")
time.sleep(5)
print()
print()
print("  Processor:        Intel(R) Core(TM) i7-11700 @ 2.50GHz")
print("  Motherboard:      ASUS Prime H510M-E")
print("  Graphics:         NVIDIA GeForce GTX 1660 Ti")
print("  Memory:           Corsair Vengeance LPX 16GB DDR4 3200MHz (DDR4)")
print("  Storage:          SSD0: Samsung 970 EVO 500GB")
print("  Power Supply:     Corsair RM650x 650W")
print("  Input Devices:    Keyboard: Logitech G512 CarbonIDX")
print("                    Mouse: Logitech G520 Hero")
print("                    Microphone: Blue Yeti USB Microphone")
print("  Output Devices:   ASUS VG279Q")
print("                    Speaker: Logitech Z623 2.1 Channel Speaker System")
print()
print()
print()
time.sleep(1)
print(f"{Fore.YELLOW}    =================================================================== ")
print(f"    ----------------------- UEFI Initialization ----------------------- ")
print(f"    =================================================================== {Fore.RESET}")
time.sleep(0.8)
print()
print()
time.sleep(0.8)
main_text = '  UEFI Firmware Version: 3.0.2'
print_with_delay(main_text, 0.05)
print()
main_text = '  UEFI Revision:        2.1'
print_with_delay(main_text, 0.05)
print()
print()
main_text = '  Boot Order:'
print_with_delay(main_text, 0.05)
time.sleep(0.3)
print()
main_text = '  1. SSD0: Samsung 970 EVO 500GB'
print_with_delay(main_text, 0.05)
print()
print()
time.sleep(1)
print(f"{Fore.YELLOW}    =================================================================== ")
print(f"    ------------------Loading Operating System: PYNUX------------------ ")
print(f"    =================================================================== {Fore.RESET}")
time.sleep(5)
print('\n' * 75)
print('\033[H') 
print("  PYNUX Loading...")
time.sleep(0.1)
print(" .")
time.sleep(0.1)
print(" .")
time.sleep(0.1)
print(" .")
time.sleep(0.1)
print(" .")
time.sleep(0.1)
print(" .")
time.sleep(0.1)
time.sleep(0.4)
main_text = ' Loading PYNUX Kernel          '
print_with_delay(main_text, 0.05)
proses(main_text)
main_text = ' Initializing System Services  '
print_with_delay(main_text, 0.05)
proses(main_text)
main_text = ' Configuring Drivers           '
print_with_delay(main_text, 0.05)
proses(main_text)
main_text = ' Setting Up Network            '
print_with_delay(main_text, 0.05)
proses(main_text)
main_text = ' Loading User Profiles         '
print_with_delay(main_text, 0.05)
proses(main_text)
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
main_text = ' Now loading please wait       '
print_with_delay(main_text, 0.05)
proses(main_text)
time.sleep(1)
print('\n' * 50)
print('\033[H') 
print(" All complete! Wellcome... ")


 #====================================================SHELL========================================================
def check(device, category):
    if category == "Keyboard":
        print("\nInput Devices:")
    elif category == "Display":
        print("\nOutput Devices:")

    print(f" {category}:")
    for percentage in range(1, 101):
        print(f"\r  {device} {percentage}%", end='', flush=True)
        time.sleep(0.05)
    print(" OK")

def get_access_message():
    return (
        " Direktori tidak bisa diakses semua, hanya Direktori Home, Download, Music, dan Pictures\n"
        " direktori baru yang dibuat dengan mkdir tidak bisa diakses user karena secara otomatis permission untuk user hanya r\n"
        " ataupun bila dijabarkan untuk permission secara default pada program ini sebagai berikut\n"
        " rwxr--   Karena OS masih dalam tahap pengembangan\n"
        " 3 digit diawal adalah permission untuk admin atau root, dan 3 digit setelahnya adalah permission untuk user\n"
        " 3 digit awal rwx yang menandakan admin memiliki kendali penuh\n"
        " 3 digit selanjutnya r-- menandakan user hanya bisa read saja\n"
    )

def checkdiv(b):
    category_to_check = ""
    if b == '':
        for command, description in checkdiv_info.items():
            print(f"{command.ljust(20)} : {description}")
        print()
    elif b == 'all':
        for category, details in hardware.items():
            if isinstance(details, dict):  # Jika itu adalah dictionary
                for sub_category, sub_details in details.items():
                    check(sub_details, sub_category)  # Panggil fungsi check untuk setiap perangkat
            else:
                check(details, category)  # Panggil fungsi check untuk perangkat
                print()
    elif b == 'memory':
        category_to_check = 'Memory'
        category_to_check = 'Storage'
        if category_to_check in hardware:
            check(hardware[category_to_check], category_to_check)
            print()
    elif b == 'graphic':
        category_to_check = 'Graphics'
        category_to_check = 'Storage'
        if category_to_check in hardware:
            check(hardware[category_to_check], category_to_check)
            print()
    elif b == 'storage':
        category_to_check = 'Storage'
        if category_to_check in hardware:
            check(hardware[category_to_check], category_to_check)
            print()
    elif b == 'input':
        category_to_check = 'Input Devices'
        if category_to_check in hardware:
            devices_to_check = hardware[category_to_check]
            if isinstance(devices_to_check, dict):
                for device_category, device_details in devices_to_check.items():
                    check(device_details, device_category)
                    print()
            else:
                check(devices_to_check, category_to_check)
                print()
    elif b == 'output':
        category_to_check = 'Output Devices'
        if category_to_check in hardware:
            devices_to_check = hardware[category_to_check]
            if isinstance(devices_to_check, dict):
                for device_category, device_details in devices_to_check.items():
                    check(device_details, device_category)
            else:
                check(devices_to_check, category_to_check)
                print()
    else:
        print(f"{b} tidak didefinisikan sebagai perintah.")
        print()

def get_current_datetime():
    now = datetime.now()
    return now.strftime('%d/%m/%Y'), now.strftime('%H:%M')

def tampil(c):
    for i in range(len(c['tanggal'])):
       print(" {:<15} {:<10} {:<10} {:<10} {:<15}".format(
        c['tanggal'][i],
        c['jam'][i],
        c['jenis'][i],
        c['size'][i],
        c['nama'][i]
    ))

def lihat_dir(b):
    global params 
    global kode
    if b == '' and kode == 'root':
        kode = 'root'
        print()
        tampil(root)
    elif (b == 'Download' and params == '') or (b == '' and kode == 'download'):
        print()
        tampil(download)
        params = '\Download'  
        kode = 'download' 
    elif (b == 'Music' and params == '') or (b == '' and kode == 'music'):
        params = '\Music' 
        kode = 'music'
        print()
        tampil(music)
    elif (b == 'Pictures' and params == '') or (b == '' and kode == 'pictures'):
        params = '\Pictures' 
        kode = 'pictures'
        print()
        tampil(pictures)
    elif b in root['nama'] and b not in ['Download', 'Music', 'Pictures']:
        print(f" User tidak memiliki ijin mengakses Direktori {b} ")
    elif b in download['nama']:
        print(f" User tidak memiliki ijin mengakses Direktori {b} ")
    elif b in music['nama']:
        print(f" User tidak memiliki ijin mengakses Direktori {b} ")
    elif b in pictures['nama']:
        print(f" User tidak memiliki ijin mengakses Direktori {b} ")
    else:
        print(" Direktori Tidak Tersedia")
        print()
        return 
    print()

def rm(b):
    global kode
    if kode == 'root':
        if b == '.conf':
            print(f" Direktori {b} merupakan folder system, sehingga tidak dapat dihapus user")
        elif b == '.etc':
            print(f" Direktori {b} merupakan folder system, sehingga tidak dapat dihapus user")
        elif b == '.lib':
            print(f" Direktori {b} merupakan folder system, sehingga tidak dapat dihapus user")
        elif b == '.boot':
            print(f" Direktori {b} merupakan folder system, sehingga tidak dapat dihapus user")
        else:
            nama_to_remove = b
            index_to_remove = None
            for i, nama in enumerate(root['nama']):
                if nama == nama_to_remove:
                    index_to_remove = i
                    break
            if index_to_remove is not None:
                for key in root.keys():
                    del root[key][index_to_remove]
                print(" Berhasil menghapus direktori!")
            else:
                print(" Direktori tidak ditemukan.")
        print()
    elif kode == 'download':
        nama_to_remove = b
        index_to_remove = None
        for i, nama in enumerate(download['nama']):
            if nama == nama_to_remove:
                index_to_remove = i
                break
        if index_to_remove is not None:
            for key in download.keys():
                del download[key][index_to_remove]
            print(" Berhasil menghapus direktori!")
        else:
            print(" Direktori tidak ditemukan.")
        print()
    elif kode == 'music':
        nama_to_remove = b
        index_to_remove = None
        for i, nama in enumerate(music['nama']):
            if nama == nama_to_remove:
                index_to_remove = i
                break
        if index_to_remove is not None:
            for key in music.keys():
                del music[key][index_to_remove]
            print(" Berhasil menghapus direktori!")
        else:
            print(" Direktori tidak ditemukan.")
        print()
    elif kode == 'pictures':
        nama_to_remove = b
        index_to_remove = None
        for i, nama in enumerate(pictures['nama']):
            if nama == nama_to_remove:
                index_to_remove = i
                break
        if index_to_remove is not None:
            for key in pictures.keys():
                del pictures[key][index_to_remove]
            print(" Berhasil menghapus direktori!")
        else:
            print(" Direktori tidak ditemukan.")
        print()


def mkdir(b):
    global kode
    input_data = {
        'tanggal': get_current_datetime()[0],
        'jam': get_current_datetime()[1],
        'jenis': '<DIR>',
        'size': ' ',
        'nama': b
    }   
    if kode == 'root':
        for key, value in input_data.items():
            root[key].append(value)
    elif kode == 'download':
        for key, value in input_data.items():
            download[key].append(value)
    elif kode == 'music':
        for key, value in input_data.items():
            music[key].append(value)
    elif kode == 'pictures':
        for key, value in input_data.items():
            pictures[key].append(value)
    print(" Berhasil membuat direktori baru")
    print()

def cd():
    global kode
    global params
    params = ''
    kode = 'root'

def cla():
    print('\n' * 75)
    print('\033[H') 

def login():
    global status
    username = input(" Username: ")
    password = input(" Password: ")
    if cekakun(username, password):
        print(" Login berhasil!")
        print()
        status +=1
    else:
        print(" Akun tidak terdaftar, silahkan ketik user untuk melihat info seputar akun")
        print()

def cekakun(username, password):
    return username == 'kelompok5' and password == '1234'

def ket():
    print(get_access_message())

def show_help(commands):
    for command, description in commands.items():
        print(f"{command.ljust(20)} : {description}")

def show_helplogin():
    for command, description in helplogin_info.items():
        print(f"{command.ljust(20)} : {description}")

def show_userlogin():
    for category, info in userlogin_info.items():
        print(f"{category.ljust(20)} : {info}")

print(logo)
def status0():
    global status
    while status == 0:
        log = input(f"{Fore.YELLOW} C:\\User>{Fore.RESET}")
        if log.lower() == 'login':
            login()
        elif log.lower() == 'shutdown':
            status += 2
        elif log.lower() == 'help':
            show_helplogin()
            print()
        elif log.lower() == 'cla':
            cla()
        elif log.lower() == 'user':
            show_userlogin()
            print()
        elif log.lower() == 'logo':
            print(logo)
            print()
        elif log.lower() == 'date':
            print(f" Tanggal hari ini: {get_current_datetime()[0]}")
            print()
        elif log.lower() == 'time':
            print(f" Waktu saat ini: {get_current_datetime()[1]}")
            print()
        else:
            print(" Akses ditolak, silahkan login terlebih dahulu atau ketik help")
            print()

def status1():
    global status
    while status == 1:
        cmd = input(rf" {Fore.YELLOW}C:\Users\kelompok5{params}{Fore.RESET}> ")
        user = cmd.split()
        a = user[0].lower()

        if len(user) > 1:
            b = user[1]
        else:
            b = ''  # Atau bisa juga diatur sesuai kebutuhan, misalnya b = ''

        if a == 'dir':
            lihat_dir(b)
        elif a == 'help':
            show_help(help)
            print()
        elif a == 'cd':
            cd()
        elif a == 'mkdir':
            mkdir(b)
        elif a == 'logout':
            status = 0
            print(" Keluar Akun")
            print()
        elif a == 'rm':
            rm(b)
        elif a == 'cla':
            cla()
        elif a == 'perm':
            ket()
            print()
        elif a == 'logo': 
            print(logo)
            print()
        elif a == 'shutdown':
            status += 1
        elif a == 'date':
            print(f" Tanggal hari ini: {get_current_datetime()[0]}")
            print()
        elif a == 'time':
            print(f" Waktu saat ini: {get_current_datetime()[1]}")
            print()
        elif a == 'checkdiv':
            checkdiv(b)
        else:
            print(f" '{a}' tidak didefinisikan sebagai perintah")
            print()
        

while True:
    status0()
    status1()
    if status == 2:
        print(" Mematikan Komputer...")
        print()
        break

