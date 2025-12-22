code = "Ly8gcmV2ZXJzZV9idWdneS5qcwoKZnVuY3Rpb24gcmV2ZXJzZVdvcmRzKHNlbnRlbmNlKSB7CiAgY29uc3Qgd29yZHMgPSBzZW50ZW5jZS5zcGxpdCgiICIpOwogIGNvbnN0IHJldmVyc2VkID0gd29yZHMubWFwKHdvcmQgPT4gewogICAgcmV0dXJuIHdvcmQuc3BsaXQoIiIpLnJldmVyc2U7CiAgfSk7CiAgcmV0dXJuIHJldmVyc2VkLmpvaW4oIiAiKTsKfQoKLy8gU2ltcGxlIHRlc3QKY29uc29sZS5sb2cocmV2ZXJzZVdvcmRzKCJIZWxsbyB3b3JsZCIpKTsgCi8vIEV4cGVjdGVkOiAib2xsZUggZGxyb3ci"


import base64
decoded = base64.b64decode(code)
print(decoded.decode("utf-8"))



text = '''// reverse_buggy.js

function reverseWords(sentence) {
  const words = sentence.split(" ");
  const reversed = words.map(word => {
    return word.split("").reverse().join("");
  });
  return reversed.join(" ");
}

// Simple test
console.log(reverseWords("Hello world")); 
// Expected: "olleH dlrow"'''

encoded = base64.b64encode(text.encode("utf-8"))

print(encoded.decode("utf-8"))