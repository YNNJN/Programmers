function solution(strings, n) {
  // localeCompare() 메서드는 기준 문자열과 비교했을 때 비교 대상 문자열이 정렬상 전에 오는지, 후에 오는지 혹은 같은 순서에 배치되는지를 알려주는 숫자를 리턴함
  return strings.sort((p, c) => p[n] === c[n] ? p.localeCompare(c) : p[n].localeCompare(c[n]))
}


// 사용 예
// The letter "a" is before "c" yielding a negative value
'a'.localeCompare('c'); // -2 or -1 (or some other negative value)

// Alphabetically the word "check" comes after "against" yielding a positive value
'check'.localeCompare('against'); // 2 or 1 (or some other positive value)

// "a" and "a" are equivalent yielding a neutral value of zero
'a'.localeCompare('a'); // 0

// Sort an array
let items = ['réservé', 'premier', 'cliché', 'communiqué', 'café', 'adieu'];
items.sort((a, b) => a.localeCompare(b)); // ['adieu', 'café', 'cliché', 'communiqué', 'premier', 'réservé']