**Basics of web scraping in JavaScript.**<br>
There are mainly two parts to web scraping.<br>
1.Getting the data using request libraries and a headless browser.<br>
2.Parsing the data to extract the exact information that we want from the data.<br>

Requirements : NodeJS installation.<br>

We are going to use the packages **node-fetch** and **cheerio** for web scraping in JavaScript.Setup the project with the npm to work with a third-party package.<br>


Steps to complete our setup.<br>
Create a directory called web_scraping and navigate to it.<br>
Run the command npm init to initialize the project.<br>
Answer all the questions based on your preference.<br>
Now, install the packages using the command<br>

npm install node-fetch cheerio<br>


**node-fetch**<br>
The package node-fetch brings the window.fetch to the node js environment. It helps to make the HTTP requests and get the raw data.


**cheerio**<br>
The package cheerio is used to parse and extract the information that is necessary from the raw data.<br>


We will see the flow of web scraping and the most useful methods in that flow.<br>


**What are we extracting?**<br>
 Wikipedia Cricket World Cup page to get the desired information.<br>
 
 Create a file called extract_cricket_world_cups_list.js in the project.<br>
 
 First, get the raw data using the node-fetch package.<br>
 
**Below code gets the raw data of the above Wikipedia page.**<br>

    const fetch = require("node-fetch");

    // function to get the raw data

    const getRawData = (URL) => {

      return fetch(URL)
   
      .then((response) => response.text())
      
      .then((data) => {
      
         return data;
         
       });
      
       };

      // URL for data
       const URL = "https://en.wikipedia.org/wiki/Cricket_World_Cup";

        // start of the program
        const getCricketWorldCupsList = async () => {
           const cricketWorldCupRawData = await getRawData(URL);
           console.log(cricketWorldCupRawData);
        };

        // invoking the main function
        getCricketWorldCupsList();
       
 We got the raw data from the URL. Now see the basic extraction using cheerio.<br>
 
 **Parse the HTML data using cheerio.load the method.**
        
        const parsedSampleData = cheerio.load(
      `<div id="container"><p id="title">I'm title</p></div>`
          );
 We have parsed the above HTML code. How to extract the p tag content from it<br>
         
         console.log(parsedSampleData("#title").text());
         
         
 Now, it’s time to extract the world cup list. To extract the information, we need to know the HTML tags that information lies on the page.<br>
 
       const cheerio = require("cheerio");

       const getCricketWorldCupsList = async () => {
         const cricketWorldCupRawData = await getRawData(URL);

         // parsing the data
         const parsedCricketWorldCupData = cheerio.load(cricketWorldCupRawData);

         // extracting the table data
         const worldCupsDataTable = parsedCricketWorldCupData("table.wikitable")[0]
            .children[1].children;

         console.log("Year --- Winner --- Runner");
         worldCupsDataTable.forEach((row) => {
            // extracting `td` tags
            if (row.name === "tr") {
               let year = null,
                  winner = null,
                  runner = null;

               const columns = row.children.filter((column) => column.name === "td");

               // extracting year
               const yearColumn = columns[0];
               if (yearColumn) {
                  year = yearColumn.children[0];
                  if (year) {
                     year = year.children[0].data;
                  }
               }

               // extracting winner
               const winnerColumn = columns[3];
               if (winnerColumn) {
                  winner = winnerColumn.children[1];
                  if (winner) {
                     winner = winner.children[0].data;
                  }
               }

               // extracting runner
               const runnerColumn = columns[5];
               if (runnerColumn) {
                  runner = runnerColumn.children[1];
                  if (runner) {
                     runner = runner.children[0].data;
                  }
               }

               if (year && winner && runner) {
                  console.log(`${year} --- ${winner} --- ${runner}`);
               }
            }
         });
      };

      // invoking the main function
      getCricketWorldCupsList();
 
**we get output as a**
    Year --- Winner --- Runner    <br>
    1975 --- West Indies --- Australia <br>
    1979 --- West Indies --- England  <br>
    1983 --- India --- West Indies<br>
    1987 --- Australia --- England<br>
    1992 --- Pakistan --- England<br>
    1996 --- Sri Lanka --- Australia<br>
    1999 --- Australia --- Pakistan<br>
    2003 --- Australia --- India<br>
    2007 --- Australia --- Sri Lanka<br>
    2011 --- India --- Sri Lanka<br>
    2015 --- Australia --- New Zealand<br>
    2019 --- England --- New Zealand<br>
