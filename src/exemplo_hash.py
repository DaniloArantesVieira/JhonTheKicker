import hashlib

senha = "secreta123"
# Encode the string to bytes
encoded_data = senha.encode('utf-8') 

# Calculate the MD5 hash
md5_hash_object = hashlib.md5(encoded_data)

# Get the hash in a human-readable hexadecimal format
hex_digest = md5_hash_object.hexdigest()

print(f"Senha: {senha}")
print(f"MD5 hash: {hex_digest}")

# Calculate the SHA1 hash
sha1_hash_object = hashlib.sha1(encoded_data)

# Get the hash in a human-readable hexadecimal format
hex_digest_sha1 = sha1_hash_object.hexdigest()

print(f"Senha: {senha}")
print(f"SHA1 hash: {hex_digest_sha1}")