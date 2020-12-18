function solution(num, cnt = 0) {
  return cnt === 500
    ? -1
    : num === 1
      ? cnt
      : solution(num % 2 ? num * 3 + 1 : num / 2, cnt + 1)
}