function solution(arr, divisor) {
  const ans = arr.filter(el => el % divisor == 0)
  return ans.length ? ans.sort((a, b) => a - b) : [-1] // 오름차순 정렬
}