import os

from config import *

def _print_output(message: str, output_file: str = None):
    """
    辅助函数：根据 output_file 参数将消息打印到控制台或写入文件。
    """
    if output_file:
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
    else:
        print(message)

def list_project_structure(root_dir: str = None ,
                           indent: str = '',
                           output_file: str = None,
                           ignore_dirs: list = []):
    """
    递归地列出指定目录下（项目）的文件和文件夹结构，支持输出到文件和忽略特定文件夹。

    Args:
        root_dir (str): 要遍历的根目录路径。
        indent (str): 用于缩进的字符串，内部使用。
        output_file (str, optional): 输出文件的路径。如果提供，内容将写入此文件。
                                     如果为 None，则打印到控制台。默认为 None。
        ignore_dirs (list, optional): 一个字符串列表，包含要忽略的文件夹名称。
                                      例如：['__pycache__', '.git', 'venv']。默认为 None。
    """
    if not os.path.exists(root_dir):
        _print_output(f"错误：路径 '{root_dir}' 不存在。", output_file)
        return

    # 获取当前目录下的所有文件和文件夹，并过滤掉忽略的文件夹
    items = sorted([item for item in os.listdir(root_dir)
                    if os.path.isdir(os.path.join(root_dir, item)) and item not in ignore_dirs or \
                       os.path.isfile(os.path.join(root_dir, item))])


    for i, item in enumerate(items):
        item_path = os.path.join(root_dir, item)
        # 判断是最后一个文件/文件夹，用于绘制不同的连接符
        is_last = (i == len(items) - 1)

        # 打印当前项
        prefix = f"{indent}{'└── ' if is_last else '├── '}"
        if os.path.isdir(item_path):
            _print_output(f"{prefix}{item}/", output_file)
            # 递归调用自身，增加缩进
            next_indent = indent + ('    ' if is_last else '│   ')
            list_project_structure(root_dir=item_path,
                                   indent=next_indent,
                                   output_file=output_file,
                                   ignore_dirs=ignore_dirs)
        else:
            _print_output(f"{prefix}{item}", output_file)


list_project_structure(root_dir=FILE_OPERATION_DIR,
                       ignore_dirs=["dist", "node_modules"])
