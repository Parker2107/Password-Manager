Project Title: MasterKey
Name: Jeevesh Malhotra
GitHub Username: Parker2107
edX Username: Parker_2107
State and Country: Haryana, India
Date: 2nd Jan 2024
URL: https://youtu.be/Jp7OA24bNNs

Description:

After spending 10 weeks completing the Problem Sets and the labs, I was faced with a rather difficult task which was to make an entire project on my own. I couldn't figure out for the life of me what I should make as a final project until one day, I faced a problem and decided to solve said problem completely by myself.

My password manager, from McAfee got leaked and someone got their hands on all of my password stored there, causing me to immediately change upwards of 50 passwords. Even though 95% of the accounts were protected with 2FA, my youtube account got compromised and banned as a result.

So, as any true computer science student would, I decided to take this personally and instead of just being cautious with passwords, decided to build an offline, completely cutoff password manager using SQL, HTML, CSS, Python and Flask.

I used and took reference from the Finance website to tie the Login-Logout feature together because that was a bit confusing to me. The web-application is attached to an SQL database called "passwords.db" which has 2 tables, users and passwords.

Users - This table just stores the amount of users who have registered to use the web-application and assign a special user-id to all the users

Passwords - This table stores and is used to extract all the passwords. Every password that is added has a user-id which corresponds to the user-id of the user that was logged in when the password was added.

The web-application, after logging in, has an index page which displays all the passwords, an add page which is used to add passwords to the database by the user and a delete page which deletes existing passwords by verifying the username and password to be deleted.

Every add or delete is done after checking the User-id to make sure other users' data isn't compromised or tampered with accidentally.

The edge cases and most minor conditions are accounted for. In the future, features like updating passwords without deleting and re-adding them, beautifying the website login-logout method and adding safety features like 2FA can be implemented.

At its core, it was just a way for me, a 18 year old, who has just started his Bachelor's in Computer Science Engineering and have successfully crossed the barrier of the CLI output. It has been a very incredibly knowledgable course and has been the most raw exposure I have had to difficult problem-solving and coding in my life.

Thank You CS50!
# Password-Manager
