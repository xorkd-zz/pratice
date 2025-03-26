import random
import time

class MazeGame:
    def __init__(self, size=10):
        self.size = size
        self.maze = None
        self.player_pos = None
        self.exit_pos = None
        self.moves_count = 0
        self.start_time = None
        self.generate_new_maze()

    def generate_new_maze(self):
        # 미로 생성 알고리즘 개선
        self.maze = [[0 for _ in range(self.size)] for _ in range(self.size)]
        
        # 테두리 벽 생성
        for i in range(self.size):
            self.maze[0][i] = 1
            self.maze[self.size-1][i] = 1
            self.maze[i][0] = 1
            self.maze[i][self.size-1] = 1
        
        # 랜덤 미로 생성 (벽 비율 조정)
        for _ in range(self.size * 3):
            x, y = random.randint(1, self.size-2), random.randint(1, self.size-2)
            self.maze[y][x] = 1
        
        # 출구와 입구 주변 경로 보장
        self.maze[1][1] = 0  # 시작점
        self.maze[self.size-2][self.size-2] = 0  # 출구점
        
        # 시작점과 출구 설정
        self.player_pos = [1, 1]
        self.exit_pos = [self.size-2, self.size-2]
        
        # 이동 카운트와 시간 초기화
        self.moves_count = 0
        self.start_time = time.time()

    def print_maze(self):
        print("\n🗺️ 현재 미로 (움직임: {}, 시간: {:.1f}초)".format(
            self.moves_count, 
            time.time() - self.start_time if self.start_time else 0
        ))
        
        for y in range(self.size):
            for x in range(self.size):
                if [y, x] == self.player_pos:
                    print('🧍', end=' ')  # 플레이어 위치
                elif [y, x] == self.exit_pos:
                    print('🏁', end=' ')  # 출구 위치
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
            self.moves_count += 1
            return True
        return False

    def play(self):
        print("🎮 미로 찾기 게임에 오신 것을 환영합니다! 🗺️")
        print("목표: 🧍에서 🏁까지 이동하세요.")
        print("이동: U(위), D(아래), L(왼쪽), R(오른쪽)")
        print("추가 명령어: NEW(새 맵), RESTART(현재 맵 다시 시작)")
        
        while self.player_pos != self.exit_pos:
            self.print_maze()
            move = input("이동 방향을 입력하세요 (U/D/L/R/NEW/RESTART): ").upper()
            
            if move == 'NEW':
                print("🔄 새로운 미로를 생성합니다!")
                self.generate_new_maze()
                continue
            
            if move == 'RESTART':
                print("🔁 현재 미로를 다시 시작합니다!")
                self.player_pos = [1, 1]
                self.moves_count = 0
                self.start_time = time.time()
                continue
            
            if move not in ['U', 'D', 'L', 'R']:
                print("잘못된 입력입니다. U, D, L, R, NEW, RESTART 중 하나를 입력하세요.")
                continue
            
            if not self.move(move):
                print("그 방향으로는 이동할 수 없습니다!")
        
        print("🎉 축하합니다! 미로를 탈출했습니다! 🏆")
        print("총 움직임 횟수: {}, 소요 시간: {:.1f}초".format(
            self.moves_count, 
            time.time() - self.start_time
        ))

def main():
    game = MazeGame()
    game.play()

if __name__ == "__main__":
    main()