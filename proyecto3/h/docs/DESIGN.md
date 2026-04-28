# DESIGN

El programa HackAssembler fue diseñado para convertir código assembler Hack a binario.

La idea es leer un archivo .asm y generar un archivo .hack con instrucciones de 16 bits.

## Cómo funciona

El programa tiene dos partes principales:

### 1. Primera pasada

En esta parte se recorren las líneas para encontrar etiquetas.

Ejemplo:
(LOOP)

Estas etiquetas no se traducen, pero se guardan en la tabla de símbolos.

---

### 2. Segunda pasada

En esta parte se traducen las instrucciones reales.

Se manejan:

- instrucciones tipo A (@valor)
- instrucciones tipo C (dest=comp;jump)

---

## Instrucciones tipo A

Son las que empiezan con @

Ejemplo:
@5

Se convierten directamente a binario de 16 bits.

Si es una variable, se le asigna una dirección desde la posición 16.

---

## Instrucciones tipo C

Ejemplo:
D=A
M=D+1
0;JMP

Se separan en:
- destino
- operación
- salto

Luego se traducen usando tablas.

---

## Instrucciones shift

Se agregó soporte para desplazamientos:

- D<<1
- A<<1
- M<<1
- D>>1
- A>>1
- M>>1

Estas instrucciones se manejan usando la tabla shift_table.

---

## Manejo de errores

El programa revisa errores como:
- símbolos inválidos
- etiquetas repetidas
- operaciones incorrectas

Si hay error, muestra la línea y se detiene.

---

## Resultado

El programa genera un archivo .hack con el mismo nombre.

Cada línea es una instrucción binaria de 16 bits.