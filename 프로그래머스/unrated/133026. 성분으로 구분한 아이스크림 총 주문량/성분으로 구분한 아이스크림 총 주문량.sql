-- 코드를 입력하세요
select INGREDIENT_TYPE, sum(ToTal_order) as TOTAL_ORDER from (SELECT FH.FLAVOR, II.INGREDIENT_TYPE, 
                                                    FH.ToTal_order From icecream_info II left join 
                                                    first_half FH on II.FLAVOR = FH.FLAVOR) aa group by INGREDIENT_TYPE;