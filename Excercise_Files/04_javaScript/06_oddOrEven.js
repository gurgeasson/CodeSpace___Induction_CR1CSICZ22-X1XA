// JS program that takes a number from user, and tells if odd or even

// user input number
let oddOrEvenNum = Number(prompt('hit me with a number: '));

// is it ZERO?
if (oddOrEvenNum === 0){
  console.log(oddOrEvenNum + ' is ZERO');  
}
// check if it's even by looking at the remainder after dividing it by 2
else if (oddOrEvenNum % 2 === 0){
  console.log(oddOrEvenNum + ' is even');
}
// now surely it can only be odd
else {
  console.log(oddOrEvenNum + ' is odd');
}
