import os
import re

def check_git_patch_folder(keyword, output_file):
    matching_files = []
    comment_patterns = [
        r'#.*',       # Python style comments
        r'//.*',      # C/C++/Java style comments
        r'/\*.*?\*/'  # C/C++/Java multi-line comments
    ]
    
    # Duyệt qua các file trong thư mục hiện tại
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.patch'):  # Kiểm tra các file có đuôi .patch
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')
                    for line in lines:
                        if keyword.lower() in line.lower():
                            is_comment = False
                            for pattern in comment_patterns:
                                if re.match(pattern, line.strip()):
                                    is_comment = True
                                    break
                            if not is_comment:
                                matching_files.append(file_path)
                                break
    
    # Ghi các file phù hợp vào file txt
    with open(output_file, 'w', encoding='utf-8') as f:
        for file in matching_files:
            f.write(file + '\n')

if __name__ == "__main__":
    keyword = "bromite"
    output_file = "matching_files.txt"
    check_git_patch_folder(keyword, output_file)
    print(f"Đã hoàn tất! Kiểm tra file {output_file} để xem kết quả.")
