function runningSum(numbers: number[]): number[] {
  return numbers.map((number, index, array) => {
    const intermediateArray = array.slice(0, index);
    return intermediateArray.reduce(
      (result, current) => result + current,
      number
    );
  });
}

// memory optimized
function runningSum2(numbers: number[]): number[] {
  let runningSum: number[] = [];
  for (let i = 0, n = numbers.length; i < n; i++) {
    if (i == 0) {
      runningSum.push(numbers[i]);
      continue;
    }
    runningSum.push(numbers[i] + runningSum[i - 1]);
  }
  return runningSum;
}

// line optimized
function runningSum3(numbers: number[]): number[] {
  let val = 0;
  return numbers.map((res) => (val = res + val));
}
