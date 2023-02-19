def solution(want, number, discount):
    zip_want = [i for i in zip(number, want)]
    ten_sale = [discount[i:10+i] for i in range(len(discount)-9)]
    all_pass = 0
    result = 0
    while ten_sale:
        for nu, wa in zip_want:
            if ten_sale[0].count(wa) == nu:
                all_pass +=1
            else :
                del ten_sale[0]
                all_pass = 0
                break
        if all_pass == len(number):
            result += 1
            del ten_sale[0]
            all_pass = 0
    return result