// this program calculates the average of the items of an array

// declare array
let arrayToAvg = [20, 30, 25, 35, -16, 60, -100];
// count and store number of items in array
let arrayToAvgLen = arrayToAvg.length;
// declare and initiate sum
let sum = 0;

// iterate through array and sum all items
for (let i = 0; i < arrayToAvgLen; i++) {
  sum += arrayToAvg[i];
}

// declare and calculate average
let avg = sum / arrayToAvgLen;

// print average
console.log('the average of array is: ' + avg);
