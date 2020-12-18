function solution(s) {
  return s.split(' ').map(v => {
      return v.split('').map((a,i) => i ? a.toLowerCase() : a.toUpperCase()).join('')
  }).join(' ')
}