// this program calculates the factorial of a number

function factorial_function(num) {
  // declare variable factorial that aids calculation and will hold result
  let factorial = 1;
  // iterate form num to 1 and multiply each whole number with factorial on the way
  for (let i = num; i > 0; i--){
    factorial *= i;
  }
  // return the result
  return factorial;
}

// declare user_num to hold number input from user
let user_num = Number(prompt('input a positive whole number: '));

// call function and output to console
console.log(factoral_function(user_num))
