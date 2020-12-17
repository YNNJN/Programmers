function solution(a, b) {
  // getDay() 메서드는 주어진 날짜의 현지 시간 기준 요일을 반환함
  // 0이 일요일을 나타냄
  return ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'][new Date(2016, a - 1, b).getDay()]
}