# file : mypack/games/__init__.py


# 此列表将在from mypack.games import *
# 时只导入 contral 和 tanks模块

__all__ = ['contra', 'tanks']


print("mypack下的games子包被导入")