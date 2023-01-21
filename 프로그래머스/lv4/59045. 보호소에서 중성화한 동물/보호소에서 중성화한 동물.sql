-- 코드를 입력하세요
# 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 
# 보호소에 들어올 당시에는 중성화 되지 않았지만, 
# 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
SELECT AI.ANIMAL_ID, AI.ANIMAL_TYPE, AI.NAME 
        FROM ANIMAL_INS AS AI LEFT JOIN ANIMAL_OUTS AS AO
        ON AI.ANIMAL_ID = AO.ANIMAL_ID 
        WHERE AI.SEX_UPON_INTAKE LIKE "%INTACT%" AND 
              (AO.SEX_UPON_OUTCOME LIKE "%Neutered%" OR 
              AO.SEX_UPON_OUTCOME LIKE "%Spayed%");