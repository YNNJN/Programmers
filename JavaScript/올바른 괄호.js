function solution(s) {
  let cnt = 0
  for (let i = 0; i < s.length; i ++) {
    s[i] === '(' ? cnt ++ : cnt --
    if (cnt < 0) return false
  }
  if (cnt) return false
  return true
}