import sys

def main():

    c = float(input("Kindly input the current temperature °C = "))
    f = c * 9 / 5 + 32

    print(f"The temperature is {f}°F")
    return 0

if __name__ == "__main__":
    sys.exit(main())




