def valid_arg():
    while True:
        
        numbers = input().split()
        numbers1 = numbers
        for num in numbers:
            if num.startswith("-"):
                num = num[1:]

            if num.count(".") == 1:
               num = num.replace(".","")

            if not num.isdigit():
                print("Invalid Input! Enter a valid input.")
                break
        else:
            numbers = numbers1
            for num in range(len(numbers)):
                numbers[num] = float(numbers[num])
            return numbers
    


def AVG(numbers):
    sum_num = sum(numbers)
    len_num = len(numbers)
    return sum_num / len_num


def main():
    print(f"{AVG(valid_arg()):.2f}")

main()