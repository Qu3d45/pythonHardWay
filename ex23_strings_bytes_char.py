# Learn Pyhton The Hard Way ex23 - Strings, Bytes and Character Encodings
# Manuel Lameira

import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    # Debugging
    # print(">>>> main", repr(language_file), encoding, errors)
    line = language_file.readline()

    if line:
        # Debugging
        # print(">> there's a line", repr(line))
        print_line(line, encoding, errors)
        # Debugging
        # print(">> calling main again")
        return main(language_file, encoding, errors)
    # Debugging
    # print("<<<< exit main")


# Takes a line, the encoding (in this case UTF-8) and how to handel errors


def print_line(line, encoding, errors):
    # Debugging
    # print(">>> print_line", repr(print_line), encoding, errors)
    # Removes the withe space oe the new line symbole at the end of the line
    next_lang = line.strip()
    # Takes the line and transform (encodes) in to raw bytes b'...'
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Takes the raw bytes and decodes so we can se the original line value
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
    # Debugging
    # print("<<< exit print_line")


languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
