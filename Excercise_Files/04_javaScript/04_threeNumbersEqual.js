// JS program that takes three numbers from user, and tells if all equal, all different or in-between

// user input three numbers
let num1 = Number(prompt('First number: '));
let num2 = Number(prompt('Second number: '));
let num3 = Number(prompt('Third number: '));

// check if they are all equal
if (num1 === num2 && num1 === num3){
  console.log('All numbers are equal');
}
// check if they are all different
else if (num1 != num2 && num1 != num3 && num2 != num3){
  console.log('All numbers are different');
}
// if neither of the above, fall back to this
else {
  console.log('Neither all are equal or different');
}
