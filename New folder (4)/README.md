========================================
🤖 ROBOT CỨU HỘ PCCC - GIẢI THÍCH THUẬT TOÁN
========================================

1. BFS (Breadth-First Search) - Tìm kiếm theo chiều rộng
--------------------------------------------------------
- Dùng cấu trúc dữ liệu HÀNG ĐỢI (Queue) - FIFO (First In First Out)
- Nguyên lý: Duyệt hết các ô ở tầng hiện tại trước khi xuống tầng sau
- Ưu điểm: Luôn tìm được ĐƯỜNG ĐI NGẮN NHẤT
- Nhược điểm: Tốn NHIỀU BỘ NHỚ hơn vì phải lưu toàn bộ hàng đợi
- Ứng dụng: Tìm đường đi tối ưu cho robot cứu hộ

2. DFS (Depth-First Search) - Tìm kiếm theo chiều sâu
-----------------------------------------------------
- Dùng cấu trúc dữ liệu NGĂN XẾP (Stack) - LIFO (Last In First Out)
- Nguyên lý: Đi sâu vào một nhánh đến cùng, nếu bế tắc thì quay lui
- Ưu điểm: TIẾT KIỆM BỘ NHỚ hơn (chỉ lưu 1 nhánh)
- Nhược điểm: KHÔNG ĐẢM BẢO đường đi ngắn nhất, dễ lạc vào ngõ cụt
- Ứng dụng: Khi bộ nhớ bị giới hạn, không cần đường đi tối ưu

3. So sánh số ô đã duyệt (Visited Nodes)
----------------------------------------
- BFS: Duyệt theo lớp → thường duyệt NHIỀU ô hơn
- DFS: Đi sâu một nhánh → thường duyệt ÍT ô hơn

4. Ảnh hưởng của thứ tự ưu tiên các hướng
------------------------------------------
- BFS: KHÔNG ảnh hưởng đến tính tối ưu của đường đi
- DFS: ẢNH HƯỞNG LỚN đến đường đi (thay đổi hướng đầu tiên)

5. Kết luận cho Robot cứu hộ PCCC
---------------------------------
- Cần đường đi NGẮN NHẤT → Dùng BFS
- Bộ nhớ GIỚI HẠN → Dùng DFS
- Thời gian THỰC TẾ → BFS được ưu tiên hơn để cứu nạn nhân nhanh nhất

========================================
