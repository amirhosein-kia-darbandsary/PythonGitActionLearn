def main():
    answre = 2 + 2
    with open('./dist/log.txt'  , 'w') as f:
        f.write("this is a log test")
        f.close()
    return answre



if __name__ == '__main__':
    main()