function solution(phone_number) {
  const n = phone_number.length
  const back_number = phone_number.slice(-4)
  return '*'.repeat(n - 4) + back_number
}