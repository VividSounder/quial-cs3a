import streamlit as st
from streamlit.logger import get_logger

def encrypt_decrypt(text, shift_keys, ifdecrypt):
    """
    Encrypts or decrypts a text using Caesar Cipher with a list of shift keys.
    Args:
        text: The text to encrypt or decrypt.
        shift_keys: A list of integers representing the values for each character.
        ifdecrypt: Flag indicating whether to decrypt (True) or encrypt (False).
    Returns:
        A string containing the encrypted or decrypted text.
    """
    result = ""

    if len(shift_keys) <= 1 or len(shift_keys) > len(text):
        raise ValueError("Invalid shift keys length")
    for i, char in enumerate(text):
            
        # Ensure the shift keys are within the specified range
        shift_key = shift_keys[i % len(shift_keys)]

        if 32 <= ord(char) <= 125:
            new_ascii = ord(char) + shift_key if not ifdecrypt else ord(char) - shift_key
            while new_ascii > 125:
                new_ascii -= 94
            while new_ascii < 32:
                new_ascii += 94
            result += chr(new_ascii)
            
        else:
            result += char
        st.write(i, char, shift_key, result[i])
    return result

LOGGER = get_logger(__name__)

def main():
    st.set_page_config(
        page_title="Caesar Cipher",
        page_icon="X"
    )

    # Example usage
    text = st.text_input("Enter text: ")
    
    shift_keys_input = st.text_input("Enter shift keys: ").split()
    shift_keys = [int(key) for key in shift_keys_input]

    if st.button("Print output"):
        enc = encrypt_decrypt(text, shift_keys, False)
        dec = encrypt_decrypt(enc, shift_keys, True)

        st.write("----------")
        st.write("Text:", text)
        st.write("Shift keys:", shift_keys_input)
        st.write("Encrypted text:", enc)
        st.write("Decrypted text:", dec)
        st.write("----------")

# def Print_Output(text, shift_keys, enc, dec):
#     print("Text: ", text)
#     print("Shift keys: ", *shift_keys)
#     print("Cipher: ", enc)
#     print("Decrypted text: ", dec)

# enc = encrypt_decrypt(text, shift_keys, False)
# print("----------")

# dec = encrypt_decrypt(enc, shift_keys, True)
# print("----------")

# encrypt_input = encrypt_decrypt(text, shift_keys, False)
# print("Encrypted text:", encrypt_input)

if __name__ == "__main__":
    main()