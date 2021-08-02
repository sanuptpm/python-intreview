class RangeExample:
    def range_method(self):
        for i in range(10):
            print("range_method", i)

    def range_start_stop(self):
        for i in range(2, 10):
            print("range_start_stop", i)


obj1 = RangeExample()
obj1.range_method()
obj1.range_start_stop()
