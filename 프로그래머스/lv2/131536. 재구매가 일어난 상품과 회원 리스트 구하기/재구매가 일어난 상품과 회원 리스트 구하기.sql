-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID from onLine_sale 
      group by user_id, product_id
      HAVING COUNT(online_sale_id) > 1
      order by USER_ID, product_id desc;