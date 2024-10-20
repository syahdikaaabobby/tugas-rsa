from Crypto.Util.number import *
from Crypto.Util.Padding import pad
import numpy as np
import matplotlib.pyplot as plt

# Generate two large primes
p = getPrime(256)
q = getPrime(256)
n = p * q

# Generate a prime d and calculate the corresponding e
while True:
    d = getPrime(128)
    if GCD(d, (p - 1) * (q - 1)) == 1:
        e = inverse(d, (p - 1) * (q - 1))
        break

# Message (flag)
flag = b"sebagai informasi timnas indonesia akan kembali melawan bahrain pada dua lima maret dua ribu dua lima untuk lanjutan putaran ketiga kualifikasi piala dunia dua ribu dua enam zona asia laga tersebut rencananya digelar di stadion gelora utama bung karno sugbk jakarta namun federasi sepak bola bahrain bahrain fa belum lama ini mengajukan permintaan ke afc dan fifa untuk memindahkan venue pertandingan ke tempat netral alasannya yakni demi keselamatan para pemain bahrain fa mengkaim mendapat banyak ancaman dari suporter timnas indonesia hal tersebut merupakan buntut hasil imbang antara bahrain vs timnas indonesia pada sepuluh oktober lalu kala itu bahrain mampu menahan tim asuhan shin tae yong dengan skor dua dua"
m = bytes_to_long(pad(flag, n.bit_length() // 8))

# Encryption
c = pow(m, e, n)

print(f"p = {p}")
print(f"q = {q}")
print(f"d = {d}")
print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")

# 1. Visual: Visualize the original and encrypted message in binary form
m_bin = bin(m)[2:]
c_bin = bin(c)[2:]

# Ensure both binaries are the same length for visualization
max_len = max(len(m_bin), len(c_bin))
m_bin = m_bin.zfill(max_len)
c_bin = c_bin.zfill(max_len)

# Plot binary comparison between message and ciphertext
plt.figure(figsize=(10, 5))
plt.plot(list(map(int, m_bin)), label="Message (Binary)", color='blue')
plt.plot(list(map(int, c_bin)), label="Ciphertext (Binary)", color='red', linestyle='dashed')
plt.legend()
plt.title('Message vs Ciphertext (Binary)')
plt.xlabel('Bit Position')
plt.ylabel('Bit Value')
plt.show()

# 2. Correlation Coefficient
# Convert the binary strings to arrays of integers
m_array = np.array(list(map(int, m_bin)))
c_array = np.array(list(map(int, c_bin)))

# Compute correlation coefficient
correlation_coefficient = np.corrcoef(m_array, c_array)[0, 1]
print(f"Correlation Coefficient between message and ciphertext: {correlation_coefficient}")

# 3. Avalanche Effect: Encrypt a slightly modified message
# Modify the message by flipping one bit (for example, flip the last bit)
m_flipped = m ^ 1  # Flip the last bit
c_flipped = pow(m_flipped, e, n)

# Compare ciphertexts (original vs flipped message)
c_bin_flipped = bin(c_flipped)[2:].zfill(max_len)

# Calculate the avalanche effect (number of differing bits)
avalanche_effect = sum(b1 != b2 for b1, b2 in zip(c_bin, c_bin_flipped))
print(f"Avalanche Effect (bit differences between original and modified message ciphertexts): {avalanche_effect} bits")
