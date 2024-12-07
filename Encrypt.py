import random

def g_power_k_mod_p(base, exp, mod):        # Exponentiation
    result = 1
    for _ in range(exp):
        result = (result * base) % mod  # Correcting the result update here
    return result

# Encryption part
def encrypt(public_key, message):
    p, g, β = public_key
    
    k = random.randint(1, p - 2)      # Choose a random k
    
    c1 = g_power_k_mod_p(g, k, p)   # Calculate the first part of the secret text
    
    c2 = (message * g_power_k_mod_p(β, k, p)) % p   # Compute the second part (m * β^k) mod p
    
    secret_text = (c1, c2)           # Define the secret_text
    return secret_text

#EX
p, g, β = 47, 4, 6          # Public Key inputs
message = 12                  # Message to encrypt
public_key = (p, g, β)

# Encrypt the message
secret_text = encrypt(public_key, message) # Call to act
print("Your secret text is:", secret_text)
