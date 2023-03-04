import re
import psycopg2


# The following lines of code up to line 65 contains the answer to task 2, 3, 5

with open("python_class_question.html", 'r', encoding="utf-8") as html_file:
    html_content = html_file.read()

tag = 'td'
reg_str = "<" + tag + ">(.*?)</" + tag + ">"

res = re.findall(reg_str, html_content)

colors_list = []
distinct_colors = []
days, gre, yel, bro, blu, pin, ora, cre, red, whi, ars, ble, bla = [0 for i in range(13)]

for item in res:
    if item.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        days += 1
        continue
    colors = item.split(',')
    for color in colors:
        color = color.replace(" ", "")
        colors_list.append(color)
        if color not in distinct_colors:
            distinct_colors.append(color)
        if color == 'GREEN':
            gre += 1
        elif color == 'YELLOW':
            yel += 1
        elif color == 'BROWN':
            bro += 1
        elif color == 'BLUE':
            blu += 1
        elif color == 'PINK':
            pin += 1
        elif color == 'ORANGE':
            ora += 1
        elif color == 'CREAM':
           cre += 1
        elif color == 'RED':
            red += 1
        elif color == 'WHITE':
            whi += 1
        elif color == 'ARSH':
            ars += 1
        elif color == 'BLEW':
            ble += 1
        else:
            bla += 1


num_list = [gre, yel, bro, blu, pin, ora, cre, red, whi, ars, ble, bla]
max_num = num_list[0]
for num in num_list:
    if num > max_num:
        max_num = num


print(f"2. The color mostly worn throughout the week is blue. It was worn {max_num} times.")

middle_num = int(len(colors_list) / 2)
print(f"3. The median color is {colors_list[middle_num]}")
print(f"5. The probability of choosing a red color at random is {red}/{len(colors_list)}")



# TASK NO 6
conn = psycopg2.connect("interview.db", user="user_name", password="password", host="127.0.0.1", port="5432")
conn.execute("""CREATE TABLE interview ("ID" INT, "COLORS" TEXT NOT NULL, \
    "FREQUENCY" INT);""")

for i, color, freq in zip(range(1, 13), distinct_colors, num_list):
    c = "'" + color + "'"
    command = f"INSERT INTO interview (ID,COLORS,FREQUENCY) \
    VALUES ({i}, {c}, {freq});"
    conn.execute(command)

conn.commit()
print("Answers to question 6:")
rows = conn.execute("SELECT * from interview")
for row in rows:
    print(row[0], end=' ')
    print(row[1], end=' ')
    print(row[2])

conn.close()



# TASK NO. 7
def rec_search(n, list_num, i):
    if i >= len(list_num):
        print("Index out of range!")
        return False

    if n == list_num[i]:
        return True

    if rec_search(n, list_num, i + 1):
        return True

def main():
    print("Answer to question 7:")
    n = int(input("Enter your number: "))
    list_num = [1, 2, 3, 4, 5, 6, 7]


    if rec_search(n, list_num, 0):
        print("The number is in this list")
    else:
        print("Number not found")

main()

# TASK NO 8

def generate_digits():
    digits = []
    for _ in range(4):
        digits.append(str(random.randint(0,1)))
    return ''.join(digits)


def convert_to_base_10(bin):
    dec = 0
    for exp, dig in zip(range(len(bin)-1, -1, -1)bin[:]):
        dec += int(dig)*(2**exp)
        exp += 1
    return dec

binary = generate_digits()
decimal = convert_to_base_10(binary)
print("8. The generated 4 digits number of 0s and 1s :{} and it's value in base 10 is: {}".format(binary, decimal))



# TASK NO 9
def fibonacci_sum(n):
    a, b = 0, 1
    fib_sum = 0

    for i in range(n):
        fibonacci_sum += a
        a, b = b, a + b

    return fib_sum

fib_sum = fibonacci_sum(50)
print("9. The sum of first 50 Fibonacci numbers is", fib_sum)
