function solution(A,B) {
  const b = B.sort((p, c) => c - p) // 내림차순 정렬
  const a = A.sort((p, c) => p - c) // 오름차순 정렬
  return a.map((v,i) => v * b[i]).reduce((a, c) => a + c, 0)
}