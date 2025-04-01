__author__  = "Lukas Bajic"
__version__ = "3.12.5"
__email__   = "Lukas.lindbajic@elev.ga.ntig.se"

import pygame  # Importerar Pygame-biblioteket.
import random  # Importerar Pythons inbyggda random-bibliotek.
import os #Används för highscore filen 

# Färger
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

HIGH_SCORE_FILE = "highscore.txt" #Skapar en fil med alla tidigare highscores 

def load_high_score(): #Läser av det högsta highscore från filen
    if os.path.exists(HIGH_SCORE_FILE): #Om filenvägen finns så öppnas den och läser av den
        with open(HIGH_SCORE_FILE, "r") as file: 
            return int(file.read()) #Laddar och retunerar highscore i heltal 
    return 0 #Om filen inte finns så retuneras 0 

def save_high_score(score): #Sparar en ny highscore 
    with open(HIGH_SCORE_FILE, "w") as file: 
        file.write(str(score)) #Skriver den nya highscoren till filen

def main():
    width, height, mines = 10, 10, 10 #Skriver ut bredden x höjden som brädan ska vara samt hur många miner som ska va på brädan 
    pygame.init() #Startar spelet 
    cell_size = 30 #Storlek på varje ruta i pixlar 
    screen = pygame.display.set_mode((width * cell_size, height * cell_size + 40)) #Skapar ett fönster där spelet blir displayat 
    pygame.display.set_caption("Minesweeper") #namnger spelet 
    game = Minesweeper(width, height, mines) #Läser in bredden och höjden på brädan samt hur många miner på brädan som är random genererat
    running = True #Sätter igång spelet genom att göra variabeln running till true 
    high_score = load_high_score() #Laddar in tidigare highscore från filen 
    
    while running: #while loop medans spelet körs while running = true  
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #Om man stänger fönster ruttan så stängs spelet 
                running = False 
            elif event.type == pygame.MOUSEBUTTONDOWN: #Gör en elif för vad som ska hända om man trycker på höger eller vänster mustaggent
                x, y = pygame.mouse.get_pos() #Hämtar mustrycktes position på bräddan när den trycks ned
                if y >= height * cell_size: #Ignorerar mustryck utanför brädans diametrar
                    continue  # Ignorera klick utanför spelbrädan
                x //= cell_size #Omvandlar pixlar till rutnummer
                y //= cell_size
                if 0 <= x < width and 0 <= y < height: #Kontrollerar om koordinaterna är inom spelbrädets gränser.
                    if event.button == 1: #Vad som händer när du trycker på vänstra musknappen 
                        if game.reveal_cell(x, y):
                            print("Game Over! You hit a mine.")
                            if game.score > high_score: #Om ditt nya score är högre en tidigare highscore 
                                high_score = game.score 
                                save_high_score(high_score) #Sparar nya highscore i filen "Highscore"
                            game = Minesweeper(width, height, mines)
                    elif event.button == 3: #Vad som händer när du trycker på högra musknappen 
                        game.toggle_flag(x, y) #Du flaggar alla miner
        
        screen.fill(WHITE) 
        game.draw_board(screen)
        
        font = pygame.font.SysFont(None, 30) #Skapar ett font objekt som används för att rendera text och dess textstorlek i pixlar 
        score_text = font.render(f"Score: {game.score}  High Score: {high_score}", True, BLACK) #Genererar vad som ska stå i fonten och textens färg 
        screen.blit(score_text, (10, height * cell_size + 10)) #Ritar texten på spelet (10, height * cell_size + 10) kordinater vart texten ska stå 
        
        pygame.display.flip() #Uppdaterar skärmen efter man gör en ändrings så som en tryck eller uppdatering av din score 
    
    pygame.quit() #

class Minesweeper:
    def __init__(self, width, height, mines): #Skapar en spelplan
        self.width = width 
        self.height = height
        self.mines = mines
        self.cell_size = 30
        self.board = [[0 for _ in range(width)] for _ in range(height)] 
        self.visible = [[False for _ in range(width)] for _ in range(height)] #Håller koll på vilka ruter som har blivit revelade inom brädan 
        self.flagged = [[False for _ in range(width)] for _ in range(height)] #Håller koll på vilka ruter som har blivit flaggade inom brädan 
        self.score = 0
        self.generate_board()

    def generate_board(self):
        mines = random.sample([(x, y) for x in range(self.width) for y in range(self.height)], self.mines) #Genererar miner random inom spel brädan 
        for x, y in mines: 
            self.board[y][x] = -1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and self.board[ny][nx] != -1:
                        self.board[ny][nx] += 1 #Värderna på ruterna runtom minerna går upp 

    def reveal_cell(self, x, y): #revealar vad det är du trycker på brädan som flaggade miner eller nummer 
        if self.visible[y][x] or self.flagged[y][x]:
            return False
        self.visible[y][x] = True
        if self.board[y][x] == -1:
            return True
        self.score += 1
        if self.board[y][x] == 0:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal_cell(nx, ny)
        return False

    def toggle_flag(self, x, y):
        if not self.visible[y][x]:
            self.flagged[y][x] = not self.flagged[y][x]

    def draw_board(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                if self.visible[y][x]:
                    if self.board[y][x] == -1:
                        pygame.draw.rect(screen, RED, rect)
                        pygame.draw.circle(screen, WHITE, rect.center, self.cell_size // 3)
                    elif self.board[y][x] == 0:
                        pygame.draw.rect(screen, GRAY, rect)
                    else:
                        pygame.draw.rect(screen, GRAY, rect)
                        color = [BLACK, GREEN, PURPLE, ORANGE, YELLOW, CYAN][self.board[y][x]]
                        font = pygame.font.SysFont(None, 20)
                        text = font.render(str(self.board[y][x]), True, color)
                        text_rect = text.get_rect(center=rect.center)
                        screen.blit(text, text_rect)
                else:
                    pygame.draw.rect(screen, GRAY, rect)
                    pygame.draw.rect(screen, BLACK, rect, 1)
                if self.flagged[y][x]:
                    font = pygame.font.SysFont(None, 20)
                    text = font.render("F", True, BLUE)
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)

if __name__ == "__main__":
    main()
