// this program finds the Min and Max of an array

// declare array
let minMaxArray = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49];
 // list original list before sorting
console.log('Original List:' + minMaxArray);
/*
https://stackoverflow.com/questions/1063007/how-to-sort-an-array-of-integers-correctly
*/
// numeric sort array ascending
minMaxArray = minMaxArray.sort(function (a, b) {  return a - b;  });
// console.log('sorted List: ' + minMaxArray);

// find and print Max value
console.log('Maximum value for the above list = ' + minMaxArray[minMaxArray.length - 1]);
// find and print Min value
console.log('Minimum value for the above list = ' + minMaxArray[0]);
