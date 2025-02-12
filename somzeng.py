# fruits = ["Apple","Mango","Banana"]

# for fruit in fruits:
#     print(fruit)

# for item in range(10):
#         print(item)

# for count in range(10):
#       if count > 5:
#             break
#       elif count % 2 ==0:
#             continue
#       print(count)


#       count = 0
#       while count <= 5:
#             print(count)
#             count += 1


# int name(int a){
#     printf("%d",a);
#     return a;
# }
# this is wriiten a
def function_name(a:int, b: int = None) -> int:
    print(f"a: {a}")
    print(f"b: {b}")
    return a
function_name(b=10, a=20)
