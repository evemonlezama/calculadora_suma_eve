from nicegui import ui
import os

def sumar():
    try:
        n1 = float(num1.value)
        n2 = float(num2.value)
        resultado.text = f'Resultado: {n1 + n2}'
    except:
        resultado.text = 'Ingresa numeros validos'

def limpiar():
    num1.value = ''
    num2.value = ''
    resultado.text = 'Resultado: 0'

with ui.column().classes('w-full h-screen items-center justify-center').style('background-color:#233;'):
    with ui.card().style('width:400px; background-color:#00233B;').classes('items-center'):
        ui.label('CALCULADORA DE SUMA').style('color:white; font-size:22px; font-weight:bold')
        
        num1 = ui.input('Ingresa el primer numero').props('dark outlined').style('width:350px; color:white')
        num2 = ui.input('Ingresa el segundo numero').props('dark outlined').style('width:350px; color:white')
        
        with ui.row().classes('w-full justify-center no-wrap').style('gap:10px;'):
            ui.button('Sumar', icon='calculate', color='green', on_click=sumar).style('width:140px')
            ui.button('LIMPIAR', icon='delete', color='red', on_click=limpiar).style('width:140px')
        
        resultado = ui.label('Resultado: 0').style('color:white; font-size:20px')

port = int(os.environ.get("PORT", 8080))
ui.run(host='0.0.0.0', port=port, title='Calculadora Suma')