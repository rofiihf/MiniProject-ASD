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

class PCBuilder:
    def __init__(self):
        self.pc_list = []
        self.available_components = {
            "motherboard": [
                "MSI B450", "ASUS ROG Strix X570", "Gigabyte B550", "ASRock Z590",
                "MSI MAG B550 TOMAHAWK", "ASUS TUF Gaming B550-PLUS", "GIGABYTE B550 AORUS PRO",
                "ASRock B550M Steel Legend", "ASUS PRIME B550M-A", "MSI MPG B550 GAMING EDGE WIFI"
            ],
            "processor": [
                "AMD Ryzen 5 5600X", "AMD Ryzen 9 5900X", "Intel Core i7-11700K", "Intel Core i9-11900K",
                "AMD Ryzen 7 5800X", "AMD Ryzen 9 5950X", "Intel Core i5-11600K", "Intel Core i9-10900K",
                "AMD Ryzen 5 3600", "Intel Core i5-10600K"
            ],
            "vga": [
                "NVIDIA GeForce RTX 3070", "NVIDIA GeForce RTX 3080", "AMD Radeon RX 6800 XT", "NVIDIA GeForce RTX 3090",
                "NVIDIA GeForce RTX 3060 Ti", "AMD Radeon RX 6900 XT", "NVIDIA GeForce RTX 3060", "AMD Radeon RX 6700 XT",
                "NVIDIA GeForce RTX 3050 Ti", "AMD Radeon RX 6600 XT"
            ],
            "ram": [
                "16GB DDR4", "32GB DDR4", "64GB DDR4", "128GB DDR4",
                "8GB DDR4", "16GB DDR4 RGB", "32GB DDR4 RGB", "64GB DDR4 RGB",
                "16GB DDR4 3600MHz", "32GB DDR4 3600MHz"
            ],
            "ssd": [
                "500GB NVMe SSD", "1TB NVMe SSD", "2TB NVMe SSD", "4TB NVMe SSD",
                "250GB NVMe SSD", "2TB SATA SSD", "4TB SATA SSD", "500GB SATA SSD",
                "1TB M.2 SATA SSD", "2TB M.2 SATA SSD"
            ],
            "psu": [
                "750W Gold", "850W Platinum", "1000W Titanium", "1200W Platinum",
                "650W Bronze", "550W Gold", "850W Gold", "1000W Gold",
                "650W Platinum", "750W Titanium"
            ],
            "casing": [
                "NZXT H510", "Corsair 4000D", "Fractal Design Meshify C", "Lian Li PC-O11",
                "Phanteks Eclipse P300A", "Cooler Master MasterBox Q300L", "NZXT H710", "Corsair 275R Airflow",
                "NZXT H210", "Lian Li Lancool II Mesh"
            ]
        }

    def create_pc(self):
        print("Pilih komponen untuk PC baru:")
        motherboard = self.select_component("motherboard")
        processor = self.select_component("processor")
        vga = self.select_component("vga")
        ram = self.select_component("ram")
        ssd = self.select_component("ssd")
        psu = self.select_component("psu")
        casing = self.select_component("casing")
        pc = PC(motherboard, processor, vga, ram, ssd, psu, casing)
        self.pc_list.append(pc)

    def select_component(self, component_type):
        print(f"Pilih {component_type}:")
        table = PrettyTable([f"No.", f"{component_type.capitalize()}"])
        components = self.available_components[component_type]
        for index, component in enumerate(components, start=1):
            table.add_row([index, component])
            os.system("cls")
        print(table)
        while True:
            choice = input("Masukkan nomor pilihan: ")
            if choice.isdigit() and 1 <= int(choice) <= len(components):
                return components[int(choice) - 1]
            else:
                print("Pilihan tidak valid. Silakan pilih nomor yang sesuai.")

    def read_pc(self):
        if not self.pc_list:
            print("Keranjang Anda masih kosong.")
        else:
            for index, pc in enumerate(self.pc_list, start=1):
                print(f"PC {index}:")
                table = PrettyTable(["Komponen", "Spesifikasi"])
                table.add_row(["Motherboard", pc.motherboard])
                table.add_row(["Processor", pc.processor])
                table.add_row(["VGA", pc.vga])
                table.add_row(["RAM", pc.ram])
                table.add_row(["SSD", pc.ssd])
                table.add_row(["PSU", pc.psu])
                table.add_row(["Casing", pc.casing])
                print(table)

    def update_pc(self, index):
        if not self.pc_list:
            print("Belum ada PC yang dibuat.")
            return

        pc = self.pc_list[index - 1]
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
        del self.pc_list[index - 1]

def main():
    global builder
    builder = PCBuilder()

    while True:
        os.system("cls")
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
            builder.read_pc()
            input("Tekan 'Enter' untuk melanjutkan...")
        elif choice == "2":
            builder.create_pc()
            print("PC berhasil dibuat.")
        elif choice == "3":
            os.system("cls")
            builder.read_pc()
            index = int(input("Masukkan nomor PC yang ingin diperbarui: "))
            os.system("cls")
            builder.update_pc(index)
            print("PC berhasil diperbarui.")
        elif choice == "4":
            builder.read_pc()
            index = int(input("Masukkan nomor PC yang ingin dihapus: "))
            builder.delete_pc(index)
            print("PC berhasil dihapus.")
        elif choice == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
