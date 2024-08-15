from count_pairs import test_python_implementation as test_python
from count_pairs import test_c_implementation as test_c
import sys
import csv
import random



def make_file(i):

    heads_or_tails = random.randint(0,1)
    if heads_or_tails == 0:
        target = -(10**3000 + random.randint(1, 10**3000))
    else:
        target = 10**3000 + random.randint(1, 10**3000)
    base = 10**4200
    size = i * 100

    with open(f'inputs/input_{i}.txt', mode='w') as file:
        file.write(f"{target}\n")
        file.write(f"{size}\n")
        for _ in range(size):
            file.write(f"{base + random.randint(-i*2,i*2)*target +  random.randint(-i*5,i*5)}\n")
    
    return f'inputs/input_{i}.txt' , target
            








if __name__ == "__main__":
    if len(sys.argv) !=3:
        print(f'Run properlly: python3 {sys.argv[0]} <start> <end>')
        sys.exit(1)
    # Open the file argv[1]
    # filename = sys.argv[1]
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    # Call count_pairs_file and print the result


    with open('results.csv', mode='w') as results_file:
        for i in range(start, end + 1):

            
            filename , target = make_file(i)
            print(f"Running test {i}")
            py, py_time = test_python(filename)
            c, c_time = test_c(filename)
            assert py == c
            results_file.write(f"{i*100}, {target} ,{py},{py_time},{c},{c_time}\n")
            print(f"Test {i} completed")
    print("All tests passed")




