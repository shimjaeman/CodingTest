-- 코드를 입력하세요
select ICE.FLAVOR from ICECREAM_INFO as ICE join FIRST_HALF as FIR on ICE.FLAVOR = FIR.FLAVOR
where FIR.TOTAL_ORDER > 3000 and ICE.INGREDIENT_TYPE = "fruit_based";