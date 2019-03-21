#!/usr/bin/env python3
from os import path, getcwd
def check_gitfile_exist():
    path = getcwd()
    try:
        path.isdir(path + '/.git')
    except:
        raise fatal('not a git repository (or any of the parent directories)')


def git_init():
