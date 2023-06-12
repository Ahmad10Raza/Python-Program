import hashlib

def sha256(string):
  # Initialize a SHA256 hash object
  sha256_hash = hashlib.sha256()

  # Encode the string and update the hash object
  sha256_hash.update(string.encode())

  # Return the hexadecimal digest of the hash
  return sha256_hash.hexdigest()

# Print the SHA256 hash of "prallav"
print(sha256("prallav"))
