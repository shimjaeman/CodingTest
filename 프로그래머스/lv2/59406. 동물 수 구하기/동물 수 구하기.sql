-- 코드를 입력하세요
select count(*) from (SELECT * from ANIMAL_INS group by ANIMAL_ID)a;