// JS program that gives you the 10 times multiplication table of a chosen number

// user input
let base = Number(prompt('Which whole number do you choose for your multiplication table? '));

// a for loop to do the multiplication 10 times
// variable i will also act as the multiplier
// print it all on screen
for (let i = 1; i <= 10; i++) {
  console.log(base + ' x ' + i + ' = ' + base * i);
}
