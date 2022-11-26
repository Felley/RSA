from utils import is_prime, are_coprime


def generate(start: int, finish: int, output_file: str):
    with open(output_file, 'w') as f:
        f.write("p,q,k\n")
        for p in range(start, finish):
            if not is_prime(p):
                continue
            for q in range(p + 1, finish):
                if p == q or not is_prime(q):
                    continue
                phi_n = (p - 1) * (q - 1)
                for k in range(3, phi_n):
                    if are_coprime(k, phi_n):
                        f.write(f"{p},{q},{k}\n")


if __name__ == "__main__":
    generate(2, 100, "keys.csv")
