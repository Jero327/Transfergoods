===
April 1st 2020-Started @ 6:30PM
Going to work on Auth function, to try and implement register and related url.
Estimate: 60 minutes

9PM: Finished implement Auth register, after which there will pop up a message to tell user wether register done or not.
Actual time taken: ~2.5 hours.

Stopped @ 10PM
===
April 2nd 2020-Started @ 7PM
Going to work on Optimizing URL, cause there will be urls before and after being authenticated.
Estimate: 30 minutes

7.30PM: By {% if user.is_authenticated %}, judging whether the user is authenticated. By add 'LOGOUT_REDIRECT_URL' and 'LOGIN_REDIRECT_URL', to handle when user login in and log out redirect.

8PM: Finished.
Actual time taken: ~1hour.

Stopped @ 8.30PM
===
April 5th 2020-Started @ 10AM
Going to work on publish new orders and prevent login or register again when user has authentication.
Estimate: 4 hours

12AM: show message to tell user that they have already log in when request login or register url by {% if user.is_authenticated %}=>{% else %}
3.30PM: Users could publish new needs and service orders through form.save and save to database, meanwhile, they can upload images to server-side by models.ImageField

4PM: Finished publish functions
Actual time taken: 6 hours.

Stopped @ 4PM
===
April 6th 2020-Started @1PM
Going to implement display published items to all users.
Estimate: 1.5 hours

2PM: Define new funciton in View.py to obtain data from the database then pass them to display html
2.30PM: Finished displaying
Actual time taken: 1.5 hour.

Stopped @ 3PM
===
April 8th 2020-Started @3.30PM
BUG: Orders other than newly published have been displayed to public bu mistake
Fixing Bug Estimate: 1hour

4.30PM: Finished fixing bug by filter orders by orders'status before displaying
5PM: Going to convert database from sqlite to POSTgreSQL.
Estimate: 2 hours

7PM: Finished converting.
Actual time taken: 2 hours.

Stopped @ 8PM
===
