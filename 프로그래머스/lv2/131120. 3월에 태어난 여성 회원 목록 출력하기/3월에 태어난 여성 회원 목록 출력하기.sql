-- 코드를 입력하세요
SELECT Member_id, member_name, gender, date_format(DATE_OF_BIRTH, "%Y-%m-%d")
        from member_profile 
        where DATE_OF_BIRTH LIKE "%03%" 
        and TLNO is not null
        and Gender = "W";