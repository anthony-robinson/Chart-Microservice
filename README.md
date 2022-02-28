# Chart Microservice

First, to begin you'll need python3 and the pip package manager.

## Setup 

Install Flask and quickcharts by running 

`pip install quickchart.io flask`

Start a server running

`python3 app.py`

in a terminal instance. 

## Making a Request

The server runs on http://127.0.0.1:5000/

the endpoint to create a line chart is 

`POST /line_chart`

The API accepts a POST request with the header
"Content-Type": "application/json"

Include the path to the file you'd like to write to,
the width, and heights and data attributes in the JSON.

![Here is an example](/assets/first_chart.png)

created by this JSON (slightly modified from the docs here https://quickchart.io/documentation/)

```
{
	 "path": "./assets/first_chart.png",
	 "width": "700",
	 "height": "500",
   "data":{
      "labels":[
         "January",
         "February",
         "March",
         "April",
         "May",
         "June",
         "July"
      ],
      "datasets":[
         {
            "label":"My First dataset",
            "backgroundColor":"rgb(255, 99, 132)",
            "borderColor":"rgb(255, 99, 132)",
            "data":[
               93,
               -29,
               -17,
               -8,
               73,
               98,
               40
            ],
            "fill":false
         },
         {
            "label":"My Second dataset",
            "fill":false,
            "backgroundColor":"rgb(54, 162, 235)",
            "borderColor":"rgb(54, 162, 235)",
            "data":[
               20,
               85,
               -79,
               93,
               27,
               -81,
               -22
            ]
         }
      ]
   },
   "options":{
      "title":{
         "display":true,
         "text":"My Cool Chart"
      }
   }
}
```

![Example 2](/assets/next_chart.png)
{
	 "path": "./assets/next_chart.png",
	 "width": "700",
	 "height": "700",
   "data":{
      "labels":[
				0,
				1,
				2,
				3,
				4,
				5
      ],
      "datasets":[
         {
            "label":"My First dataset",
            "backgroundColor":"rgba(255, 99, 132, 0.5)",
            "borderColor":"rgb(255, 99, 132)",
            "data":[
               0,
               1,
               2,
               3,
							 4,
							 5
            ],
            "fill":true
         }
         
      ]
   },
   "options":{
      "title":{
         "display":true,
         "text":"Next Chart"
      }
   }
}


