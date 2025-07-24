import os

def list_project_structure(root_dir, indent=''):
    """
    递归地列出指定目录下（项目）的文件和文件夹结构。

    Args:
        root_dir (str): 要遍历的根目录路径。
        indent (str): 用于缩进的字符串，内部使用。
    """
    if not os.path.exists(root_dir):
        print(f"错误：路径 '{root_dir}' 不存在。")
        return

    # 获取当前目录下的所有文件和文件夹
    items = sorted(os.listdir(root_dir))

    for i, item in enumerate(items):
        item_path = os.path.join(root_dir, item)
        # 判断是最后一个文件/文件夹，用于绘制不同的连接符
        is_last = (i == len(items) - 1)

        # 打印当前项
        if os.path.isdir(item_path):
            print(f"{indent}{'└── ' if is_last else '├── '}{item}/")
            # 递归调用自身，增加缩进
            next_indent = indent + ('    ' if is_last else '│   ')
            list_project_structure(item_path, next_indent)
        else:
            print(f"{indent}{'└── ' if is_last else '├── '}{item}")


