import flet as ft


class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text


class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE
        self.style = ft.ButtonStyle(shape=ft.CircleBorder(), padding=20,text_style=ft.TextStyle(size=30))


class ActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE
        self.style = ft.ButtonStyle(shape=ft.CircleBorder(), padding=20,text_style=ft.TextStyle(size=30))


class ExtraActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.BLUE_GREY_200
        self.color = ft.colors.BLACK
        self.style = ft.ButtonStyle(shape=ft.CircleBorder(), padding=20,text_style=ft.TextStyle(size=30))


class CalculatorApp(ft.Container):
    # control raíz de la aplicación (es decir, "vista") que contiene todos los demás controles
    def __init__(self):
        super().__init__()
        self.reset()
        #aqui almacenamos las operaciones que realizamos 
        self.operacion_viw = ft.Text(value="", size=25,color=ft.colors.WHITE)
        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=40)
        #self.width = 350 #ancho del contenedor principal
        #self.bgcolor = ft.colors.WHITE24
        self.border_radius = ft.border_radius.all(10)
        self.padding = 0
        self.margin = 0
        self.expand = True
        self.mode ="decimal"
        
        self.content = ft.Column(
            controls=[
                # Contenedor 1 para la pantalla
                ft.Container(
                    margin=0,
                    padding= ft.padding.only(right=15),
                    #padding=30,
                    alignment=ft.alignment.center,
                    #bgcolor=ft.colors.WHITE24,
                    height=130, #alto del contenedor
                    border_radius=5,
                    content=ft.Column(controls=[
                        ft.Row(controls=[self.operacion_viw], alignment="end"),
                        ft.Row(controls=[self.result], alignment="end"),
                        ], spacing=20, alignment= ft.MainAxisAlignment.CENTER
                    ),
                    
                ),
                # contenedor 2 para el radioGrupo 
                ft.Container(
                    #bgcolor=ft.colors.WHITE10,
                    height=70, #alto del contenedor
                    border_radius=0,
                    margin= 0,
                    padding=5,
                    content = ft.Column(
                        controls=[
                            ft.RadioGroup(
                                content=ft.Row(
                                    controls=[
                                        ft.Radio(value="decimal", label="DEC", expand=1),
                                        ft.Radio(value="binario", label="BIN", expand=1),
                                        ft.Radio(value="octal", label="OCT", expand=1),
                                        ft.Radio(value="hexadecimal", label="HEX", expand=1),
                                    ], vertical_alignment= ft.MainAxisAlignment.CENTER
                                ),
                                value="decimal",
                                on_change=self.change_mode,
                            ),
                            ft.Divider(height=1, color="white"),
                        ], spacing=1, alignment= "center"
                    ),
                    
                    
                ),
                # Contenedor 3 para los botones
                ft.Container( 
                    margin=0,
                    padding=3,
                    alignment=ft.alignment.center,
                    #bgcolor=ft.colors.WHITE30,
                    ##width=300, #ancho del contenedor inutil cuando expan = true
                    #height=450, #alto del contenedor inutil cuando expan = true
                    border_radius=5,
                    expand=True,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ExtraActionButton(text="A", button_clicked=self.button_clicked),
                                    ExtraActionButton(text="B", button_clicked=self.button_clicked),
                                    ExtraActionButton(text="C", button_clicked=self.button_clicked),
                                    ActionButton(text="R", button_clicked=self.button_clicked),
                                ], spacing=3, expand=True
                            ),
                            
                            ft.Row(
                                controls=[
                                    ExtraActionButton(text="D", button_clicked=self.button_clicked),
                                    ExtraActionButton(text="E", button_clicked=self.button_clicked),
                                    ExtraActionButton(text="F", button_clicked=self.button_clicked),
                                    ActionButton(text="/", button_clicked=self.button_clicked),
                                ], spacing=3, expand=True
                            ),
                            ft.Row(
                                controls=[
                                    DigitButton(text="7", button_clicked=self.button_clicked),
                                    DigitButton(text="8", button_clicked=self.button_clicked),
                                    DigitButton(text="9", button_clicked=self.button_clicked),
                                    ActionButton(text="*", button_clicked=self.button_clicked),
                                ],spacing=3, expand=True
                            ),
                            ft.Row(
                                controls=[
                                    DigitButton(text="4", button_clicked=self.button_clicked),
                                    DigitButton(text="5", button_clicked=self.button_clicked),
                                    DigitButton(text="6", button_clicked=self.button_clicked),
                                    ActionButton(text="-", button_clicked=self.button_clicked),
                                ], spacing=3, expand=True
                            ),
                            ft.Row(
                                controls=[
                                    DigitButton(text="1", button_clicked=self.button_clicked),
                                    DigitButton(text="2", button_clicked=self.button_clicked),
                                    DigitButton(text="3", button_clicked=self.button_clicked),
                                    ActionButton(text="+", button_clicked=self.button_clicked),
                                ], spacing=3, expand=True
                            ),
                            ft.Row(
                                controls=[
                                    DigitButton(text=".",button_clicked=self.button_clicked),
                                    DigitButton(text="0", button_clicked=self.button_clicked),
                                    DigitButton(text="<", button_clicked=self.button_clicked),
                                    ActionButton(text="=", button_clicked=self.button_clicked),
                                ], spacing=3, expand=True
                            ),
                        ],spacing=2,
                    ),
                ),
            ], spacing=0
        )
    # asignar el modo
    def change_mode(self, e):
        self.mode = e.control.value # asigna a mode la base seleccionada
        self.reset()
        self.result.value = "0"
        self.operacion_viw.value = ""
        self.update()
    # logica principal
    def button_clicked(self, e):
        data = e.control.data
        #print(f"Button clicked with data = {data}") #imprime en consola el boton presionado
        if data == "<":
            self.borrar_caracter()#funsion para borar caracter
            
        if self.result.value == "Error" or data == "R":
            self.result.value = "0"
            self.operacion_viw.value = "" #reiniciamos la vista de la operacion
            self.reset()
            
        elif self.mode == "decimal" and data in ("A", "B", "C", "D", "E", "F"):
            return
        elif self.mode == "binario" and data not in ("0", "1", "+", "-", "*", "/", "R", "="):
            return
        elif self.mode == "octal" and data in ("8", "9", "A", "B", "C", "D", "E", "F", "." ):
            return
        elif self.mode == "hexadecimal" and data == ".":
            return

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "A", "B", "C", "D", "E", "F"):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("+", "-", "*", "/"):
            if self.new_operand:
                #para mostrar que se sigue operando con el resultado despues de darle igual
                self.operacion_viw.value = str(self.result.value) + f" {data} " #vista de operaciones
            else:
                self.operacion_viw.value += str(self.result.value) + f" {data} " #vista de operaciones
            # convertimos el segundo parametro de entrada llamando a la funcion convert_input
            self.result.value = self.calculate(
                self.operand1, float(self.convert_input(self.result.value)), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.convert_input(self.result.value))
            self.new_operand = True

        elif data in ("="):
            self.operacion_viw.value += str(self.result.value) + f" {data} " #vistra de operaciones
            #convertimos el segundo parametro de entrada llamando a la funcion convert_input
            self.result.value = self.calculate(
                self.operand1, float(self.convert_input(self.result.value)), self.operator
            )
            self.reset()
        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):
        if operator == "+":
            result = self.format_number(operand1 + operand2)
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                result = operand1 / operand2
            
        match self.mode:
            case "binario":
                return self.decimal_a_binario(result) if result != "Error" else "Error"
            case "octal":
                return self.decimal_a_octal(result) if result != "Error" else "Error"
            case "hexadecimal":
                return self.decimal_a_hexadecimal(result) if result != "Error" else "Error"
            case _:
                return round(self.format_number(result), 10) #despues
            
    # funcion de conversion principal    
    def convert_input(self, value):
        match self.mode:
            case "binario":
                return self.binario_a_decimal(value)
            case "octal":
                return self.octal_a_decimal(value)
            case "hexadecimal":
                return self.hexadecimal_a_decimal(value)
            case _:
                return float(value)
    
    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True
        
    def borrar_caracter(self):
            # Si result.value tiene contenido, borra el último carácter
            if self.result.value and self.result.value != "0":
                self.result.value = self.result.value[:-1]
                if not self.result.value:  # Si queda vacío, vuelve a "0"
                    self.result.value = "0"
            self.update()
            return
    
    # fuciones para operaciones con numero binarios
    def binario_a_decimal(self, binario):
        posicion = 0
        #Aqui almacenamos el resultado
        decimal = 0
        # reversed invertir la cadena porque debemos recorrerla de derecha a izquierda
        for digito in reversed(binario):
            if digito == "1":
                decimal = decimal + pow(2, posicion)
            posicion += 1
        return decimal
    
    def decimal_a_binario(self, decimal):
        if decimal <= 0:
            return "0"
        binario = ""
        while decimal > 0:
            # Saber si es 1 o 0
            residuo = int(decimal % 2)
            decimal = int(decimal / 2)
            binario = str(residuo) + binario
        return binario

    # funciones para operaciones con numeros octales
    def octal_a_decimal(self, octal):
        decimal = 0
        posicion = 0
        # reversed Inverte el octal, porque debemos recorrerlo de derecha a izquierda
        for digito in reversed(octal):
            #para evitar que aga operaciones con 0
            if digito != 0:
                decimal = decimal + int(int(digito)* int(pow(8, posicion)))
            posicion += 1
        return decimal

    def decimal_a_octal(self, decimal):
        octal = ""
        while decimal > 0:
            residuo = decimal % 8
            octal = str(residuo) + octal
            decimal = int(decimal / 8)
        return octal

    # funviones para operaciones con numeros hexadecimales
    def obtener_caracter_hexadecimal(self, valor):
        # Lo necesitamos como cadena
        valor = str(valor)
        equivalencias = {
            "10": "A",
            "11": "B",
            "12": "C",
            "13": "D",
            "14": "E",
            "15": "F",
        }
        if valor in equivalencias:
            return equivalencias[valor]
        else:
            return valor

    def decimal_a_hexadecimal(self, decimal):
        hexadecimal = ""
        while decimal > 0:
            residuo = decimal % 16
            verdadero_caracter = self.obtener_caracter_hexadecimal(residuo)
            hexadecimal = verdadero_caracter + hexadecimal
            decimal = int(decimal / 16)
        return hexadecimal

    def obtener_valor_real(self,  caracter_hexadecimal):
        equivalencias = {
            "F": 15,
            "E": 14,
            "D": 13,
            "C": 12,
            "B": 11,
            "A": 10,
        }
        if caracter_hexadecimal in equivalencias:
            return equivalencias[caracter_hexadecimal]
        else:
            return int(caracter_hexadecimal)

    def hexadecimal_a_decimal(self, hexadecimal):
        decimal = 0
        posicion = 0
        # La debemos recorrer del final al principio, así que la invertimos
        for digito in reversed(hexadecimal):
            # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
            valor = self.obtener_valor_real(digito)
            decimal = decimal + int(valor) * int(pow(16, posicion))
            posicion += 1
        return decimal

#funcion main principal
def main(page: ft.Page):
    page.title = "Calc App"
    page.bgcolor = ft.colors.BLACK
    page.window.width = 330  # Ancho de la ventana
    page.window.height = 700  # Alto de la ventana
    page.vertical_alignment= "center"
    page.horizontal_alignment= "center"
    page.appbar = ft.AppBar(
        #leading_width=50,
        toolbar_height= 30,
        title=ft.Text("Calculador"),
        center_title=False,
        bgcolor=ft.colors.BLACK,
        )
    # creamos una instacia de la aplicacion
    calc = CalculatorApp()

    # agregamos el control raíz de la aplicación a la página
    page.add(calc)

# para correr en escritorio
ft.app(target=main)