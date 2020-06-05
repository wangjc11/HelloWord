from sys import exit

def gold_room():
    print("推开这扇门，你会发现这个房间里面堆满了零食，然后有着声音传过来，说是满分为100分，你有多爱汪进超，就能拿走多少零食，请告诉魔镜你的答案！")
    
    while True:
        choice = input(">")
        if "0" in choice or "1" in choice or "2" in choice or "3" in choice or "4" in choice or "5" in choice or "6" in choice or "7" in choice or "8" in choice or "9" in choice:
            how_much = int(choice)
        else:
            dead("你必须说出具体的值！！到底是多少？")
        
        if how_much < 99:
            print("太少了，你还不够爱他，不能拿走零食！！！魔镜很生气，你一丁点零食都拿不到！！！！")
            print("看在宝贝很可爱的份上，再给宝贝一次机会，请大声说出来你有多爱他！！！")
        else:
            dead("hhhhh，原来你这么爱他呀！！魔镜很开心，这一屋子的零食都是你的啦，恭喜你通关啦~~~~")
        

def bear_room():
    print("在这个房间中，有着一只大狗熊，狗熊在睡觉，他的背后有着一扇门，你必须引走狗熊才能进如这扇门，你会怎么做呢？")
    bear_moved = False

    while True:
        choice = input(">请输入 用蜂蜜勾引/打晕狗熊  ")

        if choice == "用蜂蜜勾引":
            print("狗熊在美梦中醒过来，并且流着口水看着你！！")
            print("显然狗熊醒啦你就更没有机会啦，这个答案错了哟~~重新来宝贝")
        elif choice == "打晕狗熊" and not bear_moved:
            print("现在你可以绕过狗熊到达门前~")
            print("现在你面临着这扇门，你不知道门后面是什么，你是想 打开门一探究竟/退出并随手敲了狗熊一棍子？")
            
            x = input("请输入 打开门一探究竟/退出并随手敲了狗熊一棍子")
            if x == "退出并随手敲了狗熊一棍子":
                dead("狗熊不知道怎么就醒了，你赶紧逃走没想到还是慢了一步，狗熊一口咬住你的脚，然后慢慢的吃掉了你~~")
            elif x == "打开门一探究竟":
                gold_room()     # while循环可以用break跳出，也可以调用别的函数跳出
        else:
            print("你输入的不符合规定，请重新输入！")

def cthulhu_room():
    print("这个房间存在着一个魔镜，魔镜问你，在零食和汪进超之间只能选一个你会选谁？")

    choice = input(">请输入 零食/汪进超/都不选  ")

    if "都不选" in choice:
        print("不能都不选，破坏游戏规则，重新开始游戏！！！")
        start()
    elif "汪进超" in choice:
        dead("宝贝我就知道你是爱我的！！！！")
    else:
        print("我知道你选错了再给宝贝一个机会~")
        cthulhu_room()   # 重复调用一个函数也可以形成循环

def dead(why):
    print(why, "我爱你哟~~~")
    exit(0)

def start():
    print("现在你身处在一个无人的小房间里，在你的左边和你的右边分别有一扇门，但是你不知道它们通往何处，现在你需要做出决定，是去是留?")

    choice = input(">请输入 左边/右边/待在原地  ")

    if choice == "左边":
        bear_room()
    elif choice == "右边":
        cthulhu_room()
    else:
        dead("你将会在这小房间里，孤独的饿死~~~")

start()  