def somar(a,b):
    return a + b
def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    if b == 0:
        raise ValueError("Não é possível dividir porrr zero.")
    return a / b
def calcular_desconto(preco, percentual): 
    desconto = preco * (percentual / 100)
    return preco - desconto