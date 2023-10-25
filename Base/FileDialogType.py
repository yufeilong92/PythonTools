#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/16 18:17
# @Author  : backpacker
# @File    : FileDialogType.py
# @Description : $文件选择器
from enum import Enum


class FileDialogType(Enum):
    DIRECTORY=1#目录
    DOCUMENT=2#文件
    pass
