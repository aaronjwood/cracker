import itertools
import string
import os


class Cracker:
    ALPHA_LOWER = string.ascii_lowercase
    ALPHA_UPPER = string.ascii_uppercase
    ALPHA_MIXED = string.ascii_letters
    PUNCTUATION = string.punctuation
    NUMERIC = ''.join(map(str, range(0, 10)))
    ALPHA_LOWER_NUMERIC = ALPHA_LOWER + NUMERIC
    ALPHA_UPPER_NUMERIC = ALPHA_UPPER + NUMERIC
    ALPHA_MIXED_NUMERIC = ALPHA_MIXED + NUMERIC
    ALPHA_LOWER_PUNCTUATION = ALPHA_LOWER + PUNCTUATION
    ALPHA_UPPER_PUNCTUATION = ALPHA_UPPER + PUNCTUATION
    ALPHA_MIXED_PUNCTUATION = ALPHA_MIXED + PUNCTUATION
    NUMERIC_PUNCTUATION = NUMERIC + PUNCTUATION
    ALPHA_LOWER_NUMERIC_PUNCTUATION = ALPHA_LOWER_NUMERIC + PUNCTUATION
    ALPHA_UPPER_NUMERIC_PUNCTUATION = ALPHA_UPPER_NUMERIC + PUNCTUATION
    ALPHA_MIXED_NUMERIC_PUNCTUATION = ALPHA_MIXED_NUMERIC + PUNCTUATION

    @staticmethod
    def search_space(charset, maxlength):
        return (
            ''.join(candidate) for candidate in
            itertools.chain.from_iterable(
                itertools.product(charset, repeat=i) for i in
                range(1, maxlength + 1)
            )
        )


if __name__ == "__main__":
    character_sets = {"01": Cracker.ALPHA_LOWER, "02": Cracker.ALPHA_UPPER, "03": Cracker.ALPHA_MIXED,
                      "04": Cracker.NUMERIC, "05": Cracker.ALPHA_LOWER_NUMERIC, "06": Cracker.ALPHA_UPPER_NUMERIC,
                      "07": Cracker.ALPHA_MIXED_NUMERIC, "08": Cracker.PUNCTUATION,
                      "09": Cracker.ALPHA_LOWER_PUNCTUATION, "10": Cracker.ALPHA_UPPER_PUNCTUATION,
                      "11": Cracker.ALPHA_MIXED_PUNCTUATION, "12": Cracker.NUMERIC_PUNCTUATION,
                      "13": Cracker.ALPHA_LOWER_NUMERIC_PUNCTUATION, "14": Cracker.ALPHA_UPPER_NUMERIC_PUNCTUATION,
                      "15": Cracker.ALPHA_MIXED_NUMERIC_PUNCTUATION}

    prompt = "Specify the character set to use:" + os.linesep
    for key, value in sorted(character_sets.items()):
        prompt += key + ". " + value + os.linesep

    selected_charset = input(prompt).zfill(2)
