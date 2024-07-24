def enk_xor():
    try:
        with open('plain.txt', 'r') as fin, open('cipher.txt', 'w') as fout:
            K = input("Kata kunci: ")
            n = len(K)
            i = 0
            while True:
                P = fin.read(1)
                if not P:
                    break
                C = chr(ord(P) ^ ord(K[i]))
                fout.write(C)
                i = (i + 1) % n
    except IOError:
        print("File tidak ditemukan atau tidak bisa dibuka")
    except Exception as e:
        print("Terjadi kesalahan: {}".format(e))

if __name__ == "__main__":
    enk_xor()
