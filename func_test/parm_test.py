def name(*namelist):
    print(namelist)

def name2(**namelist):
    print(namelist)

def name3(*namelist1,**namelist2):
    print(namelist1,namelist2)

name("ask","sdjlkfj")

name2(a="ask",b="sdjlkfj")

name3("ask","sdjlkfj",a="24244",b="35533535")