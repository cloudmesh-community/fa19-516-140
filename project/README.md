# Project walking through...


### step 1
*setting up the server [installing requirements.txt]

`sudo -H install -r requirements.txt`

### step 2

#### *Starting the server*

`python3.7 server'api`

##### *Output should look like this:*
	
<img src="results/Start server.png"
     alt="Server start"
     style="float: left; margin-right: 10px;" />


### step 3
#### *Uploading the file to the server*

`curl -X POST "http://localhost:8080/project" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@sample.csv;type=text/csv"`

#### *Output should look like this:*

`{
  "filename": "model.csv", 
  "job_id": 0
}`

### step 4

`curl -X POST "http://localhost:8080/project/kmeans" -H "accept: text/csv" -H "Content-Type: application/json"}"
`

#### *response will be an output for the calculation of the kmeans in a plotting chart of clusters rpresenting each cluster associated with its centroid [mainly three clusters and three centroids] as followin:*

<img src="results/kmeans_centroid.png"
     alt="Server start"
     style="float: left; margin-right: 10px;" />


 
