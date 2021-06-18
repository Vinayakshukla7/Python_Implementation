## Heroku Basic Python Deployment 

Heroku is a cloud platform as a service (PaaS) that lets companies build, deliver, monitor, and scale apps. Heroku bypasses infrastructure headaches.<br>
Lets us focus on our app and deliver more value to customers.<br>

Dynos : Run virually any language at scale ,smart ,lightweight containers build for modern languages.<br>
Database : Enterprise grade PostgreSQL as a service.<br>
Add-one:Marketplace for data and app services (mongoDb,email sending,email delivery)<br>

Steps for deployment :
1. Created flask basic project locally .
2. Sign in to heroku platform from browser and created a app over free tier named as flas-fi.
3. On app setting added buildpack of "heroku/python".
4. Downloaded heroku cli .
5. Opened cmd promt from windows.
6. Logged in to herko using cli .
         heroku login
         
7.Under same directory where locally project is stored created file name Procfile with "web: gunicorn app:app" .<br>

8.Added requirements.txt file in the same directory using 
         pip freeze > requirements.txt
         
9.Create a new Git repository using cmd .<br>
          cd my-project/ <br>
          git init        <br>
          heroku git:remote -a flas-fi  <br>
          
10.Deploy your application<br>
   Commit your code to the repository and deploy it to Heroku using Git.<br>
          git add .  <br>
          git commit -am "make it better"   <br>
          git push heroku master        <br>

To open the deployed app        <br>
          heroku open     <br>

