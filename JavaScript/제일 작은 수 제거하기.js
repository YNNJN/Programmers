function solution(arr) {
  const min = Math.min(...arr)
  // console.log(min)
  const r = arr.filter(v => v!== min)
  return r.length ? r : [-1]
}