#!/usr/bin/node

// function that converts from base 10 to another base

exports.converter = function (base) {
  return function (conv) {
    return conv.toString(base);
  };
};
