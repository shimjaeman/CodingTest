-- 코드를 입력하세요
-- 천재지변으로 인해 일부 데이터가 유실
-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회
SELECT AO.ANIMAL_ID, AO.NAME from ANIMAL_OUTS AS AO LEFT JOIN ANIMAL_INS AS AI 
                             ON AO.ANIMAL_ID = AI.ANIMAL_ID
                             WHERE AI.SEX_UPON_INTAKE IS NULL;