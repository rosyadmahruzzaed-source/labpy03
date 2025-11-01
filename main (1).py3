# Modal awal
modal = 100_000_000

# Daftar persentase laba per bulan selama 10 bulan
persentase_laba = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03, 0.03, 0.03]

# Inisialisasi total laba
total_laba = 0

# Loop untuk menghitung dan menampilkan laba tiap bulan
for bulan in range(10):
    laba_bulan_ini = modal * persentase_laba[bulan]
    total_laba += laba_bulan_ini
    print(f"laba bulan ke-{bulan+1} sebesar: {laba_bulan_ini}")

# Tampilkan total laba
print(f"Total laba adalah: {total_laba}")