function solution(arr1, arr2) {
  // for문 중첩 => map 두 번
  return arr1.map((row) => // 첫번째 배열 행의 갯수
      arr2[0].map((_, j) => // 두번째 배열 열의 갯수
          row.reduce((acc, num, i) => acc + num * arr2[i][j], 0)))
}