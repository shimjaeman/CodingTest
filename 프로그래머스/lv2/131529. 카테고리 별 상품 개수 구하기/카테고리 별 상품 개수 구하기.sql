-- 코드를 입력하세요
SELECT CATEGORY, COUNT(*) AS PRODUCTS 
   FROM (SELECT left(PRODUCT_CODE, 2) as CATEGORY from PRODUCT) A    GROUP BY CATEGORY
   ORDER BY CATEGORY;
   