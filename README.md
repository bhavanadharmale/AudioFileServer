# AudioFileServer

Note: 
1. uploadedTime will taken care by backend part, the value should be current date and time. And this value can't be editted
2. In update user cannot update id and date_time
## Pre-requisite:
* Install XAMPP
* enable apache and mysql server from XAMPP
* create database "flask"

## Create API
### Song:
* url: http://127.0.0.1:5000/create/Song
* method : POST
* body :
{
    "ID": 2, 
    "songName": "Faded_New", 
    "durationSec": 500
}

#########################################################

### Podcast:
* url: http://127.0.0.1:5000/create/Podcast
* method : POST
* body :
{
    "ID": 1, 
    "podcastName": "Ted Talk-1", 
    "durationSec": 15000, 
    "host": "Steave Jobs", 
    "participants": "Bhavana"
}

########################################################

### Audiobook:
* url: http://127.0.0.1:5000/create/Audiobook
* method : POST
* body :
{
    "ID": 1, 
    "title": "World War-II", 
    "author": "Hitler", 
    "narrator": "Bose", 
    "durationSec": 20000, 
}
########################################################


## Delete API : Example
### Song:
* url : http://127.0.0.1:5000/delete/Song/1
* method : POST

#########################################################

### Podcast:
* url : http://127.0.0.1:5000/delete/Podcast/1
* method : POST

########################################################

### Audiobook:
* url : http://127.0.0.1:5000/delete/Audiobook/1
* method : POST

## Update API : Example
### Song:
* url : http://127.0.0.1:5000/update/Song/1
* method : POST
* body :
{
    "songName": "Closer", 
}

#########################################################

### Podcast: 
* url : http://127.0.0.1:5000/update/Podcast/1
* method : POST
* body :
{
    "podcastName": "Ted Talk"
}

########################################################

### Audiobook:
* url : http://127.0.0.1:5000/update/Audiobook/1
* method : POST
* body :
{
    "title":"World War-II",
    "author":"Adolf Hitler",
    "narrator": "Bose"
}


## get API : Example
### Song: 
* url-1 : http://127.0.0.1:5000/get/Song/1
* url-2 : http://127.0.0.1:5000/get/Song
* method : POST

#########################################################

### Podcast:
* url-1 : http://127.0.0.1:5000/get/Podcast/1
* url-2 : http://127.0.0.1:5000/get/Podcast
* method: POST

########################################################

### Audiobook:
* url-1 : http://127.0.0.1:5000/get/Audiobook/1
* url-2 : http://127.0.0.1:5000/get/Audiobook
* method : POST

########################################################
