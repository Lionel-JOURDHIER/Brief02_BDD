import os
from cryptography.fernet import Fernet

from sqlalchemy.types import TypeDecorator, String

# For educational purposes, the key may be stored in thr root directory,
# but in production, store the key securely (e.g., in an environment variable or secure vault)
# to improve security.

def create_fernet_key(path="fernet.key"):
    '''
    Generate a new Fernet key and save it to a file.
    This key can be used for symmetric encryption in the database or 
    other secure storage. 

    WARNING:
        If the file already exists and contains a key, it will NOT be overwritten.
        If this key is used in the database, do not change it afterwards,
        as you will no longer be able to decrypt existing data.

    Args : 
        path : str, optional
            Path to the file where the fernet key will be stored. 

    Returns : 
        None
    '''
    key = Fernet.generate_key().hex()
    if os.path.exists(path):
        with open(path,"r+") as f : 
            content = f.read()
            if not content : 
                f.write(key)
            else : 
                print("There is already a key in the file.")
    else : 
        with open(path,"w") as f:
            f.write(key)
            print(f"Fernet key created and saved to '{path}'.")

def load_fernet_key(path="fernet.key"):
    '''
    Attempt to load a previously generated Fernet key from a file.
    If the file does not exist, is empty, or contains invalid data, 
    returns None instead of raising an exception.

    Args : 
        path : str, optional
            Path to the file where the fernet key is stored. 

    Returns:
        bytes or None: The Fernet key if successfully loaded, else None.
    '''
    if not os.path.exists(path):
        print(f"Key file '{path}' does not exist. Continuing without key.")
        return None
    try :
        if not os.path.exists(path):
            raise FileNotFoundError(f"The key file '{path}' does not exist.")
        with open(path, "r") as f:
            key_hex = f.read()
            if not key_hex:
                print(f"Key file '{path}' is empty. Continuing without key.")
                return None
            return bytes.fromhex(key_hex)
    except Exception as e:
        print(f"Failed to read or decode key from '{path}': {e}. Continuing without key.")
        return None
    
FERNET_KEY = load_fernet_key()
fernet = Fernet(FERNET_KEY)

def encrypt_string(original_text, fernet_key = FERNET_KEY):
    """
    Encrypts a string using Fernet symmetric encryption.

    Args : 
        original_text: The plaintext string to encrypt.
        fernet_key: The Fernet key to use for encryption (bytes).
    Return: 
        The encrypted string, base64-encoded (UTF-8).
    """
    fernet = Fernet(fernet_key)
    byte_text = original_text.encode()
    encrypted_bytes = fernet.encrypt(byte_text)
    return encrypted_bytes.decode()

def decrypt_string(encrypted_text, fernet_key = FERNET_KEY):
    """
    Decrypts a Fernet-encrypted string.

    Args : 
        encrypted_text: The encrypted string (UTF-8)
    Return: 
        The original plaintext string
    """
    fernet = Fernet(fernet_key)
    byte_text = encrypted_text.encode()
    original_bytes = fernet.decrypt(byte_text)
    return original_bytes.decode()

class EncryptedString(TypeDecorator):
    """
    SQLAlchemy custom type for storing encrypted strings in the database.

    This type automatically encrypts data when writing to the database
    and decrypts it when reading from the database using a Fernet key.
    
    Workflow:
        - Ensure a Fernet key is available, e.g. via:
            FERNET_KEY = load_fernet_key()
            fernet = Fernet(FERNET_KEY)
        - This key is used internally by EncryptedString for encryption and decryption.

    Notes:
        - Passing None as a value will store None in the database without encryption.
        - Stored values in the database are UTF-8 encoded strings of the encrypted bytes.
    """
    impl = String
    cache_ok = True 
    
    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        return fernet.encrypt(value.encode()).decode()

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        return fernet.decrypt(value.encode()).decode()