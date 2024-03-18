import os
from prettytable import PrettyTable

class PC:
    def __init__(self, pc_name, motherboard, processor, vga, ram, ssd, psu, casing):
        self.pc_name = pc_name
        self.motherboard = motherboard
        self.processor = processor
        self.vga = vga
        self.ram = ram
        self.ssd = ssd
        self.psu = psu
        self.casing = casing
        self.next = None

    def calculate_total_price(self):
        return (self.motherboard["price"] +
                self.processor["price"] +
                self.vga["price"] +
                self.ram["price"] +
                self.ssd["price"] +
                self.psu["price"] +
                self.casing["price"])

class RakitPc:
    def __init__(self):
        self.head = None
        self.available_components = {
            "motherboard": {
                "MSI B450": 150,
                "ASUS ROG Strix X570": 250,
                "Gigabyte B550": 200,
                "ASRock Z590": 300,
                "MSI MAG B550 TOMAHAWK": 180,
                "ASUS TUF Gaming B550-PLUS": 190,
                "GIGABYTE B550 AORUS PRO": 220,
                "ASRock B550M Steel Legend": 180,
                "ASUS PRIME B550M-A": 170,
                "MSI MPG B550 GAMING EDGE WIFI": 210
            },
            "processor": {
                "AMD Ryzen 5 5600X": 300,
                "AMD Ryzen 9 5900X": 600,
                "Intel Core i7-11700K": 400,
                "Intel Core i9-11900K": 500,
                "AMD Ryzen 7 5800X": 450,
                "AMD Ryzen 9 5950X": 700,
                "Intel Core i5-11600K": 350,
                "Intel Core i9-10900K": 550,
                "AMD Ryzen 5 3600": 250,
                "Intel Core i5-10600K": 300
            },
            "vga": {
                "NVIDIA GeForce RTX 3070": 500,
                "NVIDIA GeForce RTX 3080": 700,
                "AMD Radeon RX 6800 XT": 600,
                "NVIDIA GeForce RTX 3090": 1000,
                "NVIDIA GeForce RTX 3060 Ti": 400,
                "AMD Radeon RX 6900 XT": 800,
                "NVIDIA GeForce RTX 3060": 350,
                "AMD Radeon RX 6700 XT": 550,
                "NVIDIA GeForce RTX 3050 Ti": 300,
                "AMD Radeon RX 6600 XT": 400
            },
            "ram": {
                "16GB DDR4": 100,
                "32GB DDR4": 200,
                "64GB DDR4": 400,
                "128GB DDR4": 800,
                "8GB DDR4": 80,
                "16GB DDR4 RGB": 120,
                "32GB DDR4 RGB": 240,
                "64GB DDR4 RGB": 480,
                "16GB DDR4 3600MHz": 150,
                "32GB DDR4 3600MHz": 300
            },
            "ssd": {
                "500GB NVMe SSD": 80,
                "1TB NVMe SSD": 120,
                "2TB NVMe SSD": 200,
                "4TB NVMe SSD": 400,
                "250GB NVMe SSD": 60,
                "2TB SATA SSD": 150,
                "4TB SATA SSD": 300,
                "500GB SATA SSD": 70,
                "1TB M.2 SATA SSD": 100,
                "2TB M.2 SATA SSD": 180
            },
            "psu": {
                "750W Gold": 100,
                "850W Platinum": 150,
                "1000W Titanium": 200,
                "1200W Platinum": 250,
                "650W Bronze": 80,
                "550W Gold": 90,
                "850W Gold": 130,
                "1000W Gold": 160,
                "650W Platinum": 140,
                "750W Titanium": 180
            },
            "casing": {
                "NZXT H510": 70,
                "Corsair 4000D": 80,
                "Fractal Design Meshify C": 90,
                "Lian Li PC-O11": 100,
                "Phanteks Eclipse P300A": 75,
                "Cooler Master MasterBox Q300L": 65,
                "NZXT H710": 110,
                "Corsair 275R Airflow": 85,
                "NZXT H210": 75,"Lian Li Lancool II Mesh":85
            }
        }


    def create_pc(self):
        while True:
            pc_name = input("Masukkan nama PC: ")
            if pc_name.isalpha():
                break
            else:
                print("Nama PC harus berisi hanya huruf alfabet. Silakan coba lagi.")

        print("Pilih lokasi untuk menempatkan PC baru:")
        print("1. Di awal")
        print("2. Di antara")
        print("3. Di akhir")
        location_choice = input("Masukkan nomor lokasi: ")

        if location_choice == "1":
            self.createPC_diawal(pc_name)
        elif location_choice == "2":
            self.buatPC_diantara(pc_name)
        elif location_choice == "3":
            self.buatPC_diakhir(pc_name)
        else:
            print("Pilihan tidak valid.")

    def createPC_diawal(self, pc_name):
        print("Pilih komponen untuk PC baru:")
        motherboard_info = self.select_component("motherboard")
        processor_info = self.select_component("processor")
        vga_info = self.select_component("vga")
        ram_info = self.select_component("ram")
        ssd_info = self.select_component("ssd")
        psu_info = self.select_component("psu")
        casing_info = self.select_component("casing")
        pc = PC(pc_name, motherboard_info, processor_info, vga_info, ram_info, ssd_info, psu_info, casing_info)
        total_price = pc.calculate_total_price()
        pc.total_price = total_price
        pc.next = self.head
        self.head = pc
        print("PC", pc.pc_name, "berhasil dibuat. Harga Total:", pc.total_price)

    def buatPC_diantara(self, pc_name):
        if not self.head:
            print("Tidak ada PC dalam keranjang untuk menempatkan di antara.")
            return
        print("Pilih lokasi untuk menempatkan PC baru:")
        self.read_pc()
        target_pc_name = input("Masukkan nama PC setelah tempat Anda ingin menempatkan PC baru: ")
        current = self.head
        while current:
            if current.pc_name == target_pc_name:
                break
            current = current.next
        else:
            print("PC dengan nama tersebut tidak ditemukan.")
            return

        print("Pilih komponen untuk PC baru:")
        motherboard_info = self.select_component("motherboard")
        processor_info = self.select_component("processor")
        vga_info = self.select_component("vga")
        ram_info = self.select_component("ram")
        ssd_info = self.select_component("ssd")
        psu_info = self.select_component("psu")
        casing_info = self.select_component("casing")
        pc = PC(pc_name, motherboard_info, processor_info, vga_info, ram_info, ssd_info, psu_info, casing_info)
        total_price = pc.calculate_total_price()
        pc.total_price = total_price
        pc.next = current.next
        current.next = pc
        print("PC berhasil dibuat. Harga Total:", pc.total_price)


    def buatPC_diakhir(self, pc_name):
        print("Pilih komponen untuk PC baru:")
        motherboard_info = self.select_component("motherboard")
        processor_info = self.select_component("processor")
        vga_info = self.select_component("vga")
        ram_info = self.select_component("ram")
        ssd_info = self.select_component("ssd")
        psu_info = self.select_component("psu")
        casing_info = self.select_component("casing")
        pc = PC(pc_name, motherboard_info, processor_info, vga_info, ram_info, ssd_info, psu_info, casing_info)
        if not self.head:
            self.head = pc
        else:
            current = self.head
            while current.next:
                current = current.next
            total_price = pc.calculate_total_price()
            pc.total_price = total_price
            current.next = pc
        print("PC", pc.pc_name, "berhasil dibuat. Harga Total:", pc.total_price)

    def select_component(self, component_type):
        print(f"Pilih {component_type}:")
        table = PrettyTable([f"No.", f"{component_type.capitalize()}", "Harga"])
        components = self.available_components[component_type]
        for index, (component, price) in enumerate(components.items(), start=1):
            table.add_row([index, component, price])
        print(table)
        while True:
            choice = input("Masukkan nomor pilihan: ")
            if choice.isdigit() and 1 <= int(choice) <= len(components):
                component_name = list(components.keys())[int(choice) - 1]
                component_price = components[component_name]
                return {"name": component_name, "price": component_price}
            else:
                print("Pilihan tidak valid. Silakan pilih nomor yang sesuai.")

    def read_pc(self):
        pc_list = []  
        if not self.head:
            print("Keranjang Anda masih kosong.")
        else:
            current = self.head
            while current:
                pc_list.append(current) 
                pc = current
                table = PrettyTable(["Nama PC", "Komponen", "Merek", "Harga"])
                table.add_row([pc.pc_name, "Motherboard", pc.motherboard["name"], pc.motherboard["price"]])
                table.add_row(["", "Processor", pc.processor["name"], pc.processor["price"]])
                table.add_row(["", "VGA", pc.vga["name"], pc.vga["price"]])
                table.add_row(["", "RAM", pc.ram["name"], pc.ram["price"]])
                table.add_row(["", "SSD", pc.ssd["name"], pc.ssd["price"]])
                table.add_row(["", "PSU", pc.psu["name"], pc.psu["price"]])
                table.add_row(["", "Casing", pc.casing["name"], pc.casing["price"]])
                table.add_row(["", "Total", "", pc.calculate_total_price()])
                print(table)
                current = current.next
        return pc_list

    def fibonacci_search(self, pc_list, key, search_field):
        def fibonacci(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            else:
                return fibonacci(num - 1) + fibonacci(num - 2)

        def min_(a, b):
            if a <= b:
                return a
            else:
                return b

        def jump_search(arr, x, n):
            step = int(fibonacci(n))
            prev = 0
            while arr[min_(step, n) - 1] < x:
                prev = step
                step += fibonacci(step)
                if prev >= n:
                    return -1

            while arr[prev] < x:
                prev += 1
                if prev == min_(step, n):
                    return -1

            if arr[prev] == x:
                return prev

            return -1

        pc_names = [pc.__dict__[search_field] for pc in pc_list]
        result_index = jump_search(pc_names, key, len(pc_names))

        if result_index != -1:
            return pc_list[result_index]
        else:
            return None

    def search_pc_by_name(self, pc_list):
        name = input("Masukkan nama PC yang ingin Anda cari: ")
        result = self.fibonacci_search(pc_list, name, "pc_name")
        if result:
            print("PC ditemukan:")
            print("Nama PC:", result.pc_name)
            print("Harga Total:", result.calculate_total_price())
        else:
            print("PC tidak ditemukan.")

    def search_pc_by_price(self, pc_list):
        price = int(input("Masukkan harga PC yang ingin Anda cari: "))
        result = self.fibonacci_search(pc_list, price, "total_price")
        if result:
            print("PC ditemukan:")
            print("Nama PC:", result.pc_name)
            print("Harga Total:", result.calculate_total_price())
        else:
            print("PC tidak ditemukan.")

    def quick_sort(self, pc_list, ascending=True):
        if not pc_list:
            print("Keranjang kosong.")
            return pc_list

        def partition(arr, low, high, ascending=True):
            i = low - 1
            pivot = arr[high]

            for j in range(low, high):
                if (arr[j].pc_name < pivot.pc_name) if ascending else (arr[j].pc_name > pivot.pc_name):
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quick_sort_helper(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort_helper(arr, low, pi - 1)
                quick_sort_helper(arr, pi + 1, high)

        quick_sort_helper(pc_list, 0, len(pc_list) - 1)

        if not ascending:
            pc_list.reverse()

        return pc_list

    def sort_pc_by_name(self, pc_list, ascending=True):
        sorted_pc_list = self.quick_sort(pc_list, ascending)
        print("Daftar PC setelah diurutkan berdasarkan nama:")
        for pc in sorted_pc_list:
            print(f"Nama PC: {pc.pc_name}")

    def sort_pc_by_price(self, pc_list, ascending=True):
        sorted_pc_list = self.quick_sort(pc_list, ascending)
        print("Daftar PC setelah diurutkan berdasarkan harga:")
        for pc in sorted_pc_list:
            print(f"Harga: {pc.calculate_total_price()}")

    def main(self):
        while True:
            print('''
            ============SIMULASI RAKIT PC============
            [*]       1. Tampilkan Keranjang      [*]
            [*]       2. Buat PC                  [*]
            [*]       3. Ubah Komponen            [*]
            [*]       4. Hapus PC                 [*]
            [*]       5. Cari PC                  [*]
            [*]       6. Keluar                   [*]
            =======================================
            ''')

            choice = input("Masukkan pilihan: ")

            if choice == "1":
                os.system("cls")
                print("Menu Lihat Keranjang:")
                pc_list = self.read_pc()  
                sort_choice = input("Pilih urutan (1. Ascending / 2. Descending / 3. Tanpa Sorting): ")
                if sort_choice == "1":
                    sort_order = True
                elif sort_choice == "2":
                    sort_order = False
                elif sort_choice == "3":
                    sort_order = None
                else:
                    print("Pilihan tidak valid.")
                    continue

                sort_criteria = input("Pilih kriteria sorting (1. Nama / 2. Harga): ")
                if sort_criteria == "1":
                    self.sort_pc_by_name(pc_list, sort_order)
                elif sort_criteria == "2":
                    self.sort_pc_by_price(pc_list, sort_order)
                else:
                    print("Pilihan tidak valid.")
                input("Tekan 'Enter' untuk melanjutkan...")
            elif choice == "2":
                self.create_pc()
            elif choice == "3":
                os.system("cls")
                pc_list = self.read_pc() 
                index = int(input("Masukkan nomor PC yang ingin diperbarui: "))
                os.system("cls")
                self.update_pc(index)
            elif choice == "4":
                pc_list = self.read_pc() 
                index = int(input("Masukkan nomor PC yang ingin dihapus: "))
                self.delete_pc(index)
            elif choice == "5":
                os.system("cls")
                print("Menu Cari PC:")
                search_choice = input("Pilih kriteria pencarian (1. Nama / 2. Harga): ")
                if search_choice == "1":
                    self.search_pc_by_name(pc_list)
                elif search_choice == "2":
                    self.search_pc_by_price(pc_list)
                else:
                    print("Pilihan tidak valid.")
                input("Tekan 'Enter' untuk melanjutkan...")
            elif choice == "6":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    builder = RakitPc()
    builder.main()
