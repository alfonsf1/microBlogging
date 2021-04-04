Micro Blogging API With Authentication  
===============================
This project contains two RESTful back-end microservices. Our microvlogging API offers services similar to twitter.  

Contributors of the group project:  
---------------------------------- 
1) Alfonso Figueroa - Figueroa.a@csu.fullerton.edu  
2) Ryan Luong - Ryan12@csu.fullerton.edu  
  
Recent Changes  
===============================  
1) Added two new services to timeline and user  
2) to test new changes: $ http GET localhost:5000/home/Alfonso   
  
Technologies      
===============================
1) Python  
2) Bottle Framework  
3) SQLite3  
4) MySQL  
5) Foreman  
6) HTTPie  
7) Authentication   

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
      ``` $ foreman start -m gateway=1,users=1,timelines=3 ```  
4) Open a new terminal in the same directory and use the methods listed below;  
  
    
>localhost:5000 is connected gateway.py  

>localhost:5100 is connected to user.py  
  
>localhost:5200 is connected timeline.py   
  
  
Methods  
--------------  
- Crate User  
   - createUser function crates a user that is tied to a username, password, and an email  
      - Example  
      ``` $ http post localhost:5100/user username="Sergio" password="xyz789A12" email="Sergio@gmail.com" ```  

- Check Password  
   -  checkPassword functon takes in the parameters of a username and password and check it with the data base.  
      - Exanple  
      ``` $ http get localhost:5100/user/Alfonso/adwO12312 ```  

- Add Follower   
   - addFollower function takes in the parameter of the username account and the name of the user they wish to follow.  
      - Example  
      ``` $ http post localhost:5100/user/follower/add username="Alfonso" follower="Rosendo" ```  

- Remove Follower
   - removeFollower function takes in the parameter of the username account and the name of the user they want to unfollow  
      - Example  
      ``` $ http DELETE localhost:5100/user/follower/remove username="Alfonso" follower="Rosendo" ```  
- User Timeline  
   - userTimeline gets all of the posts of the signed in user  
      - Example  
      ``` $ http GET localhost:5200/timeline/Alfonso ```  

- Public Timeline  
   - publicTimeline displays of the users posts from the micro blogging service  
      - Example  
      ``` $ http GET localhost:5200/timeline/public ```    

- Home Timeline  
   - homeTimeLine displays the post of the followers of the user  
      - Example  
      ``` $ http GET localhost:5200/timeline/home/Alfonso ```    

- Post Tweet  
   - postTweet function allows users to post to the timeline
      - Example  
      ``` $ http post localhost:5200/timeline/create author="Alfonso" text="Hello! Today is Monday" ```  
  
-  Gateway Function  
   - Uses gateway function to communicate with user and timline service to retieve timiles for the specified user  
      - Example  
      ``` $ http GET localhost:5000/home/Alfonso```  



