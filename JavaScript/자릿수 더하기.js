function solution(n) {
  return String(n).split('').reduce((a, c) => a + +c, 0); // +c로 문자열을 숫자로 바꿈
}