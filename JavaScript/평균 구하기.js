function solution(arr) {
  // 평균, 곱, 합과 같이 쌓이는 것 => reduce
  return arr.reduce((a, c) => a + c) / arr.length
}