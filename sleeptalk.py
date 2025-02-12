class Person:
    def __init__(afu, name, age):
        afu.name = name
        afu.age = age

    def sleep(afu):
            print(f'{afu.name} is sleeping')

    def talk(afu):
            print(f'{afu.name} is talking')

eyon = Person("Eyon Hun", 21)
print(eyon.age)
eyon.sleep()
eyon.talk()

xuehua = Person("xuehua Piao", 26)
xuehua.talk()
xuehua.sleep()
