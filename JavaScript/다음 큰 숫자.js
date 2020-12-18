function solution(n) {
  // toString(2)로 이진법으로 바꿈
  // match(/1/g).length는 1의 개수를 셈
  const bin = n.toString(2).match(/1/g).length
  while (n++) {
      // 함수 안에서는 return으로 반복문을 멈출 수 있음
      if (n.toString(2).match(/1/g).length === bin) return n
  }
}