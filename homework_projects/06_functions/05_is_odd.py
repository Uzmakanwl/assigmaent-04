def main():
    for i in range(10, 20):  
        if is_odd(i):  
            print(i, "odd")  
        else:  
            print(i, "even")

def is_odd(value: int):    
    remainder = value % 2  
    return remainder == 1 

if __name__ == '__main__':
    main()  
