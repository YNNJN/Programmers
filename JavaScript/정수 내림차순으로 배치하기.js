function solution(n) {
  let ans = String(n).split('').sort((p, c) => c - p).join('')
  return parseInt(ans)
}