# Excel Text Finder

Excel Text Finder là một ứng dụng Desktop (giao diện đồ họa) được viết bằng Python. Công cụ này giúp người dùng dễ dàng tìm kiếm từ khóa hoặc đoạn văn bản cụ thể bên trong nhiều tệp Excel (định dạng `.xlsx`) cùng một lúc. Đặc biệt, kết quả sau khi tìm kiếm sẽ được xuất thông minh ra một file báo cáo Excel riêng, trong đó tự động gắn hyperlink tới vị trí tìm thấy và bôi đỏ từ khóa gốc.

## Tính Năng Chính
* **Quét Thư Mục Thông Minh**: Tự động tìm tất cả các file `.xlsx` trong một thư mục đã chọn.
* **Tùy Chọn Tìm Kiếm Khu Vực**: 
  * Chọn / Bỏ chọn từng file Excel cụ thể muốn tìm kiếm.
  * Hỗ trợ tìm kiếm theo kiểu **Khớp toàn bộ ô (Exact match)** hoặc tìm kiếm chuỗi con.
  * Hỗ trợ thứ tự quét dữ liệu: Ưu tiên quét theo hàng (Rows) hoặc độ ưu tiên quét theo cột (Columns).
* **Hiệu Suất Tốt, Không Đơ Giao Diện**: Việc quét và tìm kiếm file được đẩy vào chạy dưới nền (background threads), do đó sẽ không gây đóng băng (freeze) giao diện trong quá trình xử lý khối lượng lớn file.
* **Xuất Báo Cáo Excel Trực Quan**: 
  * Báo cáo bao gồm: Từ khóa tìm kiếm, Tên File, Tên Sheet, Vị Trí Cell, Context kết quả.
  * Tạo **Hyperlink** mở trực tiếp ngay tọa độ dòng/cột của file Excel gốc.
  * **Highlight Text**: Text kết quả trong báo cáo sẽ tự động được bôi đỏ (`red`) ngay ở vị trí tìm thấy từ khóa tìm kiếm.

## Cấu Trúc Mã Nguồn (Source Code Structure)

Dự án được cố tình phân tách thành 2 module chính là: **Giao diện người dùng (GUI)** và **Lõi phân tích liệu dữ (Core)**, giúp mã nguồn trở nên gọn gàng, module hóa và dễ bảo trì.

```
excel_finder/
│
├── main.py                  # Điểm bắt đầu (Entry point). Khởi chạy cấu trúc Tkinter UI App.
├── requirements.txt         # File chứa danh sách thư viện phụ thuộc (openpyxl, xlsxwriter...).
├── README.md                # Tài liệu dự án.
│
├── core/                    # [Backend/Logic Layer] Chứa các logic tính toán và xử lý file Excel
│   ├── __init__.py
│   ├── scanner.py           # Quét thư mục được chỉ định và trả về tất cả những file .xlsx.
│   ├── excel_processor.py   # ("Trái tim" của hệ thống). Dùng thư viện `openpyxl` ở chế độ read_only giúp tiết kiệm ram, quét sâu vào từng hàng/cột của các file Excel để dò tìm từ khóa.
│   └── excel_exporter.py    # Nhận dữ liệu kết quả, sử dụng thư viện `xlsxwriter` tạo bảng, định dạng màu, làm hyperlink và ghi file báo cáo.
│
└── gui/                     # [Presentation Layer] Chứa các Component của giao diện Tkinter
    ├── __init__.py
    ├── app.py               # `AppWindow`: Cửa sổ trung tâm, chịu trách nhiệm "gom" các panel nhỏ và là cầu nối tương tác với module `core` bằng threading.
    ├── search_panel.py      # Panel hiển thị khung chọn Folder, hộp nhập từ khóa Keyword và các option tìm kiếm (Radio buttons, Checkbox).
    └── file_list.py         # Danh sách hiển thị file trực quan đi kèm tính năng Checkbox (Select All / Deselect All).
```

## Cách Hoạt Động (Flow)
1. **Khởi chạy**: Người dùng chạy `python main.py`, nó sẽ tạo ra giao diện thông qua class `AppWindow` trong thư mục `gui`.
2. **Chọn Folder**: Người dùng load folder chứa Excel. Hàm trong `core/scanner.py` sẽ trả về danh sách các tệp, và giao diện cập nhật danh sách hiển thị qua `file_list.py`.
3. **Thực thi tìm kiếm**:
   * Giao diện lấy các Option search.
   * Gửi danh sách file gốc sang `core/excel_processor.py`, quá trình này chạy trên thread riêng biệt.
   * `excel_processor` sẽ quét toàn bộ và nhả lại Array Object.
   * Chuyển array vào trong `core/excel_exporter.py`. Module tiến hành ghi toàn bộ thành một file `ExcelSearchResult_xxx.xlsx` mới ở chính root folder chỉ định.
   * Thông báo lại Message Box Alert trên giao diện người dùng.
