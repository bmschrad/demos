# Sample easy program
import pdb

def run():
    i = 0

    while i < 10:
        pdb.set_trace()
        print(i)
        i = i+1

if __name__ == '__main__':
    run()
