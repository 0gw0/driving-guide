# DRIVING LICENSE GUIDE
#### VIDEO Demo: <https://youtu.be/MXk4OJkZV_0>
#### Description:
This web application helps guide private students trying to get a driving license. By first asking where they want to enrol in and which stage of the learning journey they are in, the web application is able to give better advice.

The login.html and register.html is to keep data on users so as they complete different milestones in their journey over a few months the website remembers their progress ad they don’t need to keep updating the website

The progress.db file stores the information from register.html. It is filled with 2 main components (1st is user and 2nd is progress with 5 boolean condition to indicate which level of progress each user is at)

Helpers.py contains some stuff from prev weeks like apology msgs but also with new stuff like the function  getpercentage and getstep which check the progress database to see what milestone the person has completed and return percentage done and next step respectively

Styles.css contains some inspiration from prev cs50 labs and psets

Favicon.ico is my own .ico image made from a bit of photoshop editing

Design-wise at first I wanted first time users  to get sent to a qns.html page that would ask how far along the driving journey they are then be redirected to the index.html page. However I combined it with the checkbox system that you see in the index.html page now as the index.html page ended up looking empty.  The new index.html page then seemed like it was showing the user their progress better and that inspired me to do a progress bar to further build on that concept.