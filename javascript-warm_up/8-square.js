#!/usr/bin/node

const val = parseInt(process.argv[2]);
let i = 0;
let j = 0;
let square = '';
if (!Number.isInteger(val)) {
  console.log('Missing size');
} else {
  for (;i < val; i++) {
    for (;j < val; j++) {
      square = square + 'X';
    }
    console.log(square);
  }
}
