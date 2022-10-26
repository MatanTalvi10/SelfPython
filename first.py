lst0 = [a for a in "hello"]
print(lst0)
print("hi")
x = 5
print("i like {}".format("apples"))
print(f"hi, your number is {x}")
mydict = {"a": 2, "b": 3, "c": 4}
for key,val in mydict.items():
    print(val)
a = (4,2,5)
b = set(mydict)
print(b)
my_new_file = open("my_new_file.txt", "w")
my_new_file.write("ONE ON FIRST\nTWO ON SECOND\nTHREE ON THIRD")
my_new_file = open("my_new_file.txt", "r")
print(my_new_file.read())
with open("my_new_file.txt", "a") as f:
    f.write("FOUR AS FOURTH")
print(my_new_file.read())
lst1 = [1,2,3]
lst2 = ['a','b','c']
lst_match = list(zip(lst1,lst2))
print(47/182)
def myfunc(*nums):
    print(nums)
myfunc(4,6,8,9)
a = "hello idan mamy"
a.split()
print(a)
