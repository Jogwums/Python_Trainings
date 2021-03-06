from hashlib import sha256

# print(sha256("ABC".encode("ascii")).hexdigest())
MAX_NONCE = 100000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_no, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros

    for nonce in range(MAX_NONCE):
        # nonce = 2
        text = str(block_no) + transactions + previous_hash + str(nonce)

        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f'Succefull! Mined bitcoin with nonce value: {nonce}')
            return new_hash

    raise BaseException(f'"no show!" after trying {MAX_NONCE} times')


if __name__ == '__main__':
    # print(SHA256("ABC"))
    transactions = """
        Jt->Ken->40,
        Henry->James->25
    """
    #increase difficulty takes longer time 
    difficulty= 6
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions,'00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048',difficulty)
    total_time= str((time.time() - start))
    print(f'end mining... Mining took: {total_time} seconds ')
    print(new_hash)