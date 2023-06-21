import streamlit as st

# Título do aplicativo
st.title('Calculadora')

# Entrada dos números
num1 = st.number_input('Digite o primeiro número:', value=0.0)
num2 = st.number_input('Digite o segundo número:', value=0.000000001)

# Operações matemáticas
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2

# Botões para realizar as operações
if st.button('Adicionar'):
    st.write(f'Resultado da adição: {add_result}')
if st.button('Subtrair'):
    st.write(f'Resultado da subtração: {sub_result}')
if st.button('Multiplicar'):
    st.write(f'Resultado da multiplicação: {mul_result}')
if st.button('Dividir'):
    st.write(f'Resultado da divisão: {div_result}')
