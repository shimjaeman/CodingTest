-- 코드를 입력하세요
-- 상품코드 별 매출액(판매가 * 판매량) 합계를 출력하는 SQL문을 작성
-- 결과는 매출액을 기준으로 내림차순 정렬
-- 매출액이 같다면 상품코드를 기준으로 오름차순 정렬
SELECT pd.PRODUCT_CODE, (sum(os.SALES_AMOUNT) * pd.price) as SALES
        from product as pd 
        left join offline_sale as os 
        on pd.PRODUCT_ID = os.PRODUCT_ID
        group by pd.PRODUCT_CODE
        order by SALES desc, pd.PRODUCT_CODE;