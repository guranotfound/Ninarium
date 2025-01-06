#!/bin/bash

directory="/d/chromium/src/patches"  # Thư mục chứa các file patch

for file in "$directory"/*.patch; do
    if [ -f "$file" ]; then
        echo "Đang áp dụng patch: $file"
        git am "$file"
        if [ $? -ne 0 ]; then
            echo "Lỗi khi áp dụng patch: $file. Bỏ qua patch này..."
            git am --skip
        else
            echo "Đã áp dụng patch: $file"
        fi
    fi
done
