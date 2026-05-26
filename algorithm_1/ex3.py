def main():
    while True:
        try:
            line = input()
            numbers = list(map(int, line.split()))
            total = sum(numbers)
            print(total)
        except EOFError:
            break

if __name__ == "__main__":
    main()