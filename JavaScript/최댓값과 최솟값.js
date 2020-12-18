function solution(s) {
  // 숫자 배열로 변환
  const arr = s.split(' ').map(v => v * 1)
  // 배열에서 최대 최소값 찾아서 조인
  return [Math.min(...arr), Math.max(...arr)].join(' ')
}