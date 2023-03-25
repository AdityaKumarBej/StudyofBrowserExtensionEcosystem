const axios = require('axios');
const fs = require('fs');

const urls = [
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=1&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=2&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=3&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=4&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=5&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=6&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=7&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=8&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=9&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=10&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=11&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=12&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=13&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=14&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=15&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=16&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=17&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=18&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=19&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=20&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=21&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=22&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=23&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=24&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=25&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=26&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=27&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=28&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=29&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=30&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=31&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=32&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=33&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=34&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=35&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=36&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=37&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=38&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=39&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=40&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=41&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=42&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=43&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=44&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=45&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=46&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=47&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=48&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=49&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=50&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=51&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=52&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=53&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=54&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=55&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=56&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=57&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=58&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=59&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=60&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=61&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=62&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=63&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=64&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=65&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=66&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=67&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=68&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=69&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=70&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=71&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=72&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=73&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=74&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=75&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=76&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=77&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=78&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=79&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=80&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=81&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=82&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=83&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=84&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=85&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=86&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=87&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=88&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=89&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=90&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=91&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=92&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=93&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=94&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=95&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=96&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=97&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=98&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=99&page_size=40000&type=extension',
    'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=100&page_size=40000&type=extension',
];


// Use Promise.all() to fetch data from all URLs concurrently
Promise.all(urls.map(url => axios.get(url)))
  .then(responses => {
    // Read the existing JSON data from the file

    let count = 0;
    let masterBatch = [];
    for (const response of responses) { //for each page
        //console.log("for response", response.data.results);

        for(var i = 0 ; i < response.data.results.length ; i++){    //iterating over 50 responses
            // var manifestBatch = (response.data.results);
            var id = response.data.results[i].id;  
            var name = response.data.results[i].slug;
            var publisher = response.data.results[i].authors;
            var rating = response.data.results[i].ratings.average;
            var rating_count = response.data.results[i].ratings.count;
            var user_count = response.data.results[i].average_daily_users;

            var tempObj = {
                'id': id,
                'name': name,
                'publisher': publisher,
                'rating': rating,
                'rating_count': rating_count,
                'user_count': user_count,
                'permissions': response.data.results[i].current_version.files[0].permissions
            }
            masterBatch.push(tempObj);
        }
            //permissions - current_version/files/
  
        count++;
      }

      //console.log("the masterbatch is", JSON.stringify(masterBatch));

      fs.writeFile('myjsonfile_1_100_core.json', JSON.stringify(masterBatch), err => {
        if(err){
            console.log("error in writing to file", err);
        }else{
            console.log("writing success");
        }
    });
  })
  .catch(error => {
    console.error(error);
  });
