from collections import deque
from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path

def bfs(maze, order='default'):
    """
    Thuật toán BFS sử dụng Queue (Hàng đợi)
    
    Tham số:
        maze: ma trận bản đồ
        order: thứ tự ưu tiên các hướng
    
    Trả về:
        path: đường đi từ S đến G
        visited_count: số ô đã duyệt
    """
    start, goal = get_start_goal(maze)
    
    if start is None or goal is None:
        print("Lỗi: Không tìm thấy điểm S hoặc G trong bản đồ!")
        return None, 0
    
    # Queue lưu (vị trí hiện tại, đường đi đến đó)
    queue = deque([(start, [start])])
    
    # Tập hợp các ô đã visited
    visited = set([start])
    
    print(f"\n{'='*50}")
    print(f"🚀 BFS BẮT ĐẦU - Thứ tự: {order}")
    print(f"📍 Start: {start}, 🎯 Goal: {goal}")
    print(f"{'='*50}")
    
    step = 0
    while queue:
        step += 1
        current, path = queue.popleft()
        
        # Kiểm tra nếu đã đến đích
        if current == goal:
            print(f"\n✅ BFS: TÌM THẤY ĐÍCH sau {step} bước duyệt!")
            print_maze_with_path(maze, path, len(visited))
            return path, len(visited)
        
        # Duyệt các ô lân cận
        neighbors = get_neighbors(maze, current, order)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    print(f"\n❌ BFS: KHÔNG tìm thấy đường đi đến đích!")
    print(f"📊 Tổng số ô đã duyệt: {len(visited)}")
    return None, len(visited)