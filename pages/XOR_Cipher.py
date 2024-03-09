import streamlit as st

def xor_encrypt(plaintext, key):
    """Encrypts plaintext using XOR cipher with the given key, printing bits included."""
    
    ciphertext = bytearray()
    
    for i in range(len(plaintext)): 
        plaintext_byte = plaintext[i]
        key_byte = key[i % len(key)]
                
        encrypted_byte = plaintext_byte ^ key_byte
        ciphertext.append(encrypted_byte)
    
        st.write(f"Plaintext byte: {format(plaintext_byte, '08b')} = {chr(plaintext_byte)}")
        st.write(f"Key byte:       {format(key_byte, '08b')} = {chr(key_byte)}")
        st.write(f"XOR result:     {format(ciphertext[-1], '08b')} = {chr(ciphertext[-1])}")
        st.write("--------------------")
        
    return ciphertext
    
def xor_decrypt(ciphertext, key):
    """"Decrypts ciphertext using XOR cipher with the given key."""
    return xor_encrypt(ciphertext, key)# XOR decryption is the same as the encryption.

def main():
    # Example usage:
    plaintext = st.text_input("Enter text: ")

    key = st.text_input("Enter key: ")

    if st.button("Print output"):
        if not (1 < len(plaintext) >= len(key) >= 1):
            st.write("Plaintext length should be equal or greater than the length of key")
        elif not plaintext != key:
            st.write("Plaintext should not be equal to the key")
        else:
            ciphertext = xor_encrypt(plaintext, key)
            st.write("Ciphertext:", ciphertext.decode())

            decrypted_text = xor_decrypt(ciphertext, key)
            st.write("Decrypted:   ", decrypted_text.decode())

if __name__ == "__main__":
    main()