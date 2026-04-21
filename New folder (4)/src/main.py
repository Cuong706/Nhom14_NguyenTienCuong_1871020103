import sys
import os

# Thêm đường dẫn
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bfs_solver import bfs
from dfs_solver import dfs
from maps.maze_basic import maze as basic_maze
from maps.maze_hard import maze as hard_maze
from maps.maze_hard2 import maze as hard_maze2

def run_on_maze(maze, name):
    """Chạy BFS và DFS trên một bản đồ"""
    print(f"\n{'='*60}")
    print(f"🗺️  {name}")
    print(f"{'='*60}")
    
    print("\n▶️ BFS:")
    bfs(maze, 'default')
    
    print("\n▶️ DFS:")
    dfs(maze, 'default')

if __name__ == "__main__":
    print("\n=== ROBOT CỨU HỘ PCCC ===\n")
    
    # Chạy trên bản đồ cơ bản
    run_on_maze(basic_maze, "BẢN ĐỒ CƠ BẢN (5x5)")
    
    # Chạy trên bản đồ khó 10x10
    run_on_maze(hard_maze, "BẢN ĐỒ KHÓ 10x10 #1")
    
    # Chạy trên bản đồ cực khó 10x10
    run_on_maze(hard_maze2, "BẢN ĐỒ CỰC KHÓ 10x10 #2")