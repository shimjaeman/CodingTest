-- 코드를 입력하세요
-- 할인율이 적용되는 대여 기간 종류로는 
   -- '7일 이상' (대여 기간이 7일 이상 30일 미만인 경우)
   -- '30일 이상' (대여 기간이 30일 이상 90일 미만인 경우)
   -- '90일 이상' (대여 기간이 90일 이상인 경우) 
   -- 대여 기간이 7일 미만인 경우 할인정책이 없습니다.
-- 자동차 종류가 '트럭'인 자동차의 대여 기록 별로 대여 금액(컬럼명: FEE)을 구하여 
-- 대여 기록 ID와 대여 금액 리스트를 출력
-- 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 기록 ID를 기준으로 내림차순 정렬해주세요.
SELECT HISTORY_ID,
ROUND(CASE WHEN datediff(END_DATE, START_DATE)+1 < 7 THEN CAR.DAILY_FEE * (datediff(END_DATE, START_DATE) +1)
     WHEN datediff(END_DATE, START_DATE)+1 < 30 THEN CAR.DAILY_FEE * (datediff(END_DATE, START_DATE) +1) * (SELECT 1 - DISCOUNT_RATE/100 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '7일 이상')
     WHEN datediff(END_DATE, START_DATE)+1 < 90 THEN CAR.DAILY_FEE * (datediff(END_DATE, START_DATE) +1) * (SELECT 1 - DISCOUNT_RATE/100 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '30일 이상')
     ELSE CAR.DAILY_FEE * (datediff(END_DATE, START_DATE) +1) *(SELECT 1 - DISCOUNT_RATE/100 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '90일 이상') END) AS FEE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY HIS LEFT JOIN CAR_RENTAL_COMPANY_CAR CAR
ON HIS.CAR_ID = CAR.CAR_ID
WHERE CAR.CAR_TYPE = "트럭"
ORDER BY FEE DESC, HISTORY_ID DESC;