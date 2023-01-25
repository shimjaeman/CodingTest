-- 코드를 입력하세요
-- 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회
-- 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.
SELECT CART_ID FROM CART_PRODUCTS
WHERE NAME = "MILK" AND CART_ID IN 
(SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = "Yogurt");