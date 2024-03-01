// This is a long comment in JavaScript. It's intended to test the overflow and how well comments, strings,
// and various syntax elements are highlighted in your editor.

function calculateArea(radius) {
  return Math.PI * Math.pow(radius, 2);
}

function greet(name) {
  console.log(`Hello, ${name}!`);
}

class MyClass {
  constructor(name) {
    this.name = name;
  }

  displayName() {
    console.log(`Name: ${this.name}`);
  }
}

const myObject = new MyClass('Sample Object');
myObject.displayName();

document.addEventListener('DOMContentLoaded', (event) => {
  greet('Bob');
  console.log(`Area: ${calculateArea(5)}`);

  // Fetch example to test syntax highlighting for promises
  fetch('https://api.example.com/data')
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));
});
