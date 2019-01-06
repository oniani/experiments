/*
 * Author: David Oniani
 * License: MIT
 * Purpose: A function to check the primality of the number
 */

function isPrime(num) {
    for (var i = 2; i <= Math.sqrt(num); i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

function generatePrimes(upTo) {
    var primes = [];
    for (var i = 2; i <= upTo; i++) {
        if (isPrime(i)) {
            primes.push(i);
        }
    }
    return primes;
}

function generatePrimesImproved(upTo) {
    return [...Array(upTo + 1).keys()].slice(2).filter(isPrime);
}


function test() {
    console.log("Checking the primality of the numbers...");
    console.log(isPrime(11));
    console.log(generatePrimes(11));
    console.log(generatePrimes(50));

    // Lambda expression
    let adder = (a, b) => a + b;
    console.log(adder(1, 2));

    // Using map
    let square = (a) => Math.pow(a, 2);
    console.log([1, 2, 3, 4, 5].map(square));

    // Improved prime generator
    console.log(generatePrimesImproved(11));
    console.log(generatePrimesImproved(50));
}


test();
