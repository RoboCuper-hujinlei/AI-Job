"""
python multiprocessing 跨平台多进程模块
"""

from multiprocessing import Process
import os

def run_proc(name):
    print(f'Run child process {name}: ({os.getpid()})...')

# run_proc('th1')
if __name__ == '__main__':
    print(f'Parent process: {os.getpid()}')
