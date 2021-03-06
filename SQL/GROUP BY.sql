-- 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE

-- 동명 동물 수 찾기
SELECT NAME, COUNT
FROM (SELECT NAME, COUNT(NAME) COUNT
    FROM ANIMAL_INS
    WHERE NAME IS NOT NULL
    GROUP BY NAME
    ORDER BY NAME)
WHERE COUNT >= 2

-- 입양 시각 구하기
SELECT HOUR, COUNT(HOUR)
FROM (SELECT TO_CHAR(DATETIME,'HH24') HOUR FROM ANIMAL_OUTS)
WHERE HOUR >= 9 AND HOUR <= 19
GROUP BY HOUR
ORDER BY HOUR