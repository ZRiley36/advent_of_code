// reverse_buggy.js

function reverseWords(sentence) {
  const words = sentence.split(" ");
  const reversed = words.map(word => {
    return word.split("").reverse().join("");
  });
  return reversed.join(" ");
}

// Simple test
console.log(reverseWords("Hello world")); 
// Expected: "olleH dlrow"