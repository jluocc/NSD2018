# file: mypack/games/contra.py

def play():
    print("正在玩 魂斗罗")

def game_over():
    print("魂斗罗游戏结束!!!")
    # 想调用mypack/menu.py里的show_menu
    # 绝对导入
    # from mypack.menu import show_menu
    # show_menu()
    # 相对导入: 相对于当前mypack/games/
    from ..menu import show_menu
    show_menu()
    # 调用mypack/games/tanks.py里的play()
    # 当前位置: mypack/games/
    # from .tanks import play
    # from ..games.tanks import play
    from ...mypack.games.tanks import play

    play()



print("魂斗罗模块被加载")
