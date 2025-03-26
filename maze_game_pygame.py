import pygame
import random
import sys

class MazeGame:
    def __init__(self, size=10, tile_size=60):
        pygame.init()
        
        # 게임 설정
        self.size = size
        self.tile_size = tile_size
        self.screen_width = size * tile_size
        self.screen_height = size * tile_size
        
        # 색상 팔레트
        self.BACKGROUND = (240, 248, 255)  # 연한 하늘색 배경
        self.WALL_COLOR = (70, 70, 100)    # 어두운 회색 벽
        self.PATH_COLOR = (240, 240, 240)  # 밝은 회색 길
        self.PLAYER_COLOR = (255, 105, 180)  # 핑크색 플레이어
        self.EXIT_COLOR = (50, 205, 50)    # 밝은 초록색 출구

        # 게임 화면 설정
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('🌟 미로 탈출 게임 🌟')
        
        # 게임 요소 초기화
        self.maze = self.generate_maze()
        self.player_pos = [0, 0]
        self.exit_pos = [size-1, size-1]
        
        # 시계
        self.clock = pygame.time.Clock()
        
        # 폰트
        self.font = pygame.font.Font(None, 36)

    def generate_maze(self):
        # 0: 길, 1: 벽
        maze = [[0 for _ in range(self.size)] for _ in range(self.size)]
        
        # 랜덤하게 벽 생성
        for _ in range(self.size * 3):
            x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            maze[y][x] = 1
        
        # 시작점과 끝점은 길로 유지
        maze[0][0] = 0
        maze[self.size-1][self.size-1] = 0
        
        return maze

    def draw_maze(self):
        self.screen.fill(self.BACKGROUND)
        
        # 미로 타일 그리기
        for y in range(self.size):
            for x in range(self.size):
                rect = pygame.Rect(
                    x * self.tile_size, 
                    y * self.tile_size, 
                    self.tile_size, 
                    self.tile_size
                )
                
                if [y, x] == self.player_pos:
                    pygame.draw.rect(self.screen, self.PLAYER_COLOR, rect)
                elif [y, x] == self.exit_pos:
                    pygame.draw.rect(self.screen, self.EXIT_COLOR, rect)
                elif self.maze[y][x] == 1:
                    pygame.draw.rect(self.screen, self.WALL_COLOR, rect)
                else:
                    pygame.draw.rect(self.screen, self.PATH_COLOR, rect, 1)
        
        pygame.display.flip()

    def move(self, direction):
        x, y = self.player_pos
        
        # 상(U), 하(D), 좌(L), 우(R) 이동
        moves = {
            'UP': [-1, 0],
            'DOWN': [1, 0],
            'LEFT': [0, -1],
            'RIGHT': [0, 1]
        }
        
        dx, dy = moves.get(direction, [0, 0])
        new_x, new_y = x + dx, y + dy
        
        # 이동 가능 여부 체크
        if (0 <= new_x < self.size and 
            0 <= new_y < self.size and 
            self.maze[new_x][new_y] == 0):
            self.player_pos = [new_x, new_y]
            return True
        return False

    def show_message(self, message):
        text = self.font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.screen_width//2, self.screen_height//2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)

    def play(self):
        running = True
        game_won = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if not game_won and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move('UP')
                    elif event.key == pygame.K_DOWN:
                        self.move('DOWN')
                    elif event.key == pygame.K_LEFT:
                        self.move('LEFT')
                    elif event.key == pygame.K_RIGHT:
                        self.move('RIGHT')
            
            self.draw_maze()
            
            # 게임 승리 조건
            if self.player_pos == self.exit_pos:
                if not game_won:
                    self.show_message('🎉 축하합니다! 미로 탈출! 🏆')
                game_won = True
            
            self.clock.tick(10)  # 초당 프레임 제한
        
        pygame.quit()
        sys.exit()

def main():
    game = MazeGame()
    game.play()

if __name__ == "__main__":
    main()