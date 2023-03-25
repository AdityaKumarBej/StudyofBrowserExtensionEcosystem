const fs = require('fs');
const json2csv = require('json2csv').parse;

const filePaths = ['myjsonfile_1_100_core.json', 'myjsonfile_101_200_core.json', 'myjsonfile_201_300_core.json', 
'myjsonfile_301_400_core.json', 'myjsonfile_401_500_core.json', 'myjsonfile_501_600_core.json']
// Read the JSON data from file
const jsonData = JSON.parse(fs.readFileSync('myjsonfile_501_600_core.json', 'utf-8'));

// Filter the data based on the value in the array
const filteredData = jsonData.filter(obj => obj.permissions.includes('mozillaAddons'));

console.log("checking filtered data", )
// Define the fields to include in the CSV
const fields = ['id', 'name', 'publisher', 'rating', 'rating_count', 'user_count'];

// Convert the filtered data to CSV
const csvData = json2csv(filteredData, { fields });
``
// Write the CSV data to file
// fs.writeFile('mozillaAddons.csv', csvData, err => {
//   if (err) throw err;
//   console.log('CSV file saved!');
// });

fs.appendFile('mozillaAddons.csv', csvData, err => {
    if(err){
    console.log("some error", err);
    }
console.log('CSV file appended!');
})