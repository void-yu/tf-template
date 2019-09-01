import argparse
import time
import os
import shutil



def current_time():
    return time.asctime(time.localtime(time.time()))


def judge_and_new(folder, need_clean=False):
    if not os.path.exists(folder):
        os.makedirs(folder)
    elif need_clean:
        shutil.rmtree(folder, ignore_errors=True)
        os.makedirs(folder)