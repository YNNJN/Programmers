function solution(s){
  // split() 메서드는 String 객체를 지정한 구분자를 이용하여 여러 개의 문자열로 나눔
  // includes() 메서드는 배열이 특정 요소를 포함하고 있는지 판별함
  const p = s.split('').filter(v => ['p', 'P'].includes(v));
  const y = s.split('').filter(v => ['y', 'Y'].includes(v));
  return p.length === y.length;
}