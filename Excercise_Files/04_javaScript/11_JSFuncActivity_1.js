// this program employs two functions. one to print list content, the other to find max value

// print function
function print_function(toPrintInput) {
  console.log('The content of the list is: ' + toPrintInput);
}

// find max value of an array function
function findMax_function(findMaxInput){
  /*
  https://stackoverflow.com/questions/1063007/how-to-sort-an-array-of-integers-correctly
  */
  // sort array numerically
  findMaxInput = findMaxInput.sort(function (a, b) {  return a - b;  });
  //console.log(findMaxInput);
  // return last element, which is the greatest
  console.log('The max value in the list: ' + findMaxInput[findMaxInput.length - 1]);
}

// declare the array
let funcArray = [10, 2, 3, 4, 7];

// call functions
print_function(funcArray);
findMax_function(funcArray);
