
class Time_complexity:

    def __init__(self,lst):
        self.lst=lst


    def constant_time(self):         #constant_time=O(1)
        index_0=self.lst[0]
        print(index_0)

    def linear_search(self, value):  #linear_time=O(n)
        for index in range(len(self.lst)):
            if value == self.lst[index]:
                print('{} found in index {}'.format(value,index))
                return
        print('Value not found in the list')

    def bubble_sort(self):           #quadratic_time=O(n^2)
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.lst) - 1):
                if self.lst[i] > self.lst[i + 1]:
                    self.lst[i], self.lst[i + 1] = self.lst[i + 1], self.lst[i]
                    swapped = True
        return self.lst

    def binary_search(self,value):  #logarithmic_time=O(log n)
        n = len(self.lst)
        left = 0
        right = n - 1
        self.lst=t1.bubble_sort()

        while left <= right:
            middle = (left + right) // 2
            if value < self.lst[middle]:
                right = middle - 1
            elif value > self.lst[middle]:
                left = middle + 1
            else:
                print('{} present in index {}'.format(value,middle))
                return
        print('Value is not in the list')

    def quasilinear_time(self):     #quasilinear_time=O(n log n)
        for value in self.lst:
            t1.binary_search(value)


    def factorial_time(self,n):     #factorial_time=O(n!)
        pass

    def my_function(self):          #it has multiple time complexities: O(1) + O(n) + O(n^2)
        first_element =self.lst[0]  #O(1)
        print(first_element)

        for value in self.lst:      #O(n)
            print(value)

        for x in self.lst:          #O(n^2)
            for y in self.lst:
                print(x, y)         #we take worst case as the time complexity so here: O(n^2)

lst=[3,5,8,4,9,1]
t1=Time_complexity(lst)
print(t1.bubble_sort())
t1.binary_search(9)
t1.quasilinear_time()
t1.linear_search(1)


