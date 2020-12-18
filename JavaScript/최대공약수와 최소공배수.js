function solution(n, m) {
  function u(n,m) {
      return m % n ? u(m % n, n) : n
  }
  const gcd = u(n, m)
  return [gcd, n * m / gcd]
}