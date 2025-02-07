def count_substring(main_string, sub_string):
    count = 0
    n = len(main_string) - len(sub_string)+1
    for i in range(n):
        if(sub_string == main_string[i:i+len(sub_string)]):
            count += 1
    return count

if __name__ == '__main__':
    main_string = input().strip()
    sub_string = input().strip()
    count = count_substring(main_string, sub_string)
    print(count)
    
