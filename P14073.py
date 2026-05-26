def main():
    n, m = map(int, input().split())

    left_weights = list(map(int, input().split()))
    right_weights = list(map(int, input().split()))

    lwt = sum(left_weights)
    rwt = sum(right_weights)

    if lwt == rwt:
        print("Equal")
    else:
        print("Not Equal")


if __name__ == "__main__":
    main()