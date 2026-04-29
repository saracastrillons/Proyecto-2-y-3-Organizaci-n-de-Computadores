# Changelog

## [0.2.0] - 2026-04-27

### Added
- Implementación del chip ALU con soporte para operaciones normales y modo shift
- Implementación del chip Shifter (shift left y shift right)
- Integración del Shifter dentro de la ALU usando condición especial (zx=0, nx=0, zy=0, ny=0, no=1)
- Generación de la señal `isShift` para activar el modo de corrimiento
- Implementación de salida adicional `result` para capturar el bit desplazado
- Cálculo manual de la bandera `zr` usando reducción con compuertas OR
- Uso del bit más significativo para determinar la bandera `ng`

---

## [0.3.0] - 2026-04-27

### Added
- Implementación del archivo `design.txt` explicando la codificación binaria de instrucciones shift
- Definición de nuevas combinaciones `cccccc` para:
  - Shift left (<<1)
  - Shift right (>>1)
- Ejemplos completos de traducción a binario para instrucciones tipo C con shift
- Tabla de destinos (ddd) aplicada a instrucciones shift

---

## [0.4.0] - 2026-04-25

### Added
- Desarrollo del programa `HackAssembler.py`
- Traducción completa de instrucciones tipo A y tipo C
- Implementación de tabla de símbolos (SP, LCL, ARG, THIS, THAT, R0–R15, SCREEN, KBD)
- Manejo de etiquetas (labels) con primera pasada (first pass)
- Manejo de variables dinámicas desde la dirección 16
- Validación de errores de sintaxis (línea inválida, símbolos incorrectos, etc.)
- Generación de archivo `.hack` con instrucciones binarias de 16 bits
- Soporte para instrucciones shift en assembler usando `shift_table`

---

## [0.5.0] - 2026-04-23

### Added
- Desarrollo del programa `HackDisassembler.py`
- Traducción de instrucciones binarias `.hack` a assembler `.asm`
- Identificación de instrucciones tipo A y tipo C
- Decodificación de campos `comp`, `dest` y `jump`
- Implementación de tabla inversa para operaciones ALU
- Soporte para instrucciones shift en desensamblado
- Validación de errores en archivos binarios (longitud incorrecta, caracteres inválidos)
- Generación de archivo `ProgDis.asm`

---

## [0.6.0] - 2026-04-15

### Added
- Implementación del chip `Memory`
- Decodificación de direcciones usando `address[14]` y `address[13]`
- Integración de:
  - RAM16K
  - Screen
  - Keyboard
- Control de escritura mediante señal `load`
- Uso de multiplexores para seleccionar correctamente la salida
- Separación de rangos de memoria:
  - RAM (0–16383)
  - Screen (16384–24575)
  - Keyboard (24576)

---

## [0.7.0] - 2026-03-30

### Added
- Implementación completa del chip `CPU`
- Manejo de instrucciones tipo A y tipo C
- Control de carga de registros A y D
- Selección de entrada de la ALU (A o M) usando `instruction[12]`
- Implementación de lógica de saltos (JGT, JEQ, JLT, etc.)
- Control del Program Counter (PC)
- Generación de señales:
  - `writeM`
  - `addressM`
  - `outM`

---

## [0.8.0] - 2026-03-27

### Added
- Implementación del chip `Computer`
- Integración completa de:
  - CPU
  - Memory
  - ROM32K
- Conexión entre CPU y memoria
- Flujo completo de ejecución de instrucciones
- Sistema listo para ejecutar programas Hack

---

## [0.1.0] - 2026-03-25

### Added
- Creación inicial de la estructura del proyecto
- Carpeta proyecto2
- Archivo CONTRIBUTORS.md
- Archivo CHANGELOG.md
- Archivo LICENSE
- Archivo README.md
