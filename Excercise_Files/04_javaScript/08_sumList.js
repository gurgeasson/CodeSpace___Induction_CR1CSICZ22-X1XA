// this program sums values of an array

// declare array
let arrayToSum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
//console.log(arrayToSum);
// count number of items in array
let arrayToSumLen = arrayToSum.length;
//console.log(arrayToSumLen);
// declare and initiate the avriable sum
let sum = 0;

// iterate through the array and sum all items
for (let i = 0; i < arrayToSumLen; i++) {
  sum += arrayToSum[i];
  //console.log(arrayToSum[i]);
}
// print sum on screen
console.log('the sum of array is: ' + sum);
