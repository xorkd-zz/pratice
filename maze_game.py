import random

class MazeGame:
    def __init__(self, size=5):
        self.size = size
        self.maze = self.generate_maze()
        self.player_pos = [0, 0]
        self.exit_pos = [size-1, size-1]

    def generate_maze(self):
        # 0: 길, 1: 벽
        maze = [[0 for _ in range(self.size)] for _ in range(self.size)]
        
        # 랜덤하게 벽 생성
        for _ in range(self.size * 2):
            x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            maze[y][x] = 1
        
        # 시작점과 끝점은 길로 유지
        maze[0][0] = 0
        maze[self.size-1][self.size-1] = 0
        
        return maze

    def print_maze(self):
        for y in range(self.size):
            for x in range(self.size):
                if [y, x] == self.player_pos:
                    print('P', end=' ')  # 플레이어 위치
                elif [y, x] == self.exit_pos:
                    print('E', end=' ')  # 출구 위치
                elif self.maze[y][x] == 1:
                    print('🧱', end=' ')  # 벽
                else:
                    print('⬜', end=' ')  # 길
            print()

    def move(self, direction):
        x, y = self.player_pos
        
        # 상(U), 하(D), 좌(L), 우(R) 이동
        moves = {
            'U': [-1, 0],
            'D': [1, 0],
            'L': [0, -1],
            'R': [0, 1]
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

    def play(self):
        print("🎮 미로 찾기 게임에 오신 것을 환영합니다! 🗺️")
        print("목표: 'P'에서 'E'까지 이동하세요.")
        print("이동: U(위), D(아래), L(왼쪽), R(오른쪽)")
        
        while self.player_pos != self.exit_pos:
            self.print_maze()
            move = input("이동 방향을 입력하세요 (U/D/L/R): ").upper()
            
            if move not in ['U', 'D', 'L', 'R']:
                print("잘못된 입력입니다. U, D, L, R 중 하나를 입력하세요.")
                continue
            
            if not self.move(move):
                print("그 방향으로는 이동할 수 없습니다!")
        
        print("🎉 축하합니다! 미로를 탈출했습니다! 🏆")

def main():
    game = MazeGame()
    game.play()

if __name__ == "__main__":
    main()