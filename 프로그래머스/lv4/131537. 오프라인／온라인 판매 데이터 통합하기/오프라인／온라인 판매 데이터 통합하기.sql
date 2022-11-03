-- 코드를 입력하세요
SELECT date_format(sales_date, '%Y-%m-%d') as sales_date, PRODUCT_ID, USER_ID, SALES_AMOUNT 
        from ONLINE_SALE
        where date_format(SAles_date, "%Y-%m") = "2022-03" 
union
SELECT date_format(sales_date, '%Y-%m-%d') as sales_date, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT 
        from OFFLINE_SALE
        where date_format(SALES_DATE, "%Y-%m") = "2022-03" 
        order by SAles_date, PRODUCT_ID, USER_ID;