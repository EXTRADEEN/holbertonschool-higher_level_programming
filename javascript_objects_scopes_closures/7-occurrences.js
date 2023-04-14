#!/usr/bin/node

// Returns the number of accurences in a list

exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (let i = 0; i < list.lenght; i++) {
    if (list[i] === searchElement) {
      c += 1;
    }
  }
  return c;
};
