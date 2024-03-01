import sys

if len(sys.argv) != 4:
        print("Usage: python app.py 3 - 1")
        sys.exit(1)

input1 = sys.argv[1]
input2 = sys.argv[2]
input3 = sys.argv[3]

if input2 == '-':
        input4 = int(input1) - int(input3)
elif input2 == '+':
        input4 = int(input1) + int(input3)
elif input2 == '*':
        input4 = int(input1) * int(input3)
elif input2 == '/':
        input4 = int(input1) / int(input3)

print(input4)
