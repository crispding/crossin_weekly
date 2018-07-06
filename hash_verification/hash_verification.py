#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
计算并验证文件的哈希值
"""

__doc__ = '''
使用示例：
python hash_caculator.py python-3.5.3-amd64.exe
必须有两个参数。 
'''

import os
import sys
import hashlib

_FILE_SLIM = (100*1024*1024) # 100MB


def select_algorithm():

    """ 选择摘要算法 """

    supported_algorithm = {
        'md5':hashlib.md5(),
        'sha1':hashlib.sha1(),
        'sha224':hashlib.sha224(),
        'sha256':hashlib.sha256(),
        'sha384':hashlib.sha384(),
        'sha512':hashlib.sha512()
        }
    print('支持的哈希算法：{ md5 | sha1 | sha224 | sha256 | sha384 | sha512 }.')
    algorithm_input = input('请输入哈希算法：')
    algorithm_select = supported_algorithm[algorithm_input.lower()]
    return algorithm_input, algorithm_select


def file_hash_value(digest_algorithm, file_name):

    """ 返回文件的指定摘要算法哈希值 """

    calltimes = 0
    hash_method = digest_algorithm
    f_size = os.stat(file_name).st_size
    with open(file_name, "rb") as fp:
        if f_size > _FILE_SLIM:
            while f_size > _FILE_SLIM:
                hash_method.update(fp.read(_FILE_SLIM))
                f_size -= _FILE_SLIM
                calltimes += 1
                print('\rcalculating' + '.'*(calltimes-1), end='')
            if(f_size > 0) and (f_size <= _FILE_SLIM):
                hash_method.update(fp.read())
                print('\rcalculating' + '.'*calltimes, end='')
        else:
            hash_method.update(fp.read())
            print('calculating', end='')
        print('\nDone')
        return hash_method.hexdigest()


def cmp_hash_value(hashvalue_out):

    """ 比较计算的哈希值与校验值是否匹配 """

    hashvalue_vrf = input('请输入用于验证的哈希值（如不输入请直接回车）：')
    if hashvalue_vrf == '':
        return 'nothing'
    elif hashvalue_vrf.lower() == hashvalue_out:
        return True
    elif hashvalue_vrf.lower() != hashvalue_out and len(hashvalue_vrf) == len(hashvalue_out):
        return False
    else:
        print('输入的哈希值格式错误，请重试。')
        return 'wrong_value'


def hash_result_output(hash_value, algorithm, cmp_result):

    """ 在命令行及新文件中输出哈希值 """

    print('哈希值计算结果：\n' + hash_value)
    if cmp_result == 'nothing':
        print('未给予用于验证的哈希值。')
    elif cmp_result:
        print('该文件的 %s 值正确。' %algorithm)
    else:
        print('该文件的 %s 值错误。' %algorithm)


# def write_result(hash_value, algorithm, result):

#     """ 将哈希校验结果输出到文件 """

#     if os.name == 'nt':
#         file_output = os.path.abspath('.' + '\\hashoutput.txt')
#     else:
#         file_output = os.path.abspath('.' + '/hashoutput.txt')
#     with open(file_output, 'w') as fw:
#         fw.write('“' + sys.argv[1] + '”的 ' + algorithm + ' 哈希值')
#         fw.write('计算结果为：\n' + hash_value + '\n')
#         if result == 'nothing':
#             fw.write('未给予用于验证的哈希值。')
#         elif result:
#             fw.write('哈希值匹配，文件通过验证。')
#         else:
#             fw.write('哈希值未匹配，文件未通过验证。')
#     print('哈希验证结果已输出到文件“hashoutput.txt”中。')


def main():

    """ 主函数 """

    if len(sys.argv) == 2:
        try:
            FilePath = os.path.abspath(sys.argv[1])
            (AlgorithmInput, AlgorithmSelect) = select_algorithm()
            HashValue = file_hash_value(AlgorithmSelect, FilePath)
            Result = 'wrong_value'
            while Result == 'wrong_value':
                Result = cmp_hash_value(HashValue)
            hash_result_output(HashValue, AlgorithmInput, Result)
            # write_result(HashValue, AlgorithmInput, Result)
        except KeyError:
            print('哈希算法输入错误，请重试。')
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
