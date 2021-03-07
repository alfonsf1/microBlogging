Micro Blogging API
===============================
This project contains two RESTful back-end microservices. Our microvlogging API offers services similar to twitter.  

Contributors of the group project:  
---------------------------------- 
1) Alfonso Figueroa - Figueroa.a@csu.fullerton.edu  
2) Ryan Luong - ryan12@csu.fullerton.edu  
  
Technologies      
===============================
1) Python  
2) Bottle Framework  
3) SQLite3  
4) MySQL  
5) Foreman  
6) HTTPie  

Install Technologies (Ubuntu)  
===============================
1) Foreman, httpie, sqlite3  
   ``` $ sudo apt install --yes python3-pip ruby-foreman httpie sqlite3  ```
2) Bottle and SQLite plugin for bottle  
   ``` $ python3 -m pip install bottle bottle-sqlite ```  

How to run project:
--------------------  
1) Download the files from git  
2) To run the microBlogging service  
   - Go to the directory in the terminal and type.  
      ``` $ foreman start```  

Methods  
--------------  
- Crate User  
   ``` $ http post localhost:5000/createUser username='Sergio' password='xyz789' email='Sergio@gmail.com' ```  

- Check Password  
   ``` $ http localhost:5000/checkPassword/Alfonso/abc123 ```  

- Add Follower   
   ``` $ http POST localhost:5000/addFollower username="Alfonso" follower="Rosendo" ```  

- Remove Follower  
   ``` $ http DELETE localhost:5000/removeFollower username="Alfonso" usernameToRemove="Rosendo" ```  
  
- User Timeline  
   ``` $ http GET localhost:5000/getUserTimeline/Alfonso ```  

- Public Timeline  
   ``` $ http GET localhost:5100/getPublicTimeline ```    

- Home Timeline  
   ``` $ http GET localhost:5100/getHomeTimeLine/Alfonso ```    

- Post Tweet  
   ``` $ http POST localhost:5100/postTweet author="Alfonso" postText="Hello!, My name is Alfonso!" ```   

