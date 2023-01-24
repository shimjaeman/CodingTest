-- 코드를 입력하세요
-- 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회
-- 결과는 총매출을 기준으로 내림차순 정렬
-- 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬
SELECT A.PRODUCT_ID, A.PRODUCT_NAME, (A.PRICE * SUM(B.AMOUNT)) AS TOTAL_SALES
       FROM FOOD_PRODUCT A LEFT JOIN FOOD_ORDER B 
       on A.PRODUCT_ID = B.PRODUCT_ID
       WHERE PRODUCE_DATE LIKE "%2022-05%"
       GROUP BY A.PRODUCT_ID
       ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID ASC;