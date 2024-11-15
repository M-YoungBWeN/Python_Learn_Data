from . import *


def package_api(mode, file_path, w_str):
    """
    文件读写函数
    :param mode: 选择读取还是写入(mode='r' mode='w',str)
    :param file_path: txt文件路径(utf-8,file)
    :param w_str: 需要写入的文本(str)
    :return:
    """
    try:
        if mode == 'r':
            load_data(file_path)
        elif mode == 'w':
            write_data(file_path, w_str)
        else:
            print('请输入正确的mode')
    except:
        print('发生错误')
