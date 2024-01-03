#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

if (!filePath) {
  console.error('Usage: node 0-readme.js <file_path>');
  process.exit(1); // Exit with an error code
}

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
