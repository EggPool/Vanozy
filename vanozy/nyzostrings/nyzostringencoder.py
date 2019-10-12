"""
Nyzo String encoder

ref: https://github.com/n-y-z-o/nyzoVerifier/blob/master/src/main/java/co/nyzo/verifier/nyzoString/NyzoStringEncoder.java
ref: js impl
"""

from hashlib import sha256
from nyzostrings.nyzostring import NyzoString


__version__ = "0.0.1"


CHARACTER_LOOKUP = (
    "0123456789"
    + "abcdefghijkmnopqrstuvwxyz"  # all except lowercase "L"
    + "ABCDEFGHIJKLMNPQRSTUVWXYZ"  # all except uppercase "o"
    + "-.~_"
)


# From JS code
NYZO_PREFIXES_BYTES = {
    "pre_": bytes([97, 163, 191]),
    "key_": bytes([80, 232, 227]),
    "id__": bytes([72, 223, 255]),
    "pay_": bytes([96, 168, 127]),
    "tx__": bytes([114, 15, 255]),
}

HEADER_LENGTH = 4

CHARACTER_TO_VALUE = {}

# Init reverse index
for i, char in enumerate(CHARACTER_LOOKUP):
    CHARACTER_TO_VALUE[CHARACTER_LOOKUP[i]] = i


class NyzoStringEncoder:
    @classmethod
    def encode(cls, string_object: NyzoString) -> str:
        # Get the prefix array from the type and the content array from the content object.
        prefix_bytes = NYZO_PREFIXES_BYTES[string_object.get_type()]
        content_bytes = string_object.get_bytes()
        content_bytes_len = len(content_bytes)
        """ Determine the length of the expanded array with the header and the checksum. The header is the type-specific
        prefix in characters followed by a single byte that indicates the length of the content array (four bytes
        total). The checksum is a minimum of 4 bytes and a maximum of 6 bytes, widening the expanded array so that
        its length is divisible by 3.
        """
        checksum_length = 4 + (3 - (content_bytes_len + 2) % 3) % 3
        expanded_length = HEADER_LENGTH + content_bytes_len + checksum_length
        """ Create the array and add the header and the content. The first three bytes turn into the user-readable
        prefix in the encoded string. The next byte specifies the length of the content array, and it is immediately
        followed by the content array.
        """
        expanded_buffer = bytearray(expanded_length)
        expanded_buffer[0:3] = prefix_bytes
        expanded_buffer[3] = content_bytes_len
        expanded_buffer[4:4 + content_bytes_len] = content_bytes
        content_view = memoryview(expanded_buffer)[: 4 + content_bytes_len]
        checksum = sha256(sha256(content_view).digest()).digest()[:checksum_length]
        expanded_buffer[4 + content_bytes_len :] = checksum
        return cls.encoded_string_for_bytes(expanded_buffer)

    @classmethod
    def bytes_for_encoded_string(cls, encoded_string: str) -> bytes:
        array_length = (len(encoded_string) * 6 + 7) // 8
        array = bytearray(array_length)
        for i in range(array_length):
            left_character = encoded_string[i * 8 // 6]
            right_character = encoded_string[i * 8 // 6 + 1]
            left_value = CHARACTER_TO_VALUE.get(left_character, 0)
            right_value = CHARACTER_TO_VALUE.get(right_character, 0)
            bit_offset = (i * 2) % 6
            array[i] = (((left_value << 6) + right_value) >> 4 - bit_offset) & 0xFF
        return array

    @classmethod
    def encoded_string_for_bytes(cls, array: bytes) -> str:
        index = 0
        bit_offset = 0
        encoded_string = ""
        while index < len(array):
            # Get the current and next byte.
            left_byte = array[index] & 0xFF
            right_byte = array[index + 1] & 0xFF if index < len(array) - 1 else 0
            # Append the character for the next 6 bits in the array.
            lookup_index = (((left_byte << 8) + right_byte) >> (10 - bit_offset)) & 0x3F
            encoded_string += CHARACTER_LOOKUP[lookup_index]
            # Advance forward 6 bits.
            if bit_offset == 0:
                bit_offset = 6
            else:
                index += 1
                bit_offset -= 2
        return encoded_string
