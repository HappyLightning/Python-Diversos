from collections import deque

dq = deque(range(10), maxlen=10)  # maxlen define o numero máximo de itens permitido nessa instancia de deque
print(dq)
dq.rotate(3)  # fazer a rotação com n > 0 retira os itens da extremidade direita e os insere na esquerda;
# quando n < 0 os itens serão retirados da esquerda e concatenados à direita
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])  # adicionar tres itens à direita remove os valores -1, 1 e 2 mais à esquerda
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)
