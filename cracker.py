import itertools
import string
import os
import hashlib


class Cracker:
    ALPHA_LOWER = (string.ascii_lowercase,)
    ALPHA_UPPER = (string.ascii_uppercase,)
    ALPHA_MIXED = (string.ascii_lowercase, string.ascii_uppercase)
    PUNCTUATION = (string.punctuation,)
    NUMERIC = (''.join(map(str, range(0, 10))),)
    ALPHA_LOWER_NUMERIC = (string.ascii_lowercase, ''.join(map(str, range(0, 10))))
    ALPHA_UPPER_NUMERIC = (string.ascii_uppercase, ''.join(map(str, range(0, 10))))
    ALPHA_MIXED_NUMERIC = (string.ascii_lowercase, string.ascii_uppercase, ''.join(map(str, range(0, 10))))
    ALPHA_LOWER_PUNCTUATION = (string.ascii_lowercase, string.punctuation)
    ALPHA_UPPER_PUNCTUATION = (string.ascii_uppercase, string.punctuation)
    ALPHA_MIXED_PUNCTUATION = (string.ascii_lowercase, string.ascii_uppercase, string.punctuation)
    NUMERIC_PUNCTUATION = (''.join(map(str, range(0, 10))), string.punctuation)
    ALPHA_LOWER_NUMERIC_PUNCTUATION = (string.ascii_lowercase, ''.join(map(str, range(0, 10))), string.punctuation)
    ALPHA_UPPER_NUMERIC_PUNCTUATION = (string.ascii_uppercase, ''.join(map(str, range(0, 10))), string.punctuation)
    ALPHA_MIXED_NUMERIC_PUNCTUATION = (
        string.ascii_lowercase, string.ascii_uppercase, ''.join(map(str, range(0, 10))), string.punctuation
    )

    def __init__(self, hash_type, hash):
        self.__hash_type = hash_type
        self.__hash = hash

    def generate_hash(self, data):
        return hashlib.new(self.__hash_type.lower(), data.encode("utf-8")).hexdigest()

    @staticmethod
    def __search_space(charset, maxlength):
        return (
            ''.join(candidate) for candidate in
            itertools.chain.from_iterable(
                itertools.product(charset, repeat=i) for i in
                range(1, maxlength + 1)
            )
        )


if __name__ == "__main__":
    character_sets = {
        "01": Cracker.ALPHA_LOWER,
        "02": Cracker.ALPHA_UPPER,
        "03": Cracker.ALPHA_MIXED,
        "04": Cracker.NUMERIC,
        "05": Cracker.ALPHA_LOWER_NUMERIC,
        "06": Cracker.ALPHA_UPPER_NUMERIC,
        "07": Cracker.ALPHA_MIXED_NUMERIC,
        "08": Cracker.PUNCTUATION,
        "09": Cracker.ALPHA_LOWER_PUNCTUATION,
        "10": Cracker.ALPHA_UPPER_PUNCTUATION,
        "11": Cracker.ALPHA_MIXED_PUNCTUATION,
        "12": Cracker.NUMERIC_PUNCTUATION,
        "13": Cracker.ALPHA_LOWER_NUMERIC_PUNCTUATION,
        "14": Cracker.ALPHA_UPPER_NUMERIC_PUNCTUATION,
        "15": Cracker.ALPHA_MIXED_NUMERIC_PUNCTUATION
    }

    hashes = {
        "01": "MD5",
        "02": "MD4",
        "03": "LM",
        "04": "NTLM",
        "05": "SHA1",
        "06": "SHA224",
        "07": "SHA256",
        "08": "SHA384",
        "09": "SHA512"
    }

    prompt = "Specify the character set to use:" + os.linesep
    for key, value in sorted(character_sets.items()):
        prompt += key + ". " + ''.join(value) + os.linesep

    while True:
        try:
            selected_charset = character_sets[input(prompt).zfill(2)]
        except KeyError:
            print("Please select a valid character set")
            continue
        else:
            break

    prompt = os.linesep + "Specify the maximum possible length of the password: "

    while True:
        try:
            password_length = int(input(prompt))
        except ValueError:
            print("Password length must be an integer")
            continue
        else:
            break

    prompt = os.linesep + "Specify the hash's type:" + os.linesep
    for key, value in sorted(hashes.items()):
        prompt += key + ". " + value + os.linesep

    while True:
        try:
            hash_type = hashes[input(prompt).zfill(2)]
        except KeyError:
            print("Please select a supported hash type")
        else:
            break
