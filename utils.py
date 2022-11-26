def is_prime(p: int) -> bool:
    if p < 2:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True


def are_coprime(p: int, q: int) -> bool:
    smaller = min(p, q)
    bigger = max(p, q)
    if bigger % smaller == 0:
        return False
    for i in range(2, int(smaller ** 0.2) + 1):
        if p % i == 0 and q % i == 0:
            return False
    return True