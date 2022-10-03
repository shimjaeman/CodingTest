def solution(price):
    sale_price = 0
    if price >= 500000:
        sale_price = price * 0.80
    elif price >= 300000:
        sale_price = price * 0.90
    elif price >= 100000:
        sale_price = price * 0.95
    else :
        sale_price = price
    return int(sale_price)