"""
**********
HackDisassembler.py - Traduce un archivo binario .hack a assembler Hack .asm
Autor 1: Sara Castrillón Sánchez
Autor 2: Alejandro Cadavid
**********
"""

import sys
import os


dest_table = {
    "000": "",
    "001": "M",
    "010": "D",
    "011": "MD",
    "100": "A",
    "101": "AM",
    "110": "AD",
    "111": "AMD"
}


jump_table = {
    "000": "",
    "001": "JGT",
    "010": "JEQ",
    "011": "JGE",
    "100": "JLT",
    "101": "JNE",
    "110": "JLE",
    "111": "JMP"
}


comp_table = {
    "0101010": "0",
    "0111111": "1",
    "0111010": "-1",
    "0001100": "D",
    "0110000": "A",
    "1110000": "M",
    "0001101": "!D",
    "0110001": "!A",
    "1110001": "!M",
    "0001111": "-D",
    "0110011": "-A",
    "1110011": "-M",
    "0011111": "D+1",
    "0110111": "A+1",
    "1110111": "M+1",
    "0001110": "D-1",
    "0110010": "A-1",
    "1110010": "M-1",
    "0000010": "D+A",
    "1000010": "D+M",
    "0010011": "D-A",
    "1010011": "D-M",
    "0000111": "A-D",
    "1000111": "M-D",
    "0000000": "D&A",
    "1000000": "D&M",
    "0010101": "D|A",
    "1010101": "D|M"
}


shift_table = {
    "0000001": "D<<1",
    "0100001": "A<<1",
    "1100001": "M<<1",
    "0000011": "D>>1",
    "0100011": "A>>1",
    "1100011": "M>>1"
}


def clean_line(line):
    return line.strip()


def validate_binary_line(line, line_number):
    if len(line) != 16:
        raise Exception("Error en línea " + str(line_number) + ": la instrucción no tiene 16 bits")

    for bit in line:
        if bit != "0" and bit != "1":
            raise Exception("Error en línea " + str(line_number) + ": la línea tiene caracteres diferentes de 0 o 1")


def translate_a_instruction(line):
    number = int(line, 2)
    return "@" + str(number)


def translate_c_instruction(line, line_number):
    if not line.startswith("111"):
        raise Exception("Error en línea " + str(line_number) + ": instrucción C inválida")

    comp_bits = line[3:10]
    dest_bits = line[10:13]
    jump_bits = line[13:16]

    if comp_bits in shift_table:
        comp = shift_table[comp_bits]
    elif comp_bits in comp_table:
        comp = comp_table[comp_bits]
    else:
        raise Exception("Error en línea " + str(line_number) + ": bits de operación inválidos")

    if dest_bits not in dest_table:
        raise Exception("Error en línea " + str(line_number) + ": bits de destino inválidos")

    if jump_bits not in jump_table:
        raise Exception("Error en línea " + str(line_number) + ": bits de salto inválidos")

    dest = dest_table[dest_bits]
    jump = jump_table[jump_bits]

    instruction = ""

    if dest != "":
        instruction = dest + "=" + comp
    else:
        instruction = comp

    if jump != "":
        instruction = instruction + ";" + jump

    return instruction


def disassemble(input_file):
    if not input_file.endswith(".hack"):
        raise Exception("Error: el archivo debe tener extensión .hack")

    if not os.path.exists(input_file):
        raise Exception("Error: el archivo no existe")

    output_file = input_file[:-5] + "Dis.asm"

    with open(input_file, "r", encoding="utf-8") as file:
        lines = list(enumerate(file.readlines(), start=1))

    output_lines = []

    for line_number, raw_line in lines:
        line = clean_line(raw_line)

        if line == "":
            continue

        validate_binary_line(line, line_number)

        if line[0] == "0":
            asm_instruction = translate_a_instruction(line)
        else:
            asm_instruction = translate_c_instruction(line, line_number)

        output_lines.append(asm_instruction)

    with open(output_file, "w", encoding="utf-8") as file:
        for instruction in output_lines:
            file.write(instruction + "\n")


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 HackDisassembler.py Prog.hack")
        sys.exit(1)

    try:
        disassemble(sys.argv[1])
    except Exception as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()