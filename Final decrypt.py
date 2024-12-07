import random

# Modular Inverse using the Extended Euclidean Algorithm
def mod_inv(a, p):
    t, new_t = 0, 1
    r, new_r = p, a
    while new_r != 0:
        dividing_result = r // new_r
        t, new_t = new_t, t - dividing_result * new_t
        r, new_r = new_r, r - dividing_result * new_r
    if r > 1:
        return None
    if t < 0:
        t = t + p
    return t

# Exponentiation function (g power k mod p)
def g_power_k_mod_p(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result

# Decryption part
def decrypt(private_key, public_key, scret_text):
    p, _, β = public_key
    c1, c2 = scret_text
    
    s = g_power_k_mod_p(c1, private_key, p) # Calculate s = c1 power x mod p (using the private key)
    
    s_inv = mod_inv(s, p)           # Calculate the modular inverse of s
    
    original_message = (c2 * s_inv) % p  # get the original_message m = (c2 x s_inv) mod p
    return original_message

#EX
p, g, β = 47, 4, 6  # Public Key inputs
private_key = 15     # Private key (chosen by the receiver)
scret_text = (39, 16)  # Example ciphertext

# Decrypt the message
decrypted_message = decrypt(private_key, (p, g, β), scret_text)
print("Your message is:", decrypted_message)