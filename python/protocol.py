from typing import Protocol
from abc import abstractmethod

class A(Protocol):
    def f(self) -> int:
        return 'hello'

class B(A):
    pass

if __name__ == "__main__":
    b: B
    b = B()
    result = b.f()
    print(result)