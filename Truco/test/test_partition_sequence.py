import sys
import os
sys.path.append('../')
from Back import *
from utils import *


if __name__ == "__main__":
    s1 = "6Diamonds"
    s2 = "AceDiamonds"

    result1 = partition_sequence(s1)
    result2 = partition_sequence(s2)

    print(f"Partitioned sequence for '{s1}': {result1}")
    print(f"Partitioned sequence for '{s2}': {result2}")
