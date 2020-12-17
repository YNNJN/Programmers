function solution(arr) {
  // 반복문 돌면서 숫자 없애기
  // filter() 메서드는 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환함
  return arr.filter((v,i) => v !== arr[i + 1])
}