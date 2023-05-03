// JS program that list the Fibonacci series between 0 to 50

// initiate array with first two number
let fiboSerie = [0, 1];
// initiate array item index
let i = 0;
while(fiboSerie[i] + fiboSerie[i + 1] < 50) {
  // use variable i to identify the preceding two numbers for next in line
  // calculate next in series and add it to list
  fiboSerie.push(fiboSerie[i] + fiboSerie[i + 1]);
  // increment the count
  i += 1;
} 

// print the List
console.log(fiboSerie);
