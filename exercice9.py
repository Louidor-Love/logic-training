#Exercicio :Juego de carta
#https://www.youtube.com/watch?v=8lZ71NJYVuA

print('!Super bienvenido al Blacjack Love')
print('!aqui te presento las cartas')

# Palos y valores
palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def crear_baraja_d_52(palos,valores):
    baraja = []
    for palo in palos:
        for valor in valores:
            carta = f"{valor} + {palo}"  
            baraja.append(carta)
    return baraja

cartas = crear_baraja_d_52(palos,valores)
print(cartas)

