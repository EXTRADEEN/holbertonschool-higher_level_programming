#!/usr/bin/node

const val = process.argv;

if (val[2] == null) {
  console.log('No argument');
} else {
  console.log(val[2]);
}
