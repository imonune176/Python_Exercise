# import sys as always and then assigning variables (script, encoding, error)
import sys
script, encoding, error = sys.argv


# here we define our main functions which is going to be used at the end of the script
def main(language_file, encoding, errors):
    line = language_file.readline()

# in this if-statement we check if "line" gives us something. If line is empty the code will skip line 12, 13 else is gonna run them
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


# separate part of code where we define the function to write line keeping it apart from the rest to keep the code in a orderly fashion and simple
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)
