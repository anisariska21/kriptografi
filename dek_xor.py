def dek_xor():
    try:
        with open('cipher.txt', 'r') as fin, open('plain2.txt', 'w') as fout:
            K = input("Kata kunci: ")
            n = len(K)
            i = 0
            while True:
                C = fin.read(1)
                if not C:
                    break
                P = chr(ord(C) ^ ord(K[i]))
                fout.write(P)
                i = (i + 1) % n
    except IOError:
        print("File tidak ditemukan atau tidak bisa dibuka")
    except Exception as e:
        print("Terjadi kesalahan: {}".format(e))

if __name__ == "__main__":
    dek_xor()
