function solution(s) {
  // split-apply-combine
  return s.split('').sort((p, c) => c.charCodeAt() - p.charCodeAt()).join('');
}