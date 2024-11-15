import os


def generate_directory_tree(root_dir, indent="", is_last=True, output_file=None):
    """递归生成目录树并写入文件"""
    # 获取该目录下的所有文件和子目录
    items = os.listdir(root_dir)
    # 过滤掉隐藏文件/目录
    items = [item for item in items if not item.startswith('.')]
    item_count = len(items)

    for index, item in enumerate(items):
        # 判断是否为最后一个文件/目录
        is_last_item = (index == item_count - 1)
        # 生成目录路径
        item_path = os.path.join(root_dir, item)

        # 生成当前目录/文件字符串
        connector = "└── " if is_last_item else "├── "
        line_print = indent + connector + item
        line = line_print + "\n"
        if output_file is None:
            # 将输出写入文件
            print(line_print)
        elif output_file is not None:
            output_file.write(line)

        # 如果是目录，递归生成子目录和文件
        if os.path.isdir(item_path):
            sub_indent = "    " if is_last_item else "│   "
            generate_directory_tree(item_path, indent + sub_indent, is_last_item, output_file)


def print_directory_tree(directory):
    generate_directory_tree(directory)


def save_directory_tree(directory, output_file_path):
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(directory + "/\n")
        generate_directory_tree(directory, output_file=output_file)
    print(f"目录树已保存到:{output_file_path}")


# 示例调用
if __name__ == "__main__":
    # 指定要展示的目录路径
    directory = r"D:\桌面\励志奖学金相关材料\励志奖学金+计221-2+人数\杨文彬国励志申请表"
    output_file_path = "directory_tree.txt"
    # 只打印
    print_directory_tree(directory)
    # 只保存
    # save_directory_tree(directory, output_file_path)
