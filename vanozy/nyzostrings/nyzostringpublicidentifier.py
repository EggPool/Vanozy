"""
Nyzo String for publicIdentifier
"""

from nyzostrings.nyzostring import NyzoString


__version__ = "0.0.1"


class NyzoStringPublicIdentifier(NyzoString):

    def __init__(self, identifier: bytes) -> None:
        super().__init__('id__', identifier)

    def get_identifier(self) -> bytes:
        return self.bytes_content

    @classmethod
    def from_hex(cls, hex_string: str) -> "NyzoStringPublicIdentifier":
        filtered_string = hex_string.replace('-', '')[:64]
        return NyzoStringPublicIdentifier(bytes.fromhex(filtered_string))
