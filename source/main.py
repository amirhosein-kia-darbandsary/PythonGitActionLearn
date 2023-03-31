import os
def main():
    answre = 2 + 2
    with open('./logs/log.txt'  , 'w') as f:
        f.write("mew mew niga")
        f.close()
    return answre

def read_logger_name():
    name = os.environ['USER']
    return name 


if __name__ == '__main__':
    main()