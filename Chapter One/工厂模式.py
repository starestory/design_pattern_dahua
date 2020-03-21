# -*- coding: utf-8 -*-
# @Time : 2020/3/21 16:31
# @Author : Maybe

# 运算类
class Operation(object):

    def __init__(self,):
        self.__numberA = 0
        self.__numberB = 0

    def get_numberA(self):
        return self.__numberA

    def get_numberB(self):
        return self.__numberB

    def set_numberA(self,numberA):
        if isinstance(numberA,str):
            self.__numberA = float(numberA)

    def set_numberB(self,numberB):
        if isinstance(numberB,str):
            self.__numberB = float(numberB)

# 加法
class OperationAdd(Operation):
    def get_result(self):
        return self.get_numberA()+self.get_numberB()

# 减法
class OperationSub(Operation):
    def get_result(self):
        return self.get_numberA()-self.get_numberB()

# 乘法
class OperationMul(Operation):
    def get_result(self):
        return self.get_numberA()*self.get_numberB()

# 减法
class OperationDiv(Operation):
    def get_result(self):
        if self.get_numberB():
            return self.get_numberA()/self.get_numberB()
        return '除数不能为0'

# 运算工厂
class OperationFactory(object):
    operation = dict()
    operation['+'] = OperationAdd()
    operation['-'] = OperationSub()
    operation['*'] = OperationMul()
    operation['/'] = OperationDiv()

    def createoperation(self,ch):
        if ch in self.operation:
            oper = self.operation[ch]
            return oper
        return 'undefine operation'

# 客户端代码
if __name__ == '__main__':
    op = input("operator: ")
    numA = input("numA: ")
    numB = input("numB: ")
    oper = OperationFactory().createoperation(op)
    oper.set_numberA(numA)
    oper.set_numberB(numB)
    result = oper.get_result()
    print(result)


