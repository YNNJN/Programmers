function solution(n,m) {
  console.log(Array(m).fill().map(() => '*'.repeat(n)).join('\n'))
}

n = 3
m = 5
solution(n,m)