@echo off
echo ========================================================
echo   Auto Build Script for Excel Text Finder (PyInstaller)
echo ========================================================
echo.

:: Kiểm tra và tiến hành cài đặt thư viện PyInstaller nếu chưa có
echo [1/3] Kiem tra Pyinstaller...
pip install pyinstaller
echo.

:: Dọn dẹp các thư mục build cũ (nếu có) để tránh xung đột
echo [2/3] Don dep cache...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "ExcelTextFinder.spec" del "ExcelTextFinder.spec"
echo.

:: Build ứng dụng
:: Giải thích các cờ (flags):
:: --noconsole: Ẩn màn hình Terminal đen khi chạy file exe (thích hợp cho GUI App)
:: --onefile: Gom tất cả các file phụ thuộc vào duy nhất 1 file .exe
:: --name: Đổi tên file exe thành "ExcelTextFinder.exe" thay vì "main.exe"
:: --hidden-import: Cố tình yêu cầu quét cả 2 package "gui" và "core" đề phòng lỗi Not Found Module của PyInstaller
echo [3/3] Bat dau tien trinh Build ra Executable ...
pyinstaller --noconsole --onefile --clean --hidden-import gui --hidden-import core --name "ExcelTextFinder" main.py
echo.

echo ========================================================
echo   [HOAN TAT] Ban co the tim thay file chay tai muc "\dist\ExcelTextFinder.exe"
echo ========================================================
pause
