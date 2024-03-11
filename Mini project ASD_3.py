import os
from prettytable import PrettyTable
os.system("cls")

class PC:
    def __init__(self, motherboard, processor, vga, ram, ssd, psu, casing):
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
    def merge_sort(self, pc_list):
        if len(pc_list) > 1:
            mid = len(pc_list) // 2
            left_half = pc_list[:mid]
            right_half = pc_list[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i].total_price < right_half[j].total_price:
                    pc_list[k] = left_half[i]
                    i += 1
                else:
                    pc_list[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                pc_list[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                pc_list[k] = right_half[j]
                j += 1
                k += 1

class RakitPc:
    def delete_first(self):
        if self.head:
            self.head = self.head.next
        else:
            print("Linked list kosong.")

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
        print("Pilih lokasi untuk menempatkan PC baru:")
        print("1. Di awal")
        print("2. Di antara")
        print("3. Di akhir")
        location_choice = input("Masukkan nomor lokasi: ")

        if location_choice == "1":
            self.createPC_diawal()
        elif location_choice == "2":
            self.buatPC_diantara()
        elif location_choice == "3":
            self.buatPC_diakhir()
        else:
            print("Pilihan tidak valid.")

    def createPC_diawal(self):
        print("Pilih komponen untuk PC baru:")
        motherboard_info = self.select_component("motherboard")
        processor_info = self.select_component("processor")
        vga_info = self.select_component("vga")
        ram_info = self.select_component("ram")
        ssd_info = self.select_component("ssd")
        psu_info = self.select_component("psu")
        casing_info = self.select_component("casing")
        pc = PC(motherboard_info, processor_info, vga_info, ram_info, ssd_info, psu_info, casing_info)
        total_price = pc.calculate_total_price() 
        pc.total_price = total_price
        pc.next = self.head
        self.head = pc
        print("PC berhasil dibuat. Harga Total:", pc.total_price)

    def buatPC_diantara(self):
        if not self.head:
            print("Tidak ada PC dalam keranjang untuk menempatkan di antara.")
            return
        print("Pilih lokasi untuk menempatkan PC baru:")
        self.read_pc()
        location_index = int(input("Masukkan nomor PC setelah tempat Anda ingin menempatkan PC baru: "))
        if location_index < 1:
            print("Indeks tidak valid.")
            return
        elif location_index == 1:
            self.createPC_diawal()
            return

        current = self.head
        count = 1
        while current and count < location_index:
            current = current.next
            count += 1

        if current:
            print("Pilih komponen untuk PC baru:")
            motherboard_info = self.select_component("motherboard")
            processor_info = self.select_component("processor")
            vga_info = self.select_component("vga")
            ram_info = self.select_component("ram")
            ssd_info = self.select_component("ssd")
            psu_info = self.select_component("psu")
            casing_info = self.select_component("casing")
            pc = PC(motherboard_info, processor_info, vga_info, ram_info, ssd_info, psu_info, casing_info)
            total_price = pc.calculate_total_price()
            pc.total_price = total_price
            pc.next = current.next
            current.next = pc
            print("PC berhasil dibuat. Harga Total:", pc.total_price)
        else:
            print("Indeks tidak valid.")

    def buatPC_diakhir(self):
        print("Pilih komponen untuk PC baru:")
        motherboard_info = self.select_component("motherboard")
        processor_info = self.select_component("processor")
        vga_info = self.select_component("vga")
        ram_info = self.select_component("ram")
        ssd_info = self.select_component("ssd")
        psu_info = self.select_component("psu")
        casing_info = self.select_component("casing")
        pc = PC(motherboard_info, processor_info, vga_info, ram_info, ssd_info, psu_info, casing_info)
        if not self.head:
            self.head = pc
        else:
            current = self.head
            while current.next:
                current = current.next
            total_price = pc.calculate_total_price()
            pc.total_price = total_price
            current.next = pc
        print("PC berhasil dibuat. Harga Total:", pc.total_price)

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
    def append(self, pc):
        if not self.head:
            self.head = pc
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = pc

    def read_pc(self):
        pc_list = []  
        if not self.head:
            print("Keranjang Anda masih kosong.")
        else:
            current = self.head
            while current:
                pc_list.append(current) 
                pc = current
                table = PrettyTable(["Nomor PC", "Komponen", "Merek", "Harga"])
                table.add_row([len(pc_list), "Motherboard", pc.motherboard["name"], pc.motherboard["price"]])
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


    def show_sorted_pc(self, pc_list):
        if not pc_list:
            print("Keranjang kosong.")
            return

        choice = input("Pilih urutan (1. Ascending / 2. Descending): ")
        if choice == "1":
            sorted_pc_list = sorted(pc_list, key=lambda pc: pc.calculate_total_price())
        elif choice == "2":
            sorted_pc_list = sorted(pc_list, key=lambda pc: pc.calculate_total_price(), reverse=True)
        else:
            print("Pilihan tidak valid.")
            return

        print("Daftar PC setelah diurutkan:")
        table = PrettyTable(["Komponen", "Harga Total"])
        for pc in sorted_pc_list:
            table.add_row(["", pc.calculate_total_price()])
        print(table)
        
    def update_pc(self, index):
        pc = self.get(index)
        if not pc:
            print("PC tidak ditemukan.")
            return

        print(f"PC {index}:")
        table = PrettyTable(["No.", "Komponen", "Spesifikasi"])
        table.add_row(["1", "Motherboard", pc.motherboard])
        table.add_row(["2", "Processor", pc.processor])
        table.add_row(["3", "VGA", pc.vga])
        table.add_row(["4", "RAM", pc.ram])
        table.add_row(["5", "SSD", pc.ssd])
        table.add_row(["6", "PSU", pc.psu])
        table.add_row(["7", "Casing", pc.casing])
        print(table)
        while True:
            choice = input("Masukkan nomor komponen yang ingin diubah (0 untuk keluar): ")

            if choice == "0":
                break
            elif choice == "1":
                pc.motherboard = self.select_component("motherboard")
            elif choice == "2":
                pc.processor = self.select_component("processor")
            elif choice == "3":
                pc.vga = self.select_component("vga")
            elif choice == "4":
                pc.ram = self.select_component("ram")
            elif choice == "5":
                pc.ssd = self.select_component("ssd")
            elif choice == "6":
                pc.psu = self.select_component("psu")
            elif choice == "7":
                pc.casing = self.select_component("casing")
            else:
                print("Pilihan tidak valid.")

    def delete_pc(self, index):
        if index == 1:
            self.delete_first()
        else:
            prev = None
            current = self.head
            count = 1
            while current and count < index:
                prev = current
                current = current.next
                count += 1
            if current:
                prev.next = current.next
            else:
                print("Indeks tidak valid.")

    def get(self, index):
        current = self.head
        count = 1
        while current and count != index:
            current = current.next
            count += 1
        return current

def main():
    builder = RakitPc()

    while True:
        print('''
        ============SIMULASI RAKIT PC============
        [*]       1. Tampilkan Keranjang      [*]
        [*]       2. Buat PC                  [*]
        [*]       3. Ubah Komponen            [*]
        [*]       4. Hapus PC                 [*]
        [*]       5. Keluar                   [*]
        =======================================
        ''')

        choice = input("Masukkan pilihan: ")

        if choice == "1":
            os.system("cls")
            print("Menu Lihat Keranjang:")
            pc_list = builder.read_pc()  
            sort_choice = input("Apakah Anda ingin melakukan sorting harga? (1. YES/ 2. No): ")
            if sort_choice == "1":
                builder.show_sorted_pc(pc_list)  
            elif sort_choice == "2":
                next 
            else:
                print("Pilihan tidak valid.")
            input("Tekan 'Enter' untuk melanjutkan...")
        elif choice == "2":
            builder.create_pc()
        elif choice == "3":
            os.system("cls")
            pc_list = builder.read_pc() 
            index = int(input("Masukkan nomor PC yang ingin diperbarui: "))
            os.system("cls")
            builder.update_pc(index)
        elif choice == "4":
            pc_list = builder.read_pc() 
            index = int(input("Masukkan nomor PC yang ingin dihapus: "))
            builder.delete_pc(index)
        elif choice == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


if __name__ == "__main__":
    main()