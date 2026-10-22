import tkinter as tk
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan").pack(pady=10)

frame = tk.Frame(root)
frame.pack()

for i in range(10):
    tk.Label(frame, text="Nilai Mata Pelajaran " + str(i + 1)).grid(row=i, column=0, sticky="w", padx=5, pady=2)
    tk.Entry(frame).grid(row=i, column=1, padx=5, pady=2)

