const axios = require('axios');
const fs = require('fs');

const urls = [

  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=501&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=502&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=503&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=504&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=505&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=506&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=507&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=508&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=509&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=510&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=511&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=512&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=513&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=514&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=515&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=516&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=517&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=518&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=519&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=520&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=521&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=522&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=523&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=524&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=525&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=526&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=527&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=528&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=529&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=530&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=531&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=532&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=533&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=534&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=535&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=536&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=537&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=538&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=539&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=540&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=541&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=542&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=543&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=544&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=545&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=546&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=547&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=548&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=549&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=550&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=551&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=552&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=553&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=554&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=555&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=556&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=557&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=558&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=559&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=560&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=561&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=562&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=563&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=564&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=565&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=566&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=567&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=568&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=569&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=570&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=571&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=572&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=573&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=574&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=575&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=576&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=577&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=578&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=579&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=580&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=581&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=582&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=583&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=584&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=585&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=586&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=587&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=588&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=589&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=590&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=591&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=592&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=593&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=594&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=595&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=596&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=597&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=598&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=599&page_size=40000&type=extension',
  'https://addons.mozilla.org/api/v4/addons/search/?app=firefox&page=600&page_size=40000&type=extension'
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
            var name = response.data.results[i].name["en-US"];  
     

            var tempObj = {
                'name': name,
                'id': response.data.results[i].id
            }
            masterBatch.push(tempObj);
        }
            //permissions - current_version/files/
  
        count++;
      }

      //console.log("the masterbatch is", JSON.stringify(masterBatch));

      fs.writeFile('name_and_id_mapping_500_600.json', JSON.stringify(masterBatch), err => {
        if(err){
            console.log("error in writing to file", err);
        }else{
            console.log("writing success");
        }
    });
  })
  .catch(error => {
    console.error(error);
  });//and compare it with final firefox csv to get the actual name