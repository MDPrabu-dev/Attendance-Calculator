print("ATTENDANCE CALCULATOR")

try:
    total_classes = int(input("Enter total classes: "))
    attended_classes = int(input("Enter classes attended: "))

    if total_classes <= 0:
        print("Total classes must be greater than 0.")

    elif attended_classes < 0:
        print("Classes attended cannot be negative.")

    elif attended_classes > total_classes:
        print("Classes attended cannot be greater than total classes.")

    else:
        attendance = (attended_classes / total_classes) * 100
        print("Your attendance is:", attendance, "%")

except ValueError:
    print("Please enter a valid number.")