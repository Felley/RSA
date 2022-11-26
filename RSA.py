from utils import is_prime, are_coprime

alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])


def encode(p: int, q: int, k: int, letter: str) -> list[int]:
    assert is_prime(p) and is_prime(q), "p and q should be prime"
    assert 2 < k < (p - 1) * (q - 1), "k should be > 2 and < phi(n)"
    assert are_coprime(k, (p - 1) * (q - 1)), "k should be coprime with phi(n)"
    cypher = []
    n = p * q
    for ch in letter:
        if ch == ' ':
            x = 2
        else:
            x = ord(ch) - ord('a') + 3
        y = (x ** k) % n
        cypher.append(y)
    return cypher


def decode(n: int, k: int, cypher: list[int]) -> str:
    p, q = 1, 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            p, q = i, n // i
            break
    print(f"p: {p}, q: {q}")
    phi_n = (p - 1) * (q - 1)
    l = pow(k, -1, mod=phi_n)
    print(f"l: {l}")

    result = []
    for y in cypher:
        index = (y ** l) % n
        result.append(alphabet[index - 3] if index > 2 else ' ')
    result_string = ''.join(result)
    print(result_string)
    return result_string


if __name__ == '__main__':
    cypher = encode(37, 47, 523, "alan turing")
    print(cypher)
    decode(1739, 523, cypher)
