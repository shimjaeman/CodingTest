-- 코드를 입력하세요
-- 7월 아이스크림 총 주문량 + 상반기의 아이스크림 총 주문량을 더한 값이 
-- 큰 순서대로 상위 3개의 맛을 조회
SELECT FH.FLAVOR
FROM FIRST_HALF FH LEFT JOIN JULY JY
     ON FH.FLAVOR = JY.FLAVOR
GROUP BY JY.FLAVOR
ORDER BY (FH.TOTAL_ORDER + SUM(JY.TOTAL_ORDER)) DESC
LIMIT 3;