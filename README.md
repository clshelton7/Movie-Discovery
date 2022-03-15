# milestone3-cshelton7

#### 1. What are at least 3 technical issues you encountered with your project? How did you fix them? (Updated for Milestone 3)
  * When utilizing my state variables, I had initial issues with displaying reviews. The reviews would display as a blob of text, rather than their own entities. To mend this problem, I implemented props with a Review component that holds the review information (movie title, rating, comment) and displayed it by mapping state variables to that function. This paved way for the delete function/button and an overall cleaner Profile page.
  * At first, server communication was difficult to wrap my head around. I had difficulties with accessing specific elements of JSON responses until I used test cases and iterated through each response and printed every piece of information. I was finally able to get a functional iteration (through tests) to delete the correct information from the database (using JSON responses).
  * While gathering information for deleting reviews, the conflict of "indexing" reviews became an issue. I wasn't sure how to delete specific entries without compromising other information simply using the state variables that already existed. As a fix, I created a new state variable array to hold the spliced data (by setting the variable) removed from review state variables (ie: comments). With this new state array, I was able to communicate specific review information to the server for database deletion by setting.

#### 2. What was the hardest part of the project for you, across all milestones? What is the most useful thing you learned, across all milestones?
  * The most diffcult part of this set of milestones was adapting to new technologies. This project was by far one of the most incredible learning experiences I've had as a software developer at GSU, including the difficulties. Learning how to adjust to new syntaxes and libraries is a skill I've come to enjoy developing while it still being arduous and time-consuming. Specifically, the hardest part of this project involved implementing and utilizing new tools like React, Flask, data-extraction using APIS & databases.
  * All in all, the project itself was impactful to my development as a programmer. There were so many requirements that made me a better developer in the fact that I could tie everything we've learned together to make something! To avoid being too general, though, I will specifically point out the usefulness of setting goals and making a plan for a project. Across all milestones, pieces of the whole project were put together one at a time. First it was a Flask app with movie information, complete with API connections. Then, database inclusion was added with models, login functionality, user ratings. Finally, all of these are wrapped up as one big project with a personalized page addition that gives user more control over their movie rating experience. All of these things were tied together by setting and completing goals, whether we knew about specific requirements at first or not. Because this will help me in a corporate setting, rather than simply completing projects on my own, I would list is as one of the most useful things I learned throughout this project.

## Technologies Used

* VSCode
     * An IDE is a key resource in creating a program. I utilized pylint, and HTML autotag extension, Black, and other python extensions to make my life 10x easier while creating this web application.

* Heroku
     * Using Python with this cloud platform was super easy thanks to the interalized tools and others like Git. I was able to create, deploy, and run my app (mostly) without issue. Any time there was an error with my application, I would know immediately where to look thanks to the error code redirection. Using requirements.txt, I was able to notify the platform of necessary dependencies, much like my Procfile that told this specific app to use a web process for app.py.

* Git + GitHub
     * Git and Github are incredible resources to keep track of work and changes made while in the "coding zone". I didn't have to worry whether my applications crashed and burned, since all of my commits and data pushing could be found in the repository you're looking at now! I was able to make various comments when committing my work, a detail that prevents confusion (ie: "Hmm, what did I change since last time?"). I was able to make commits and push from my local repository via terminal by using the appropriate commands (git add, git commit, git push, etc). Pairing with the tools Heroku offers, saving and tracking progress was beyond easy!

* Flask + Jinja2, Django
     * The Flask & Jinja technologies used here work together to this web application to happen! The render_template import is crucial for putting all the pieces together and generating a webpage that would be much uglier and difficult to work with without it. Specifically, Flask is a framework for building web apps, while Jinja is a Python web template engine that allowed me to display information in my html file using clear syntax. (I can see Jinja code using "{}" and "%" very clearly in my code editor!)

* The Movie Database API
     * This REST API allowed me to access movie information efficiently. Paired with the web technologies mentioned prior, I was able to display data from the TMDB using a specific API key and the given endpoint. To find my information, I looked through the documentation, played with parameters, and even sifted through raw JSON. Overall, the documentation was fantastically user-friendly and efficient as well!

* MediaWiki Action API
     * In contrast to the TMDB API, Wikipedia's REST API documentation was a bit confusing, but helpful nonetheless. Using the Media Wiki documentation, I was able to access information without a key, rather with a query, and use the TMDB information to gather (in nearly 100% of the testing cases) the correct Wikipedia link for each movie displayed in the web application.
 

* Python Libraries
  * **OS + DotEnv**
  
      These Python modules gave me access to directories necessary for both accessing information and allowing me to keep it private in the appropriate times. For example, I was able to access my TMDB API key without risking any breaches using the os.getenv() function (reading the key-value contained in .env), a crucial part of gathering information.
      
  * **Requests**
  
      An HTTP library, requests was imported to my Python files and utilized for extracting JSON data from both APIs in order to return it to the app.py program. Without this library, it would have been much more tedious to complete this feat. I used requests.get() to extract a response from the APIs containing all information necessary to make this web app functional!
      
  * **Random**
  
      This library was a huge help in making the web app dynamic. Utilizing the random library was easy, in the sense that I called a simple function, random.randint(), not only to generate 5000 movie IDs, but to randomly select one of these IDs so that the user could view a different movie per every refresh.
      
  * **Flask-Login & UserMixin**
  
       Using flask's login libraries was such a breeze. After installing the necessary information, I simply needed to import the modules and include my user model, then I was already on my way to creating successful user functionality. From flask-login, I imported LoginManager, login_required, login_user, logout_user, and current_user. Using these tools, I was able to initialize login_manager and create the user loader to access important user information. On top of that, UserMixin allowed authentications to be made so that user information is checked each time a login occurs.
  
       
* **React**
  
     A JavaScript library, Meta's React implementation in this project allowed the user's rating page to come to life. I was able to display movie rating information using Hooks API (useState, useEffect, etc.) in an orderly fashion with a Review component, which had review props for the movie, rating, and title.
       
* **JavaScript, Fetch API & Flask-JSON**
  
     In addition to the previous APIs and web app tools used for sending and receiving information, JavaScript's Fetch API made the latest additions to the Movie Discovery app possible. Making server requests with Fetch and Flask's JSON library allowed me to implement the user ratings page in React in a way that doesn't just display information, but communicate it to different parts of the program as well. It is important to note that useEffect() is vital part of the JavaScript API functionality and should not be removed.

## Cloning the Repository
   In order to access the data in this repository, one must first fork and clone it to obtain a personal copy. To fork it directly on GitHub, 
one can click the gray "Fork" button in the top right of the repository's page. To access and push files directly from a remote machine, one must
then clone the forked repository. There are various ways to do it: from a terminal, a code editor (like VSCode), an application (like Git Bash), and 
other methods. To clone this repository to a local machine, click the green "Code" button and select the appropriate URL/CLI option (note that this
depends on what you are using to clone the repository). Using this URL, there will be a command necessary to properly complete the cloning process.

   To give a detailed example, here is a step-by-step guide on how to clone a repository using the Windows terminal:

1. Fork the repository on GitHub.
2. Open Windows Command Prompt.
3. Go to the desired location/folder for the remote repository.
4. Click the green "Code" button, copy the HTTPS URL. 
5. Use the command "git clone <HTTPS_URL>" where <HTTPS_URL> is replaced by the URL copied from GitHub.
6. All done! The repository should be in the location it was cloned to.

## Additional Set-Up Steps
#### Accessing the APIs & handling keys:
   Congratulations on cloning the repository! In addition to having the files already present, in order to run the app, one must have their own key to access the TMDB API. For this, one can request a key at [the TMDB API documentation website](https://www.themoviedb.org/).

   After obtaining this key, one must create an .env file containing that key. In the .env file, name the key "KEY", as that will match up with the code provided. (Note: double check that this file has no extension, like the .gitignore file, and that .env is listed in the .gitignore file!)
   
   Another API necessary to display particular information in the app is the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Tutorial). This website contains various documentation tools, and, while it does not require authentication, it's helpful to know where the documentation in this app can be found.
   
#### Implementing a Secret Key
   To use sessions from the flask-login library, you must have a secret key variable. To create a personal secret key, run python -c 'import secrets; print(secrets.token_hex())' and copy the value. 
   To securely store this key, ensure that you place it in the .env file and name it "SECRET", as it will match up with the code present in this repo, similar to how the API key is stored & called.


#### Setting up a Database with WSL:
Update - sudo apt update

Postgresql:
Install - sudo apt install postgresql
Run Prompt - sudo -u postgres psql

Install Psycopg2 - pip install psycopg2-binary

Install Flask-SQLAlchemy - pip install Flask-SQLAlchemy==2.1

Install Flask-login - pip install flask-login


##### Heroku Database Setup
1. Create database
   * Login - heroku login -i
   * Create Heroku app - heroku create
   * Create remote database for Heroku app - heroku addons:create heroku-postgresql:hobby-dev -a {name-of-your-app}
   * Access config variables - heroku config
   * Copy the DATABASE_URL, add it to the .env file, but change 'postgres:' to 'postgresql:':
     DATABASE_URL = "{your_url}" (DATABASE_URL is the name, {your_url} is the copied value from the terminal; do this similarly to your keys as explained previously.)

2. Accessing Database (in the terminal)
   * Basic access - heroku pg:psql
   * Finding tables - \d
   * [Other documentation for specific commands](https://www.postgresql.org/docs/current/tutorial-sql.html)

##### React App Setup
1. Installations
   * Update - sudo apt update
   * Npm - sudo apt install npm
   * App creation tool - npx create-react-app my-first-app 
   * Note: This project was completed using starter code, not the initial code given by creating a default React app.
   (For reference of starter code: https://github.com/csc4350-sp22/p1m3-starter-code)
2. Error-handling/Node versions
   * sudo npm install -g n
   * sudo n latest
For a more specific walkthrough, follow this guide: https://docs.microsoft.com/en-us/windows/dev-environment/javascript/react-on-wsl
 

   
## How to Run the Project Locally
In order to run the app locally, be sure to run npm run build when App.js changes are made. One is then able to run the file by right clicking and pressing run or manually in the terminal using "python3 app.py". This should prompt a link with a url, which one can click to see the project in the browser.
