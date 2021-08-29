"""
Nyzo String Ancestor

ref: https://github.com/n-y-z-o/nyzoVerifier/blob/master/src/main/java/co/nyzo/verifier/nyzoString/NyzoString.java
"""

__version__ = "0.0.1"


class NyzoString:

    __slots__ = ("string_type", "bytes_content")

    def __init__(self, string_type: str, bytes_content: bytes) -> None:
        self.string_type = string_type
        self.bytes_content = bytes_content

    def get_type(self) -> str:
        return self.string_type

    def get_bytes(self) -> bytes:
        return bytes(self.bytes_content)
