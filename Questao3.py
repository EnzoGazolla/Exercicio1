
#Exercício 3: Escreva um programa que imprima os primeiros 10 números da sequência de Fibonacci.

n_termos = 11
a , b = 0, 1

print( 'Sequencia de Fibonacci')

for _ in range(n_termos):
print(a)
a, b = b, a + b