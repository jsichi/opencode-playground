def count_primes(n):
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False

    return sum(is_prime)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <integer>")
        sys.exit(1)
    num = int(sys.argv[1])
    print(f"Number of primes smaller than {num}: {count_primes(num)}")
