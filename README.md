# DRIVING LICENSE GUIDE
#### VIDEO Demo: <https://youtu.be/MXk4OJkZV_0>
#### Description:
This web application helps guide private students trying to get a driving license. By first asking where they want to enrol in and which stage of the learning journey they are in, the web application is able to give better advice.

The login.html and register.html is to keep data on users so as they complete different milestones in their journey over a few months the website remembers their progress ad they don’t need to keep updating the website.

Appointment.html is the first page and step users get directed to if their progressbar is at 0%. it shows the user 3 options of schools they can join and has a hyperlink to the e-appointment page of repective schools.

Test.html is the second page users get directed to after they have made an appoint and went down to the school to make their account. For both BTT and FTT (which stand for Basic theory test and Final theory test respectively) users are redirected to this page as they are very similar and design-wise i thought it would be better to keep all the information on theory test on the same page for better reference. Althoguh the page is the same for both BTT & FTT the progress bar still increases when users have completed each step

simulator.html might be the least overwhelming page as the website for all three schools do not allow or display available dates online unless users are logged in to their account made with the school. Thus I put a youtube video to let learners know what to expect instead.

Tips.html is the final page a user will see before he/she gets their license, is has final tips and tricks to pass the practical test in the form of a youTube video on the screen.

layout.html and apology have been adopted from week 9:flask and modified for the purpose of this project. For instance, layout now has a dropdown menu for all the steps a learner has to take to get his/her driving license, this helps users to get a better overview of the requirements to get a driving license in Singapore.

The progress.db file stores the information from register.html. It is filled with 2 main components (1st is user and 2nd is progress with 5 boolean condition to indicate which level of progress each user is at).

Helpers.py contains some stuff from prev weeks like apology msgs but also with new stuff like the function  getpercentage and getstep which check the progress database to see what milestone the person has completed and return percentage done and next step respectively.

Styles.css contains some inspiration from prev cs50 labs and psets like the color of the navbar words (SGS DRIVERS GUIDE) with SG being red as it is the color of the flag.

In static there are a few images like Favicon.ico, it is my own .ico image made from a bit of photoshop editing. The other pngs are the different logos for the 3 main driving schools in Singapore that people go to. they are used to the html pages for BTT and FTT test dates.

Design-wise at first I wanted first time users  to get sent to a qns.html page that would ask how far along the driving journey they are then be redirected to the index.html page. However I combined it with the checkbox system that you see in the index.html page now as the index.html page ended up looking empty.  The new index.html page then seemed like it was showing the user their progress better and that inspired me to do a progress bar to further build on that concept.

Overall I still feel like there are alot of room for improvement that can be done in the future. The one that bugs me the most is the reduncy of certain parts of code like that in the getpercentage function in helpers.py. It has the calling of 5 db.excute(UPDATE a IN users to True) when i feel like it can be done in a loop. However when i made the milestones into a dictionary so that i can loop over it, the results given were not 1 or 0 instead it gave {"a", 'a'}. Another visual update i would like to add would be to check the database to change index.html such that if milestone == True the checkbox would be disabled and indicated that it has been ticked already.