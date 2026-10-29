# class student:

#     def__init__(self,r,n)
#     self__roll=r
#     self__name=n

#     def set_roll(self,nr,otp):
#         if otp==1234:
#             self.__roll =nr 

#     def getroll(self,pin):
#         if pin==12345:
#             return self__roll
#         else:
#             return "wrong pin "

# s1=student(1,"Chaitanya")
# s1.set_roll(123456789)
# res=s1.getroll(3)
# print(res)


class Student:
    def __init__(self, r, n):
        self.__roll = r
        self.__name = n

    def set_roll(self, nr, otp):
        if otp == 1234:
            self.__roll = nr
       

    def getroll(self, pin):
        if pin == 12345:
            return self.__roll
        else:
            return "Wrong PIN"

    def set_name(self,nn,otp):
        if otp==1234:
            self.__name=nn


    def getname(self,pin):
        if pin==12345:
            return self.__name
        else:
            return"wrong pin"

s1 = Student(1, "Chaitanya")
s1.set_roll(12, 1234)
res = s1.getroll(12345)
print(res)

s1 = Student(1, "Chaitanya")
s1.set_name("RAM", 1234)
res2 = s1.getname(12345)
print(res2)
