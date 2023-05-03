/* this program checks if a number is prime or not. it's based on
https://www.programiz.com/python-programming/examples/prime-number &
https://www.scaler.com/topics/prime-number-in-javascript/ */

// declare variable 'n' and store number from user in it
let n = Number(prompt('Enter a number: '));
// declare not prime 'flag' and initialize it to false
let flag = false;

// we know that only numbers > 1 can be prime
if (n > 1){
  // iterate from 2 to 'n'/2 included
  for (let i = 2; i <= n/2; i++){
    if (n % i === 0){ // check for factors. if remainder === 0 declare not prime, set 'flag' to true and terminate iteretion
      console.log(n + ' is not a prime number');
      console.log(i + ' times ' + n / i + ' is ' + n);
      flag = true;
      break;
    }  
  }
  // if no divisor found with no remainder, 'flag' should be left false, therefore number is PRIME
  if (flag == false){
    console.log(n + ' is a prime number');
  }
}
// input is less or equal to 0 therefore not a prime number
else {
  console.log(n + ' is not a prime number');
}
