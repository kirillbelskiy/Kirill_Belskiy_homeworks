heights = [200, 200, 180, 175, 170, 165]
petya_height = int(input("Введите рост Пети: "))

for i in range(len(heights)):
    if petya_height > heights[i]:
        print("Петя должен встать под номером:", i + 1)
        break
else:
    print("Петя должен встать в конец строя под номером:", len(heights) + 1)
