import tkinter as tk
import random

class MazeGame:
    def __init__(self, master, size=5):
        self.master = master
        master.title("🧭 미로 찾기 게임")
        
        self.size = size
        self.cell_size = 100
        
        # 미로 생성
        self.maze = self.generate_maze()
        
        # 플레이어와 탈출 지점 초기화
        self.player_pos = [0, 0]
        self.exit_pos = [size-1, size-1]
        
        # Canvas 설정
        self.canvas = tk.Canvas(
            master, 
            width=self.size*self.cell_size, 
            height=self.size*self.cell_size
        )
        self.canvas.pack(padx=20, pady=20)
        
        # 상태 레이블
        self.status_label = tk.Label(
            master, 
            text="미로를 탈출하세요!", 
            font=("Arial", 16)
        )
        self.status_label.pack(pady=10)
        
        # 키보드 이벤트 바인딩
        master.bind('<Up>', lambda e: self.move('U'))
        master.bind('<Down>', lambda e: self.move('D'))
        master.bind('<Left>', lambda e: self.move('L'))
        master.bind('<Right>', lambda e: self.move('R'))
        
        # 미로 그리기
        self.draw_maze()

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

    def draw_maze(self):
        self.canvas.delete("all")
        
        # 미로 셀 그리기
        for y in range(self.size):
            for x in range(self.size):
                x1 = x * self.cell_size
                y1 = y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # 벽 그리기
                if self.maze[y][x] == 1:
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2, 
                        fill='gray', outline='black'
                    )
                else:
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2, 
                        fill='white', outline='black'
                    )
        
        # 플레이어 그리기
        px1 = self.player_pos[1] * self.cell_size
        py1 = self.player_pos[0] * self.cell_size
        px2 = px1 + self.cell_size
        py2 = py1 + self.cell_size
        self.canvas.create_oval(
            px1+10, py1+10, px2-10, py2-10, 
            fill='green', outline='black'
        )
        
        # 탈출 지점 그리기
        ex1 = self.exit_pos[1] * self.cell_size
        ey1 = self.exit_pos[0] * self.cell_size
        ex2 = ex1 + self.cell_size
        ey2 = ey1 + self.cell_size
        self.canvas.create_oval(
            ex1+10, ey1+10, ex2-10, ey2-10, 
            fill='red', outline='black'
        )

    def move(self, direction):
        x, y = self.player_pos
        
        # 방향에 따른 이동
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
            self.draw_maze()
            
            # 탈출 체크
            if self.player_pos == self.exit_pos:
                self.status_label.config(
                    text="🎉 축하합니다! 미로 탈출 성공! 🏆", 
                    fg='green'
                )
        else:
            self.status_label.config(
                text="그 방향으로는 이동할 수 없습니다!", 
                fg='red'
            )

def main():
    root = tk.Tk()
    game = MazeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()