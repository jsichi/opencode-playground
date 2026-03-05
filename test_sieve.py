from sieve import count_primes

def verify_with_sympy(max_n, verbose=False):
    from sympy import isprime
    for n in range(1, max_n + 1):
        actual = count_primes(n)
        expected = sum(1 for i in range(2, n) if isprime(i))
        assert actual == expected, f"Mismatch at n={n}: got {actual}, expected {expected}"
    if verbose:
        print(f"sympy verified: count_primes correct for n=1 to {max_n}")
    return True

def test_smaller_than_two():
    assert count_primes(0) == 0
    assert count_primes(1) == 0
    print("Test passed: test_smaller_than_two()")

def test_prime_two():
    assert count_primes(3) == 1
    assert count_primes(10) == 4
    assert count_primes(20) == 8
    print("Test passed: test_prime_two()")

def test_small_numbers():
    assert count_primes(12) == 5
    assert count_primes(17) == 6
    print("Test passed: test_small_numbers()")

def test_larger_number():
    assert count_primes(100) == 25
    print("Test passed: test_larger_number()")

def test_verified_with_sympy():
    verify_with_sympy(100, verbose=True)
    print("Test passed: test_verified_with_sympy()")

if __name__ == "__main__":
    test_smaller_than_two()
    test_prime_two()
    test_small_numbers()
    test_larger_number()
    test_verified_with_sympy()
    print("All tests passed!")
