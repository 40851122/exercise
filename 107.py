total = 0
total_list = []
while total<5:
    x = eval(input(f'輸入第{total+1}次：'))
    total_list.append(x)
    total += 1
list_sum= sum(total_list)
list_Average = list_sum / len(total_list)
print(total_list)
print(f'Sum = {list_sum}')
print(f'Average = {list_Average}')
