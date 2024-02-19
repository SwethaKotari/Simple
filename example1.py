def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

def main():
    # Hardcoded values for the dimensions of the rectangle
    length = 5.0
    width = 3.0

    # Calculate the area of the rectangle
    area = calculate_rectangle_area(length, width)

    # Print the result
    print(f"The area of the rectangle with length {length} and width {width} is: {area}")

if __name__ == "__main__":
    main()


