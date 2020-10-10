-- 최댓값 구하기
SELECT DATETIME
FROM (SELECT * FROM ANIMAL_INS ORDER BY DATETIME DESC)
WHERE rownum = 1;

-- 최솟값 구하기
SELECT DATETIME
FROM (SELECT * FROM ANIMAL_INS ORDER BY DATETIME)
WHERE rownum = 1;

-- 동물 수 구하기
SELECT COUNT(ANIMAL_ID) FROM ANIMAL_INS

-- 중복 제거하기
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL