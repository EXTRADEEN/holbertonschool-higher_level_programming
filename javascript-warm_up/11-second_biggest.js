#!/usr/bin/node

function findSecondLargestElem (arr) {
  let first = -1; let second = -1;

  for (let i = 0; i <= arr.length - 1; i++) {
    if (arr[i] > first) {
      second = first;
      first = arr[i];
    } else if (arr[i] > second && arr[i] !== first) {
      second = arr[i];
    }
  }
  console.log(second);
}
const array = process.argv;
let idx = 2;
const tab = [];
while (idx in array) {
  tab.push(+array[idx]);
  idx++;
}
if (idx === 2) {
  console.log(0);
} else if (idx === 3) {
  console.log(0);
} else {
  findSecondLargestElem(tab);
}
