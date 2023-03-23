def find(tests):
    results = []
    for case in tests:
        A, B, X = case

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        G = gcd(A, B)
        results.append(int(X / G))

    return results


T = int(input())
tests = []

for _ in range(T):
    A, B, X = map(int, input().split())
    tests.append((A, B, X))

results = find(tests)

for result in results:
    print(result)
