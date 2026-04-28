# API

Este programa llamado HackAssembler sirve para traducir código assembler de Hack (.asm) a código binario (.hack).

El programa está hecho en Python y funciona leyendo un archivo línea por línea.

## Tablas que usa

El programa usa varias tablas para hacer la traducción:

- symbols → guarda variables, etiquetas y registros
- dest_table → traduce el destino (A, D, M)
- jump_table → traduce los saltos
- comp_table → traduce operaciones normales
- shift_table → traduce instrucciones de desplazamiento (<< y >>)

## Funciones principales

### clean_line(line)

Esta función limpia la línea quitando:
- comentarios (//)
- espacios
- tabulaciones

Sirve para trabajar solo con la instrucción.

---

### is_valid_symbol(text)

Verifica si un símbolo es válido.

Por ejemplo:
- variables
- etiquetas

---

### first_pass(lines)

Hace la primera pasada del programa.

Sirve para guardar las etiquetas como:
(LOOP)

en la tabla de símbolos con su posición.

---

### translate_a_instruction(...)

Traduce instrucciones tipo A.

Ejemplo:
@5
@i

Convierte números o variables a binario de 16 bits.

---

### translate_c_instruction(...)

Traduce instrucciones tipo C.

Ejemplo:
D=A
M=D+1
0;JMP

También reconoce instrucciones nuevas como:
D<<1
D>>1

---

### assemble(input_file)

Es la función principal.

Hace todo el proceso:
- lee el archivo
- ejecuta primera pasada
- traduce instrucciones
- genera el archivo .hack

---

### main()

Es el punto de entrada del programa.

Recibe el archivo por consola.