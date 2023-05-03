// simple program that takes three numbers from user, and tells if they increase/decrease/neither

// user input three numbers
let num1 = Number(prompt('First number: '));
let num2 = Number(prompt('Second number: '));
let num3 = Number(prompt('Third number: '));

// check if decreasing
if (num1 > num2 && num2 > num3){
  console.log('Decreasing order');
}
// or increasing
else if (num1 < num2 && num2 < num3){
  console.log('Increasing order');
}
// or neither increasing or decreasing
else {
  console.log('Neither increasing or decreasing order');
}
