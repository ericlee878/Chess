## Two player chess in python with Pygame

import pygame
pygame.init()

from chess_constants import *
from chess_visuals import *

# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    
    return all_moves_list


# checks if it is legal for piece to move
def check_legal(position, color):
    if color == 'white':
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            # check if piece is pinned vertically or horizontally
            for i in range(4):
                path = True
                if i == 0:
                    xChange = 1
                    yChange = 0
                elif i == 1:
                    xChange = 0
                    yChange = 1
                elif i == 2:
                    xChange = 0
                    yChange = -1
                elif i == 3:
                    xChange = -1
                    yChange = 0
                xPos = position[0]
                yPos = position[1]
                # checking if king is on same row or column
                while path:
                    xPos += xChange
                    yPos += yChange
                    if not (0 <= xPos <= 7 and 0 <= yPos <= 7):
                        path = False
                    elif (xPos, yPos) == king_location:
                        path = False
                        # changing direction and checking if rook or queen is on other side of row or column
                        xChange = xChange * -1
                        yChange = yChange * -1
                        path_2 = True
                        xPos = position[0]
                        yPos = position[1]
                        while path_2:
                            xPos += xChange
                            yPos += yChange
                            if (xPos, yPos) in white_locations or not (0 <= xPos <= 7 and 0 <= yPos <= 7):
                                path_2 = False
                            elif (xPos, yPos) in black_locations:
                                index = black_locations.index((xPos, yPos))
                                piece = black_pieces[index]
                                if(piece == 'rook' or piece == 'queen'):
                                    return False
                                else:
                                    path_2 = False
            # check if piece is pinned diagonally
            for i in range(4):
                path = True
                if i == 0:
                    xChange = 1
                    yChange = 1
                elif i == 1:
                    xChange = -1
                    yChange = 1
                elif i == 2:
                    xChange = 1
                    yChange = -1
                elif i == 3:
                    xChange = -1
                    yChange = -1
                xPos = position[0]
                yPos = position[1]
                # checking if king is on same diagonal
                while path:
                    xPos += xChange
                    yPos += yChange
                    if not (0 <= xPos <= 7 and 0 <= yPos <= 7):
                        path = False
                    elif (xPos, yPos) == king_location:
                        path = False
                        # changing direction and checking if bishop or queen is on other side of diagonal
                        xChange = xChange * -1
                        yChange = yChange * -1
                        path_2 = True
                        xPos = position[0]
                        yPos = position[1]
                        while path_2:
                            xPos += xChange
                            yPos += yChange
                            if (xPos, yPos) in white_locations or not (0 <= xPos <= 7 and 0 <= yPos <= 7) :
                                path_2 = False
                            elif (xPos, yPos) in black_locations:
                                index = black_locations.index((xPos, yPos))
                                piece = black_pieces[index]
                                if(piece == 'bishop' or piece == 'queen'):
                                    return False
                                else:
                                    path_2 = False
    elif color == 'black':
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            # check if piece is pinned vertically or horizontally
            for i in range(4):
                path = True
                if i == 0:
                    xChange = 1
                    yChange = 0
                elif i == 1:
                    xChange = 0
                    yChange = 1
                elif i == 2:
                    xChange = 0
                    yChange = -1
                elif i == 3:
                    xChange = -1
                    yChange = 0
                xPos = position[0]
                yPos = position[1]
                # checking if king is on same row or column
                while path:
                    xPos += xChange
                    yPos += yChange
                    if not (0 <= xPos <= 7 and 0 <= yPos <= 7):
                        path = False
                    elif (xPos, yPos) == king_location:
                        path = False
                        # changing direction and checking if rook or queen is on other side of row or column
                        xChange = xChange * -1
                        yChange = yChange * -1
                        path_2 = True
                        xPos = position[0]
                        yPos = position[1]
                        while path_2:
                            xPos += xChange
                            yPos += yChange
                            if (xPos, yPos) in black_locations or not (0 <= xPos <= 7 and 0 <= yPos <= 7):
                                path_2 = False
                            elif (xPos, yPos) in white_locations:
                                index = white_locations.index((xPos, yPos))
                                piece = white_pieces[index]
                                if(piece == 'rook' or piece == 'queen'):
                                    return False
                                else:
                                    path_2 = False
            # check if piece is pinned diagonally
            for i in range(4):
                path = True
                if i == 0:
                    xChange = 1
                    yChange = 1
                elif i == 1:
                    xChange = -1
                    yChange = 1
                elif i == 2:
                    xChange = 1
                    yChange = -1
                elif i == 3:
                    xChange = -1
                    yChange = -1
                xPos = position[0]
                yPos = position[1]
                # checking if king is on same diagonal
                while path:
                    xPos += xChange
                    yPos += yChange
                    if not (0 <= xPos <= 7 and 0 <= yPos <= 7):
                        path = False
                    elif (xPos, yPos) == king_location:
                        path = False
                        # changing direction and checking if bishop or queen is on other side of diagonal
                        xChange = xChange * -1
                        yChange = yChange * -1
                        path_2 = True
                        xPos = position[0]
                        yPos = position[1]
                        while path_2:
                            xPos += xChange
                            yPos += yChange
                            if (xPos, yPos) in black_locations or not (0 <= xPos <= 7 and 0 <= yPos <= 7):
                                path_2 = False
                            elif (xPos, yPos) in white_locations:
                                index = white_locations.index((xPos, yPos))
                                piece = white_pieces[index]
                                if(piece == 'bishop' or piece == 'queen'):
                                    return False
                                else:
                                    path_2 = False
                
    return True

# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if(not check_legal(position, color)):
        return moves_list
    
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
           (position[0], position[1] + 1) not in black_locations and position[1] < 7:
               moves_list.append((position[0], position[1] + 1))
               if (position[0], position[1] + 2) not in white_locations and \
                  (position[0], position[1] + 2) not in black_locations and position[1] == 1:
                   moves_list.append((position[0], position[1] + 2))
        if(position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if(position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))

    if color == 'black':
        if (position[0], position[1] - 1) not in white_locations and \
           (position[0], position[1] - 1) not in black_locations and position[1] > 0:
               moves_list.append((position[0], position[1] - 1))
               if (position[0], position[1] - 2) not in white_locations and \
                  (position[0], position[1] - 2) not in black_locations and position[1] == 6:
                   moves_list.append((position[0], position[1] - 2))
        if(position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if(position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))

    return moves_list

# check rook moves
def check_rook(position, color):
    moves_list = []
    if(not check_legal(position, color)):
        return moves_list

    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    if color == 'black':
        friends_list = black_locations
        enemies_list = white_locations

    # up, down, left, right
    for i in range(4):
        path = True
        if i == 0:
            xChange = 1
            yChange = 0
        elif i == 1:
            xChange = 0
            yChange = 1
        elif i == 2:
            xChange = 0
            yChange = -1
        elif i == 3:
            xChange = -1
            yChange = 0
        xPos = position[0]
        yPos = position[1]
        while path:
            xPos += xChange
            yPos += yChange
            if(xPos, yPos) not in friends_list and 0 <= xPos <= 7 and 0 <= yPos <= 7:
                moves_list.append((xPos, yPos))
                if(xPos, yPos) in enemies_list:
                    path = False
            else:
                path = False
                
    return moves_list
            

# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if(not check_legal(position, color)):
        return moves_list
    
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    if color == 'black':
        friends_list = black_locations
        enemies_list = white_locations

    # northeast, northwest, southeast, southwest
    for i in range(4):
        path = True
        if i == 0:
            xChange = 1
            yChange = 1
        elif i == 1:
            xChange = -1
            yChange = 1
        elif i == 2:
            xChange = 1
            yChange = -1
        elif i == 3:
            xChange = -1
            yChange = -1
        xPos = position[0]
        yPos = position[1]
        while path:
            xPos += xChange
            yPos += yChange
            if(xPos, yPos) not in friends_list and 0 <= xPos <= 7 and 0 <= yPos <= 7:
                moves_list.append((xPos, yPos))
                if(xPos, yPos) in enemies_list:
                    path = False
            else:
                path = False
                
    return moves_list


# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if(not check_legal(position, color)):
        return moves_list
    
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    if color == 'black':
        friends_list = black_locations
        enemies_list = white_locations

    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)


    return moves_list


# check valid queen moves
def check_queen(position, color):
    if(not check_legal(position, color)):
        return []

    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    

    return moves_list


# check valid king moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7 and not is_square_attacked(color, target):
            moves_list.append(target)
    return moves_list



# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options



# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)

# draw captured pieces on side of screen
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50*i))

    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50*i))
        
# checks if given square is attacked by any of the opponents squares
def is_square_attacked(color, square):
    if color == 'white':
            for i in range(len(black_options)):
                if square in black_options[i]:
                    return True
    else:
            for i in range(len(white_options)):
                if square in white_options[i]:
                    return True

    return False
    

# checks if given color's kings is in check
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            position_of_king = white_locations[white_pieces.index('king')]
            if(is_square_attacked('white', position_of_king)):
                if counter < 25:
                       pygame.draw.rect(screen, 'dark red', [position_of_king[0] * 100 + 1,
                                                              position_of_king[1] * 100 +1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            position_of_king = black_locations[black_pieces.index('king')]
            if(is_square_attacked('black', position_of_king)):
                if counter < 25:
                       pygame.draw.rect(screen, 'dark blue', [position_of_king[0] * 100 + 1,
                                                              position_of_king[1] * 100 +1, 100, 100], 5)

def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'),
                (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'),
                (210, 240))


# checks if given king is in checkmate
def draw_checkmate():
    # if king is in check
    if turn_step < 2:
        if 'king' in white_pieces:
            position_of_king = white_locations[white_pieces.index('king')]
            for i in range(len(black_options)):
                if position_of_king in black_options[i]:
                    if check_king() is empty:
                        winner = 'black'
    # if king is in check
    else:
        if 'king' in black_pieces:
            position_of_king = black_locations[black_pieces.index('king')]
            for i in range(len(white_options)):
                if position_of_king in white_options[i]:
                    if check_king() is empty:
                        winner = 'white'

# main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(fps)
    if counter < 50:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if mouse right click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    winner = ''
                    # game variables and images
                    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                       (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    captured_pieces_white = []
                    captured_pieces_black = []
                    # resets options
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    #0 - whites turn no selection: 1 - whites turn piece selected: 2 - black turn no selection: 3 - black turn piece selected
                    turn_step = 0
                    selection = 100
                    valid_moves = []
            # defines coordinates of mouse click
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            
            # if it is white's turn
            if turn_step < 2:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                # if the click was on a white piece
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                # if the click was on a valid move and white piece has been selected
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    # if this move captured a black piece
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        # if king is gone
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    # resets options
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    # resets variables for next move
                    turn_step = 2
                    selection = 100
                    valid_moves = []

                    
            # if it is black's turn
            if turn_step >= 2:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                # if the click was on a black piece
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                # if the click was on a valid move and black piece has been selected
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    # if this move captured a white piece
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        # if king is gone
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    # resets options
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    # resets variables for next move
                    turn_step = 0
                    selection = 100
                    valid_moves = []

    if winner != '':
        game_over = True
        draw_game_over()
                
                    
    pygame.display.flip()
pygame.quit()
