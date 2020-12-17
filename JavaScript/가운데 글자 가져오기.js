function solution(s) {
  // substr() 메서드는 문자열에서 특정 위치에서 시작하여 특정 문자 수 만큼의 문자들을 반환함
  // Math.ceil() 함수는 주어진 숫자보다 크거나 같은 숫자 중 가장 작은 숫자를 integer 로 반환함
  return s.substr(Math.ceil(s.length / 2) - 1, s.length % 2 === 0 ? 2 : 1);
}