import random

def key_generation():
    # Step 1: select  a large prime number p and a generator g
    p = 47  # temporary prime number
    g = 4   # temporary generator

    #Step 2: Generate the private key d randomly
    
    d = random.randint(1, p - 2)  # Private key (1 < d < p-1)

    # Step 3: Calculate the public key β
    
    β = pow(g, d, p)  # Equivalent to (g power d) mod p
    