from pwn import xor #pip install pwntools
flag = bytes.fromhex('3b312857495b41441a115b3a0e5d1d6b32481f3a4d051f0010')
print(xor(flag, 'VHC2022{'.encode())) #xor the ciphertext with a part of plaintext => reveal the key
print(xor(flag, 'mykeyis?'.encode())) #xor the ciphertext with the key
#b'VHC2022{wh0_w4nT_1t_4ll?}'