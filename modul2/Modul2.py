import random


def create_board(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]



def display_board(board, player_pos, goal_pos):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i, j) == player_pos:
                print('A', end=' | ')
            elif (i, j) == goal_pos:
                print('O', end=' | ')
            else:
                print(board[i][j], end=' | ')
        print()
        if i < len(board) - 1:
            print('-' * (4 * len(board[i]) - 1))



def generate_positions(width, height):
    player_pos = (random.randint(0, width - 1), random.randint(0, height - 1))
    goal_pos = (random.randint(0, width - 1), random.randint(0, height - 1))
    while player_pos == goal_pos:
        goal_pos = (random.randint(0, width - 1),
                    random.randint(0, height - 1))
    return player_pos, goal_pos




def move_player(player_pos, move):
    x, y = player_pos
    if move == 'W':
        x -= 1
    elif move == 'S':
        x += 1
    elif move == 'A':
        y -= 1
    elif move == 'D':
        y += 1
    return (x, y)




def is_game_over(player_pos, goal_pos):
    return player_pos == goal_pos



def get_user_input(prompt): return input(prompt).upper()




def play_game():
    while True:
        width = int(input("Masukkan Lebar Papan Permainan: "))
        height = int(input("Masukkan Tinggi Papan Permainan: "))
        board = create_board(width, height)
        generate_attempts = 0  

        while generate_attempts < 3:  
            player_pos, goal_pos = generate_positions(width, height)
            

            print("Pilihan Posisi Baru:")
            display_board(board, player_pos, goal_pos)  

            regenerate = input(
                "Generate posisi baru untuk pemain dan tujuan? (Yes/No): ").upper()
            if regenerate != 'YES':
                break
            generate_attempts += 1

        while True:
            display_board(board, player_pos, goal_pos)  

            move = input("Masukkan Gerakan (W/S/A/D): ").upper()
            if move not in ['W', 'S', 'A', 'D']:
                print("Gerakan Tidak Valid. Anda Kalah!")
                break  
            new_player_pos = move_player(player_pos, move)

            if 0 <= new_player_pos[0] < width and 0 <= new_player_pos[1] < height:
                player_pos = new_player_pos

                if is_game_over(player_pos, goal_pos):
                   
                    display_board(board, player_pos, goal_pos)
                    print("Anda Menang!")
                    break  
            else:
                # Menampilkan goal_pos
                display_board(board, player_pos, goal_pos)
                print("Gerakan Tidak Valid, Anda Kalah!")
                break  

        play_again = input("Main lagi? (Yes/No): ").upper()
        if play_again != 'YES':
            break  


if __name__ == "__main__":
    play_game()
