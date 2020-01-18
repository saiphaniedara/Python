if __name__=='__main__':
    string=input()
    divider = 7
    count = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            sub_string = string[i:j]
            if int(sub_string) % divider == 0:
                count += 1
    print(count) 
