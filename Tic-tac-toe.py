class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    
    def print_board(self):
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'X' if self.current_player == 'O' else 'O'
        else:
            print("¡Esa posición ya está ocupada!")
    
    def check_winner(self):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
        
        for a, b, c in win_combinations:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        
        if ' ' not in self.board:
            return 'Empate'
        
        return None

def main():
    juego = TicTacToe()
    
    print("¡Bienvenido al Tic-tac-toe Super Avanzado!")
    print("Para hacer un movimiento, ingresa un número del 0 al 8 según la siguiente disposición:")
    juego.print_board()
    
    while True:
        juego.print_board()
        print(f"Turno del jugador {juego.current_player}")
        movimiento = int(input("Ingresa tu movimiento: "))
        
        if movimiento < 0 or movimiento > 8:
            print("¡Movimiento inválido! Ingresa un número del 0 al 8.")
            continue
        
        juego.make_move(movimiento)
        
        ganador = juego.check_winner()
        if ganador:
            juego.print_board()
            if ganador == 'Empate':
                print("¡Es un empate!")
            else:
                print(f"¡El jugador {ganador} ha ganado!")
            break

if __name__ == "__main__":
    main()
