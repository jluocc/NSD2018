def play():
    print('正在玩　魂斗罗')
def game_over():
    print('魂斗罗游戏结束')
    #绝对导入
    from mypack.menu import show_menu
    show_menu()
    # 相对导入
    from ..menu import show_menu
    show_menu
    # 当前路径
    from .tanks import play
    play()
    print('游戏结束')
print('魂斗罗被加载')