# recursion_forever.py

def say_story():
    print("从前有座山,山上有座庙,庙里有个老和尚讲故事:")
    say_story()
    print("讲故事结束")

say_story()
print("程序结束")
