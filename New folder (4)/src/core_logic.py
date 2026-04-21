def get_start_goal(maze):
    """Tìm vị trí Start (S) và Goal (G) trong maze"""
    start = None
    goal = None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'G':
                goal = (r, c)
    return start, goal

def get_neighbors(maze, node, order='default'):
    """
    Lấy các ô lân cận hợp lệ
    
    order: 'default' (Lên, Xuống, Trái, Phải)
           'right_first' (Phải, Xuống, Trái, Lên)
           'down_first' (Xuống, Lên, Phải, Trái)
    """
    directions = []
    if order == 'default':
        # Thứ tự mặc định: Lên, Xuống, Trái, Phải
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif order == 'right_first':
        # Ưu tiên Phải trước: Phải, Xuống, Trái, Lên
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    elif order == 'down_first':
        # Ưu tiên Xuống trước: Xuống, Lên, Phải, Trái
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    else:
        # Mặc định
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    neighbors = []
    r, c = node
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
            # Kiểm tra ô có phải là tường (1) không
            if maze[nr][nc] != 1:
                neighbors.append((nr, nc))
    return neighbors

def print_maze_with_path(maze, path, visited_count):
    """In maze với đường đi được đánh dấu"""
    print(f"\n--- TÌM THẤY ĐÍCH! Đã duyệt qua {visited_count} ô ---")
    print(f"--- Độ dài đường đi: {len(path)} bước ---")
    
    maze_copy = [row[:] for row in maze]
    
    # Đánh dấu đường đi bằng dấu '+'
    if path:
        for r, c in path:
            if maze_copy[r][c] not in ['S', 'G']:
                maze_copy[r][c] = '+'
    
    # In bản đồ với chỉ số
    print("\n    ", end="")
    for j in range(len(maze[0])):
        print(f"{j:2d}", end=" ")
    print("\n    " + "-" * (len(maze[0]) * 3))
    
    for i, row in enumerate(maze_copy):
        print(f"{i:2d} | ", end="")
        for cell in row:
            if cell == 1:
                print("██", end=" ")  # Tường
            elif cell == 0:
                print(". ", end=" ")  # Đường đi chưa đi
            elif cell == '+':
                print("+ ", end=" ")  # Đường robot đã đi
            elif cell == 'S':
                print("S ", end=" ")  # Start
            elif cell == 'G':
                print("G ", end=" ")  # Goal
        print()
    print("-" * 40)

def print_visited_comparison(bfs_visited, dfs_visited, bfs_path_len, dfs_path_len):
    """So sánh kết quả BFS và DFS"""
    print("\n" + "="*50)
    print("📊 SO SÁNH BFS VS DFS")
    print("="*50)
    print(f"📈 Số ô đã duyệt (Visited Nodes):")
    print(f"   🟢 BFS: {bfs_visited} ô")
    print(f"   🔵 DFS: {dfs_visited} ô")
    
    if bfs_visited < dfs_visited:
        print(f"   ✅ BFS duyệt ít hơn DFS {dfs_visited - bfs_visited} ô")
        print(f"   → BFS tối ưu bộ nhớ hơn trong trường hợp này")
    elif dfs_visited < bfs_visited:
        print(f"   ✅ DFS duyệt ít hơn BFS {bfs_visited - dfs_visited} ô")
        print(f"   → DFS tối ưu bộ nhớ hơn trong trường hợp này")
    else:
        print(f"   → Hai thuật toán duyệt số ô bằng nhau")
    
    print(f"\n📏 Độ dài đường đi:")
    print(f"   🟢 BFS: {bfs_path_len} bước (Đường đi ngắn nhất ✓)")
    print(f"   🔵 DFS: {dfs_path_len} bước")
    
    print(f"\n💾 Kết luận về bộ nhớ:")
    if bfs_visited > dfs_visited:
        print(f"   → DFS TIẾT KIỆM BỘ NHỚ HƠN vì chỉ cần lưu stack (1 nhánh)")
        print(f"   → BFS tốn nhiều bộ nhớ hơn vì phải lưu toàn bộ hàng đợi")
    else:
        print(f"   → BFS TIẾT KIỆM BỘ NHỚ HƠN trong trường hợp này")
        print(f"   → DFS có thể bị lạc vào ngõ cụt và duyệt nhiều ô hơn")