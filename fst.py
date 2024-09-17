def rightmost_set_bit(n):
    # Isolate the rightmost set bit
    rightmost_bit = n & -n
    
    # Find the position of the rightmost set bit (1-indexed)
    position = (rightmost_bit).bit_length()
    
    return rightmost_bit, position

def main():
    try:
        number = int(input("Enter an integer: "))
        
        if number <= 0:
            print("Please enter a positive integer.")
            return

        bit_value, position = rightmost_set_bit(number)
        print(f"Rightmost set bit value: {bit_value}")
        print(f"Position of the rightmost set bit (1-indexed): {position}")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
