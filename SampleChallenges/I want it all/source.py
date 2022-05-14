from pwn import xor

flag = b'VHC2022{wh0_w4nT_1t_4ll?}'
xorKey = b'mykeyis?'

xored = xor(flag, xorKey)
print(xored.hex()) #3b312857495b41441a115b3a0e5d1d6b32481f3a4d051f0010

