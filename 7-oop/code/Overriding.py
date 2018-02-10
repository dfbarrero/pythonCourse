class A:
    def hello(self):
	    print("A says hello")

class B(A):
    def hello(self):
        print("B says hello")

b = B()
b.hello()
