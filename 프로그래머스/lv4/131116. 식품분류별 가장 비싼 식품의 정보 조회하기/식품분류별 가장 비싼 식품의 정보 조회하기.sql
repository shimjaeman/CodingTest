-- 코드를 입력하세요
SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME 
        from FOOD_PRODUCT 
        WHERE CATEGORY in ('과자', '국', '김치', '식용유')     
        AND PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
        group by CATEGORY 
        order by MAX_PRICE DESC;