def cm_to_inches(cm):
    inches = cm / 2.54
    return inches

if __name__ == "__main__":
    cm = float(input("Enter length in centimeters: "))
    inches = cm_to_inches(cm)
    print(f"{cm} cm = {inches:.2f} inches")