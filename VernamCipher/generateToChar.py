def binary_to_ascii(binary_list):
    ascii_string = ""
    for i in range(0, len(binary_list), 8):  
        byte = binary_list[i:i+8]
        byte_str = ''.join(str(bit) for bit in byte)
        ascii_char = chr(int(byte_str, 2))  
        ascii_string += ascii_char
    return ascii_string