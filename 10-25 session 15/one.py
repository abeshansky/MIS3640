def func():
    print("func() in one.py")

#print("top-level in one.py")

def main():
    print("Main function in one.py")

if __name__ == "__main__":
    main()
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
