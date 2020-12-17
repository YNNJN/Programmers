function solution(s) {
  var temp = parseInt(s);
  // 길이에 대한 OR 연산자를 includes를 이용하여 짧게 줄임
  if (s == temp && [4,6].includes(s.length)) {
    return true;
  }
  return false;
}