function solution(n) {
  return String(n).split('').reverse().map(v => +v) // map을 이용해 숫자로 바꿈
}