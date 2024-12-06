import tkinter as tk
from tkinter import messagebox, ttk

# Fungsi untuk menghitung zakat fitrah
def hitung_zakat_fitrah():
    try:
        # Ambil input dari pengguna
        jumlah_jiwa = int(entry_jiwa.get())
        harga_beras = float(entry_harga_beras.get())
        
        # Perhitungan zakat fitrah
        kebutuhan_per_jiwa = 2.5  # dalam kilogram
        total_zakat = jumlah_jiwa * kebutuhan_per_jiwa * harga_beras

        # Pesan hasil
        
        # Tampilkan hasil
        messagebox.showinfo("Hasil Perhitungan Zakat Fitrah", message)

    except ValueError:
        messagebox.showerror("Input Error", "Harap masukkan angka yang valid untuk semua input.")

# GUI menggunakan Tkinter
root = tk.Tk()
root.title("Kalkulator Zakat Fitrah")
root.geometry("500x400")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Judul Aplikasi
label_judul = tk.Label(root, text="Kalkulator Zakat Fitrah", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
label_judul.pack(pady=20)

# Deskripsi
label_deskripsi = tk.Label(root, text="Hitung zakat fitrah berdasarkan jumlah jiwa dan harga beras.", font=("Arial", 12), bg="#f0f0f0", fg="#666")
label_deskripsi.pack(pady=5)

# Input Jumlah Jiwa
frame_jiwa = tk.Frame(root, bg="#f0f0f0")
frame_jiwa.pack(pady=10, padx=20, anchor="w")
tk.Label(frame_jiwa, text="Jumlah Jiwa:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, sticky="w")
entry_jiwa = tk.Entry(frame_jiwa, width=25, font=("Arial", 12))
entry_jiwa.grid(row=0, column=1, pady=5)

# Input Harga Beras
frame_harga = tk.Frame(root, bg="#f0f0f0")
frame_harga.pack(pady=10, padx=20, anchor="w")
tk.Label(frame_harga, text="Harga Beras per Kg (Rp):", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, sticky="w")
entry_harga_beras = tk.Entry(frame_harga, width=25, font=("Arial", 12))
entry_harga_beras.grid(row=0, column=1, pady=5)

# Tombol Hitung
button_hitung = tk.Button(root, text="Hitung Zakat Fitrah", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=hitung_zakat_fitrah)
button_hitung.pack(pady=20)

# Footer
label_footer = tk.Label(root, text="© 2023 Kalkulator Zakat Fitrah kelompok 2", font=("Arial", 10), bg="#f0f0f0", fg="#666")
label_footer.pack(side="bottom", pady=10)

# Menjalankan aplikasi
root.mainloop()