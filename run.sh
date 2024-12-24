#!/bin/bash
HIM="Чиковани Давид"
BASE_DIR=$(pwd)

find "$BASE_DIR" -type d -name "check" | grep "2024" | while read -r CHECK_DIR; do
    FILE_PATH="$CHECK_DIR/remote"
    RELATIVE_PATH=$(cd "$CHECK_DIR" && pwd | sed "s|$BASE_DIR/||" | sed 's|/check$||')
    cat << EOF > "$FILE_PATH"
[remote]
"$HIM:$RELATIVE_PATH/1" = []
"$HIM:$RELATIVE_PATH/2" = []
"$HIM:$RELATIVE_PATH/3" = []
EOF

    echo "Файл создан: $FILE_PATH"
done
