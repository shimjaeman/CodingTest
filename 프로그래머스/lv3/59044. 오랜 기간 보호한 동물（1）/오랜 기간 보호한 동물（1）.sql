-- 코드를 입력하세요
# 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회
SELECT AI.NAME, AI.DATETIME FROM ANIMAL_INS AI LEFT JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID 
        WHERE AO.DATETIME IS NULL
        ORDER BY AI.DATETIME
        LIMIT 3;