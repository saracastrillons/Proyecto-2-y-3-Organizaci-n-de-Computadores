"""
**********
HackAssembler.py - Traductor de assembler Hack a binario
Autor 1: Sara Castrillón Sánchez
Autor 2: Alejandro Cadavid
**********
"""

import sys
import os


symbols = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576
}

for i in range(16):
    symbols["R" + str(i)] = i


dest_table = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}


jump_table = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}


comp_table = {
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "M":   "1110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "!M":  "1110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "-M":  "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101"
}


shift_table = {
    "D<<1": "0000001",
    "A<<1": "0100001",
    "M<<1": "1100001",
    "D>>1": "0000011",
    "A>>1": "0100011",
    "M>>1": "1100011"
}


def clean_line(line):
    line = line.split("//")[0]
    line = line.replace(" ", "")
    line = line.replace("\t", "")
    return line.strip()


def is_valid_symbol(text):
    if text == "":
        return False

    if not (text[0].isalpha() or text[0] in "_.$:"):
        return False

    for char in text:
        if not (char.isalnum() or char in "_.$:"):
            return False

    return True


def first_pass(lines):
    rom_address = 0

    for line_number, raw_line in lines:
        line = clean_line(raw_line)

        if line == "":
            continue

        if line.startswith("(") and line.endswith(")"):
            label = line[1:-1]

            if not is_valid_symbol(label):
                raise Exception("Error en línea " + str(line_number) + ": etiqueta inválida")

            if label in symbols:
                raise Exception("Error en línea " + str(line_number) + ": etiqueta repetida")

            symbols[label] = rom_address
        else:
            rom_address += 1


def translate_a_instruction(line, line_number, next_variable_address):
    value = line[1:]

    if value == "":
        raise Exception("Error en línea " + str(line_number) + ": instrucción A vacía")

    if value.isdigit():
        number = int(value)

        if number < 0 or number > 32767:
            raise Exception("Error en línea " + str(line_number) + ": número fuera de rango")

        return format(number, "016b"), next_variable_address

    if not is_valid_symbol(value):
        raise Exception("Error en línea " + str(line_number) + ": símbolo inválido")

    if value not in symbols:
        symbols[value] = next_variable_address
        next_variable_address += 1

    return format(symbols[value], "016b"), next_variable_address


def translate_c_instruction(line, line_number):
    dest = ""
    jump = ""
    comp_part = line

    if "=" in line:
        parts = line.split("=")

        if len(parts) != 2:
            raise Exception("Error en línea " + str(line_number) + ": error con '='")

        dest = parts[0]
        comp_part = parts[1]

    if ";" in comp_part:
        parts = comp_part.split(";")

        if len(parts) != 2:
            raise Exception("Error en línea " + str(line_number) + ": error con ';'")

        comp = parts[0]
        jump = parts[1]
    else:
        comp = comp_part

    if dest not in dest_table:
        raise Exception("Error en línea " + str(line_number) + ": destino inválido")

    if jump not in jump_table:
        raise Exception("Error en línea " + str(line_number) + ": salto inválido")

    if comp in shift_table:
        comp_bits = shift_table[comp]
    elif comp in comp_table:
        comp_bits = comp_table[comp]
    else:
        raise Exception("Error en línea " + str(line_number) + ": operación inválida '" + comp + "'")

    return "111" + comp_bits + dest_table[dest] + jump_table[jump]


def assemble(input_file):
    if not input_file.endswith(".asm"):
        raise Exception("Error: el archivo debe tener extensión .asm")

    if not os.path.exists(input_file):
        raise Exception("Error: el archivo no existe")

    output_file = input_file[:-4] + ".hack"

    with open(input_file, "r", encoding="utf-8") as file:
        lines = list(enumerate(file.readlines(), start=1))

    first_pass(lines)

    next_variable_address = 16
    output_lines = []

    for line_number, raw_line in lines:
        line = clean_line(raw_line)

        if line == "":
            continue

        if line.startswith("(") and line.endswith(")"):
            continue

        if line.startswith("@"):
            binary, next_variable_address = translate_a_instruction(
                line,
                line_number,
                next_variable_address
            )
            output_lines.append(binary)
        else:
            binary = translate_c_instruction(line, line_number)
            output_lines.append(binary)

    with open(output_file, "w", encoding="utf-8") as file:
        for binary in output_lines:
            file.write(binary + "\n")


def main():
    if len(sys.argv) != 2:
        print("Uso: python HackAssembler.py Prog.asm")
        sys.exit(1)

    try:
        assemble(sys.argv[1])
    except Exception as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()