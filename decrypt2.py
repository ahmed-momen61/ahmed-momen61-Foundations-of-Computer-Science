import random

# Modular Inverse using the Extended Euclidean Algorithm
def mod_inv(a, p):
    t, new_t = 0, 1
    r, new_r = p, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError(f"{a} has no inverse modulo {p}")
    if t < 0:
        t = t + p
    return t

# Exponentiation function (g^k mod p)
def g_power_k_mod_p(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result