function solution(arr1, arr2) {
  // for문 두 번 => map 두 번
  return arr1.map((arr, i) => arr.map((v, j) => v + arr2[i][j]))
}