function solution(n) {
  // Array fill map => 순차 배열 만듦
  return Array(n).fill().map((v, i) => i + 1).reduce((a, c) => n % c ? a : a + c, 0) // acc, cur
}