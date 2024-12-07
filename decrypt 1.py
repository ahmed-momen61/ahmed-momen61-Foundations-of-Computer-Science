import random

# Modular Inverse using the Extended Euclidean Algorithm
def mod_inv(a, p):
    t, new_t = 0, 1
    r, new_r = p, a
    while new_r != 0:
        dividing_result  = r // new_r
        t, new_t = new_t, t - dividing_result  * new_t
        r, new_r = new_r, r - dividing_result  * new_r
    if r > 1:
        return None
    if t < 0:
        t = t + p
    return t
