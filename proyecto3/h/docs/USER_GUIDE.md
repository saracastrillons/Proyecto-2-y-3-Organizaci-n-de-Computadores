# USER GUIDE

Este programa sirve para traducir archivos assembler Hack (.asm) a binario (.hack).

## Requisitos

Tener Python instalado (preferiblemente Python 3).

---

## Cómo usarlo

1. Ir a la carpeta donde está el archivo:

cd src

2. Ejecutar el programa:

python3 HackAssembler.py Prog.asm

---


- Lee el archivo .asm
- Ignora comentarios y líneas vacías
- Traduce instrucciones
- Genera archivo .hack

---

## Ejemplo

Archivo Prog.asm:

@5
D=A
D=D<<1
AM=D>>1

---

Salida esperada (Prog.hack):

0000000000000101
1110110000010000
1110000001010000
1110000011101000

---

## Instrucciones que reconoce

El programa reconoce:

- instrucciones normales de Hack
- instrucciones shift como:

D<<1
A<<1
M<<1
D>>1
A>>1
M>>1

---

## Errores

Si hay un error, el programa muestra algo como por ej:

Error en línea 3: operación inválida

y se para

---

## Notas

- El archivo debe terminar en .asm
- El archivo .hack se crea automáticamente
- Las etiquetas como (LOOP) no generan código