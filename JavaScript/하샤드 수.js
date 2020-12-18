function solution(x) {
  // * 1은 문자열을 숫자로 만들기 위함
  return !(x % String(x).split('').reduce((a,c) => a + c * 1, 0))
}