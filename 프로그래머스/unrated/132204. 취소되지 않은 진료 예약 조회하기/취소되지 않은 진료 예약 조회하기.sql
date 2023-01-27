-- 코드를 입력하세요
-- PATIENT, DOCTOR 그리고 APPOINTMENT 테이블
-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력
-- 결과는 진료예약일시를 기준으로 오름차순 정렬
SELECT AP.APNT_NO, PT.PT_NAME, PT.PT_NO, DT.MCDP_CD, DT.DR_NAME, AP.APNT_YMD
FROM APPOINTMENT AP
     INNER JOIN DOCTOR DT 
     ON AP.MDDR_ID = DT.DR_ID
     INNER JOIN PATIENT PT 
     ON AP.PT_NO = PT.PT_NO
WHERE DATE_FORMAT(AP.APNT_YMD, "%Y-%m-%d") = "2022-04-13"
      AND DT.MCDP_CD = "CS"
      AND AP.APNT_CNCL_YN = "N"
ORDER BY AP.APNT_YMD;