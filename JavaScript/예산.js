// M1
function solution(d, budget) { // 신청 금액, 예산    
  d.sort((a, b) => b - a) // 내림차순 정렬
  let cnt = 0
  while (budget >= d[d.length - 1]) {
    budget -= d.pop()
    cnt ++
  }
  return cnt;
}

// M2
function solution(d, budget) {
  let cnt = 0
  let money = 0
  d.sort((a, b) => a - b).forEach(function (val) {
    money += val
    if (money <= budget) {
      cnt++
    }
  })
  return cnt
}