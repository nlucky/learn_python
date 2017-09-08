#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
print(os.name) # The name of the operating system dependent module imported. The following names have currently been registered
print(os.ctermid()) # Return the filename corresponding to the controlling terminal of the process.
# os.chdir("path") # 切换目录
print(os.getcwd()) # 获取当前目录
# print(os.environ)
print(os.PathLike)
print(os.path.fspath(os.getcwd))