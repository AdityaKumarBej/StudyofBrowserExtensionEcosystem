const fs = require('fs');
const path = require('path');
const directory = 'chrome_set';

function clean(){
    fs.readdir(directory, (err, files) => {
        if (err) throw err;
      
        files.forEach(file => {
          const filePath = path.join(directory, file);
          const stat = fs.statSync(filePath);
          if (stat.isFile() && path.extname(file) === '.json' && stat.size === 0) {
            fs.unlinkSync(filePath);
          }
      
      fs.readFile(filePath, 'utf-8', (err, data) => {
        if (err) throw err;
      
        try {
          JSON.parse(data);
          console.log('The JSON file is valid JavaScript.');
        } catch (e) {
          console.log('The JSON file is not valid JavaScript.');
          fs.unlinkSync(filePath);
        }
      });
      
        });
      });
}

function check_count_files(){

  fs.readdir(directory, (err, files) => {
    if (err) throw err;
  
    const jsonFiles = files.filter(file => path.extname(file) === '.json');
    const numberOfJsonFiles = jsonFiles.length;
  
    console.log(`Number of JSON files: ${numberOfJsonFiles}`);
  });
  
}

function count_json_obj(){

// Define the path to the input JSON file
const input_file = './datasets/firefox/post_presentation/merged_firefox_set.json';

// Load the JSON data from the file
const data = JSON.parse(fs.readFileSync(input_file, 'utf8'));

// Count the number of JSON objects in the array
const count = data.length;

// Log the count
console.log(count);

}

// check_count_files();
count_json_obj();

function extractDOMelements(){
// Replace this with the actual API URL
const apiUrl = 'https://chrome.google.com/webstore/detail/kconeelhhdbnjombompadmclijkcfbph'

// Make an API call and get the HTML content
fetch(apiUrl)
  .then((response) => {
    if (response.ok) {
      return response.text();
    } else {
      throw new Error(`Request failed with status code ${response.status}`);
    }
  })
  .then((htmlContent) => {
    // Parse the HTML content using DOMParser
    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlContent, 'text/html');

    // Find the title tag and extract its text
    const titleTag = doc.querySelector('title');
    if (titleTag) {
      const title = titleTag.textContent;
      console.log('Title:', title);
    } else {
      console.log('Title tag not found');
    }
  })
  .catch((error) => {
    console.error('Error:', error);
  });

}


//extractDOMelements();