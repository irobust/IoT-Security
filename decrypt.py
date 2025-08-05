import argparse
import sys

def xor_decrypt(key_bytes, input_file, output_file):
    key_length = len(key_bytes)
    if key_length == 0:
        raise ValueError("Key cannot be empty")
    
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        index = 0
        while True:
            chunk = infile.read(4096)  # Read in 4KB chunks
            if not chunk:
                break
            decrypted_chunk = bytearray()
            for byte in chunk:
                key_byte = key_bytes[index % key_length]
                decrypted_chunk.append(byte ^ key_byte)
                index += 1
            outfile.write(decrypted_chunk)

def main():
    parser = argparse.ArgumentParser(description='Decrypt a file using XOR with the provided key.')
    parser.add_argument('--key', required=True, help='XOR key as a hexadecimal string (e.g., "1A2B3C")')
    parser.add_argument('--input', required=True, help='Path to the input file to decrypt')
    parser.add_argument('--output', required=True, help='Path to the output decrypted file')
    
    args = parser.parse_args()
    
    try:
        key_bytes = bytes.fromhex(args.key)
    except ValueError as e:
        print(f"Error: Invalid hexadecimal key. {e}")
        sys.exit(1)
    
    try:
        xor_decrypt(key_bytes, args.input, args.output)
        print("Decryption completed successfully.")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()