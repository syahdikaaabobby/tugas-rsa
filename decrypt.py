from Crypto.Util.number import long_to_bytes
import binascii

# Nilai yang Anda temukan
p = 83750310846082649300485078672239524216204975130617823271009793080043451001067
q = 103486588694436010815638386732858139195020500358063300499437741215628150225733
d = 222716010185631599296299814618220075513
n = 8667033971559718310631115074034031239280892064090242251586124309233677962690669043827885766079079487980892229742198167219230305084515949960173560873857111
e = 3396933384595716050189057351090107395457873097106783221936591237634396259224229112862660252093247677738891089913332683986543709478706827670289178826854737
c = 2483590389051614088196334644693979183992867583372199765247296570094716784729112814867153361074855099573488425384622930834082526298691998993453902921936394

# Dekripsi ciphertext menggunakan kunci privat d
m = pow(c, d, n)

# Konversi hasil dekripsi ke bentuk bytes
flag = long_to_bytes(m)

# Mencetak hasil dekripsi
print(f"Flag terdekripsi (as bytes): {flag}")

# ----------------------------------------
# 1. Mencoba Decode sebagai Teks (UTF-8)
try:
    flag_text = flag.decode('utf-8')  # Mencoba decode sebagai teks
    print(f"Flag terdekripsi (UTF-8): {flag_text}")
except UnicodeDecodeError:
    print("Flag terdekripsi bukan dalam format UTF-8, menampilkan hasil dalam format lain...")

# ----------------------------------------
# 2. Mencetak Flag dalam Format Hexadecimal
flag_hex = flag.hex()
print(f"Flag dalam hexadecimal: {flag_hex}")

# ----------------------------------------
# 3. Menyimpan Hasil Dekripsi sebagai File Biner (Jika bukan teks terbaca)
with open('output.bin', 'wb') as f:
    f.write(flag)
print("Hasil dekripsi disimpan dalam file 'output.bin'")
