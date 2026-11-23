# Charged rod — first exercise in python-practice
# Physics 2, Q6 (Coulomb): force on a point charge q from a uniformly
# charged rod, solved numerically by slicing the rod.
# Analytical answer: F = k*Q*q / (a*(a+L)) = 1.3485 N
# (k = 8.99e9, Q = 3e-6 C, q = 2e-6 C, L = 0.30 m, a = 0.10 m)

k = 8.99e9; Q = 3e-6; q = 2e-6; L = 0.30; a = 0.10
analytic = k * Q * q / (a * (a + L))
print("analytic:", analytic)
for N in (10, 100, 1000):
    dx = L / N; dq = Q / N; F = 0.0
    for i in range(N):
        x = a + (i + 0.5) * dx
        F += k * q * dq / x**2
    err = abs(F - analytic) / analytic * 100
    print(N, F, "err %:", err)
