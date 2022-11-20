function pivotIndex(nums: number[]): number {
  const total = nums.reduce((r, c) => r + c, 0);
  let leftSum = 0;
  for (let i = 0; i < nums.length; i++) {
    const current = nums[i];
    if (leftSum == total - leftSum - current) {
      return i;
    }
    leftSum += current;
  }
  return -1;
}
