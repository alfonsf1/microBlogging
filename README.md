Micro Blogging API
===============================
This project contains two RESTful back-end microservices. Our microvlogging API offers services similar to twitter.  

Contributors of the group project:  
---------------------------------- 
1) Alfonso Figueroa - Figueroa.a@csu.fullerton.edu  
2) Ryan Luong - Ryan12@csu.fullerton.edu  
  
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
1) git clone ``` https://github.com/alfonsf1/microBlogging.git ```      
2) To create the database   
   - Launch the terminal and type  
      ``` cd microBlogging ```  
      ``` $ sqlite3 timeline.db```  
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` sqlite> .read timeline.sql```  
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` sqlite> .exit ```  
      ``` $ sqlite3 user.db```  
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` sqlite> .read user.sql```  
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` sqlite> .exit ```  
3) To start the database    
   - In the terminal type:  
      ``` $ formman start ```  
4) Open a new terminal in the same directory and use the methods listed below;  
  
    
>localhost:5000 is connected to user.db  
  
>localhost:5100 is connected timeline.db  
  
  
Methods  
--------------  
- Crate User  
   - createUser function crates a user that is tied to a username, password, and an email  
      - Example  
      ``` $ http post localhost:5000/user username='Sergio' password='xyz789' email='Sergio@gmail.com' ```  

- Check Password  
   -  checkPassword functon takes in the parameters of a username and password and check it with the data base.  
      - Exanple  
      ``` $ http localhost:5000/user/password/Alfonso/abc123 ```  

- Add Follower   
   - addFollower function takes in the parameter of the username account and the name of the user they wish to follow.  
      - Example  
      ``` $ http POST localhost:5000/user/follower/add username="Alfonso" follower="Rosendo" ```  

- Remove Follower
   - removeFollower function takes in the parameter of the username account and the name of the user they wosh to unfollow  
      - Example  
      ``` $ http DELETE localhost:5000/user/follower/remove username="Alfonso" usernameToRemove="Rosendo" ```  
- User Timeline  
   - userTimeline gets all of the posts of the signed in user  
      - Example  
      ``` $ http GET localhost:5100/timeline/Alfonso ```  

- Public Timeline  
   - publicTimeline displays of the users posts from the micro blogging service  
      - Example  
      ``` $ http GET localhost:5100/timeline/public ```    

- Home Timeline  
   - homeTimeLine displays the post of the followers of the user  
      - Example  
      ``` $ http GET localhost:5100/timeline/home/Alfonso ```    

- Post Tweet  
   - postTweet function allows users to post to the timeline
      - Example  
      ``` $ http POST localhost:5100/timeline/create author="Alfonso" postText="Hello!, My name is Alfonso!" ```   

