-- 코드를 입력하세요
-- 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 
-- 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력
-- 결과는 카테고리명을 기준으로 오름차순 정렬 
SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM BOOK AS B LEFT JOIN BOOK_SALES AS S 
ON B.BOOK_ID = S.BOOK_ID
WHERE DATE_FORMAT(S.SALES_DATE, "%Y-%m") = "2022-01"
GROUP BY category
ORDER BY CATEGORY;