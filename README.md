# Calculadora Multi-Base con Flet

Una aplicación de calculadora de escritorio simple pero potente construida con Flet (Python). Esta calculadora no solo realiza operaciones aritméticas básicas, sino que también permite al usuario cambiar y operar entre diferentes sistemas numéricos: Decimal, Binario, Octal y Hexadecimal.

[Inserta aquí una captura de pantalla de la calculadora en funcionamiento]

---

## 🚀 Características

* **Operaciones Aritméticas:** Suma (`+`), Resta (`-`), Multiplicación (`*`) y División (`/`).
* **Soporte Multi-Base:**
    * Decimal (DEC)
    * Binario (BIN)
    * Octal (OCT)
    * Hexadecimal (HEX)
* **Conversión Dinámica:** La calculadora convierte las entradas a decimal para realizar los cálculos y luego vuelve a mostrar el resultado en la base seleccionada.
* **Entrada Inteligente:** La interfaz deshabilita automáticamente la entrada de caracteres no válidos según el modo seleccionado (por ejemplo, los dígitos del 2-9 están inactivos en modo Binario, y las letras A-F están inactivas en modo Decimal u Octal).
* **Controles de Interfaz:**
    * `R`: Resetea el cálculo actual y la memoria.
    * `<`: Borra el último carácter introducido (Retroceso).
    * `=`: Calcula el resultado final de la operación.

---

## 🛠️ Tecnologías Utilizadas

* **Python:** `3.13.0`
* **Flet:** `0.24.1`

---

## 📋 Requisitos

Para ejecutar este proyecto, necesitarás tener instalado:

* Python (versión 3.13.0 o compatible)
* Flet (versión 0.24.1)

---

## ⚙️ Instalación y Ejecución

1.  **Clona o descarga el repositorio:**
    (Si es un repositorio git)
    ```bash
    git clone https://codersamx/Calculadora.git
    cd Calculadora
    ```
    (Si solo tienes el archivo, simplemente colócalo en un directorio y navega hasta él)

2.  **(Opcional pero recomendado) Crea un entorno virtual:**
    ```bash
    python -m venv venv
    ```
    * En Windows: `.\venv\Scripts\activate`
    * En macOS/Linux: `source venv/bin/activate`

3.  **Instala las dependencias:**
    El único requisito es Flet.
    ```bash
    pip install flet==0.24.1
    ```

4.  **Ejecuta la aplicación:**
    Puedes ejecutar la aplicación directamente usando el comando `flet run` (que también proporciona recarga en caliente si haces cambios) o como un script de Python normal.

    **Opción A (Recomendada por Flet):**
    ```bash
    flet run calculator.py
    ```

    **Opción B (Estándar de Python):**
    ```bash
    python calculator.py
    ```

---

## 📁 Estructura del Código

El proyecto consta de un único archivo, `calculator.py`:

* **Clases de Botones:**
    * `CalcButton`: Clase base para todos los botones.
    * `DigitButton`: Botones para dígitos (0-9, A-F, .).
    * `ActionButton`: Botones de operaciones (+, -, \*, /, =).
    * `ExtraActionButton`: Botones de control (R, <) y A-F.

* **Clase Principal `CalculatorApp(ft.Container)`:**
    * `__init__`: Construye la interfaz de usuario (UI) completa, incluyendo la pantalla de resultados, el grupo de radio para cambiar de modo y la cuadrícula de botones.
    * `change_mode`: Maneja el evento de cambio del `RadioGroup` (DEC, BIN, OCT, HEX).
    * `button_clicked`: Lógica principal que maneja todos los clics de los botones, filtra la entrada según el modo y dirige el flujo de cálculo.
    * `calculate`: Realiza la operación aritmética (siempre en base 10).
    * `convert_input`: Convierte el valor de entrada (Binario, Octal, Hex) a Decimal antes de calcular.
    * `format_number` / `reset` / `borrar_caracter`: Funciones de utilidad.
    * **Funciones de Conversión:** Un conjunto de métodos para convertir números entre decimal, binario, octal y hexadecimal.

* **Función `main(page: ft.Page)`:**
    * Punto de entrada de la aplicación Flet. Configura la página, instancia `CalculatorApp` y la añade a la página.
