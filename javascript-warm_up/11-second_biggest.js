#!/usr/bin/node

function second_biggest (arr) {
  let first = -1; let second = -1;

  for (let i = 0; i <= arr.length - 1; i++) {
    if (arr[i] > first) {
      second = first;
      first = arr[i];
    } else if (arr[i] > second && arr[i] != first) {
      second = arr[i];
    }
  }
  console.log(second);
}
const arr = process.argv;
second_biggest(arr);
