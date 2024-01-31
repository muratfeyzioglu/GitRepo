from testCases import test_example


class Test:

    def run_tests(self):

        test_example.Test().test_example()


if __name__ == '__main__':
    my_test = Test()
    my_test.run_tests()


