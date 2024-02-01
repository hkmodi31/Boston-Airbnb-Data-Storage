# Boston Airbnb Data Storage & Visulisation

Boston is the 4th most crowded cities in the United States. (Source: https://www.rent.com/blog/most-crowded-cities-in-america/) Finding a stay here can be pretty overwhelming. With many options available, one might want to know what is the best one. Though there are many hotels in and around, finding a homestay for both, short term or long term, can be challenging. Thanks to a well built airbnb network here, one has many options to chose from.

## Inspiration
I created this project to provide analytics of the airbnb network in Boston, showcasing well rated areas, top-rated listings, map visulisation of the airbnb with each listing's crucial information and top rated hosts.

## Solution
The goal was to create an end-to-end pipeline of data extraction, processing, storage and analytics. The tools used to achieve this were python (pandas, numpy, pscopg2, os), PostGreSQL and Tableau.

## Step-wise approach
### Step - 1: Find a reliable data source
Finding a data source in this project is crucial as we need a data source that is updated regularly and has all the required information that we need to show our visulisations. The datasource I used in this project is "inside AirBnb" (Source: http://insideairbnb.com/explore/). This website gives quaterly updated airbnb details of many major cities in the world, Boston being one.

### Step - 2: Processing the data
The data, once extracted from the website, needs to be processed tobe stored on different tables. From the datasource, we have three files - listings, reviews, neighbourhoods. Our initial step is to divide these data into different tables in order to reduce data redundacy when stored in a database. Once that is achieved, our next step is to remove NaN values and duplicate rows.

### Step - 3: Storing the data.
Using python and psycopg2 library, I made a database in PostGreSQL on my local server and performed CRUD operations on it. My database consisted of 7 tables.
![QuickDBD-Free Diagram](https://github.com/hkmodi31/Boston-Airbnb-Data-Storage/assets/47323046/c7dba4ac-73d7-4190-b6f4-c76b304dfeab)

### Step - 4: Connecting the data source to Tableau
My initial goal was to create a connection between PostGreSQL and Tableau to make a live data visulisation that shows changes when any operations are made on the database. However, to make that connection, one needs the paid plan of Tableau.

So my current approach uses csv files to create a data source in Tableau and perform visulisations on the same.
<img width="1202" alt="image" src="https://github.com/hkmodi31/Boston-Airbnb-Data-Storage/assets/47323046/75056fc7-3861-40f6-8a9c-21f546971d39">

The final Tableau story can be viewed here - 
<div class='tableauPlaceholder' id='viz1706818964301' style='position: relative'><noscript><a href='#'><img alt='Boston Airbnb - Insights from the top ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;BostonAirbnbAnalytics&#47;Bostonstory&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='BostonAirbnbAnalytics&#47;Bostonstory' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;BostonAirbnbAnalytics&#47;Bostonstory&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1706818964301');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
