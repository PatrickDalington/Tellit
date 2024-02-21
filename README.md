# Tellit
‘Tellit’ presents a solo project that aims to connect movie producers, content creators, and more with a diverse array of stories for use in films, skits, and other creative projects.

This app offers a win-win scenario, facilitating writers in earning recognition and revenue while offering content creators and filmmakers a hassle-free avenue to source compelling stories. 💰📝
As earlier stated, it’s a solo project, and it was a great and exhilarating ride working on this, but in future versions, I hope to take on team members so we could together take the writing community by storm!
Here is the story behind how I came up with Tellit
If you believe I created this because of my love for writing, you’re mistaken 😂. I have a confession to make.😱Writing is not something I particularly enjoy; I find it exhausting. 😅 So, why then did I dedicate this entire project to writers?

It all goes back to my younger sister, who is a writer extraordinaire. ✍️🌺 I’d venture to say she was born with a pen in her hand. 🖊️👶 Whenever I lacked the motivation to put words on the page, she would weave her magic with her pen and come to my rescue.
I’ve witnessed her evolution from a budding writer to someone who can not only assist her older brother but also captivate readers worldwide. 🌍
This personal journey has left a lasting impact on me, prompting me to embark on this endeavor. Writing may tire me out, but coding ignites my passion.
Thus, the idea struck me — why not craft codes to support individuals like her in their writing pursuits? ☺️✨Why not WRITE codes to help people like her WRITE? 🤷‍♂️📝




* Tellit landing page: https://tellit-landing-page.netlify.app
* Tellit web page: https://tellit-page.netlify.app
* Tellit Blog post: https://medium.com/@patrickdalington11/love-what-you-do-here-is-the-history-of-how-tellit-came-about-ea4ea54f8cc4
* LinkedIn Page: https://www.linkedin.com/in/patrick-olumba/



## Table of Content
* [Installation](#installation)
* [Contribution](#contribution)
* [Usage](#usage)
* [Related Project](#related-project)
* [Authors](#authors)
* [License](#license)


## Installation
* Clone this repository: `git clone "https://github.com/PatrickDalington/Tellit.git"`
* Access Tellit directory: `cd Tellit`
* Run virtual env: `auth/bin/activate`
* Run export project: `export FLASK_APP=project`
* Run project: `flask run`

## Contribution
`This project is a solo project`

## Usage
```
Navigating through the web app is simple.

The home tab: This shows all the stories, movie scripts, skit script, popular users and others.

Add tab: This page is for creating new stories, movie scripts or skit script.

Signup tab: This page is for creating a new account.

Login tab: This page is for login user into the web app.

```

## Related projects
----




## Challenges
In the third week of my project, one morning, I encountered an unexpected issue while working on my app, Tellit. After starting my usual routine, I noticed some conflicts arose as I attempted to add more stories to enhance the 360 3D animation.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1eWndSH1gzBU8VzDPoK3kA.png)



Upon days of debugging, I discovered the root cause: I had made changes to the database using DB Browser for SQLite without saving them, which disrupted the application’s flow, leading to a system error.
For those unfamiliar, DB Browser for SQLite is a visual tool used for managing SQLite databases, offering a convenient way to create, edit, and analyze SQLite files.



![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jsfViWGTaVNB8O8_GvZLiQ.gif)



Now, let’s talk about how I resolved this error. Over time, I’ve developed the habit of leaving my computer running after work. In this instance, I had made changes to the database using DB Browser but failed to save and close the software. When I attempted to create a new story, conflicts arose because the database file was still open for editing in DB Browser, confusing the Python compiler.
To simplify this scenario for non-technical folks, imagine going to the doctor’s office and asking the nurse if you can see the doctor, only to be told that someone is currently in the room. If you were to walk in regardless, you might be startled to find the doctor examining a patient. Similarly, attempting to add new data to the database while DB Browser is unsaved and open is like trying to enter the doctor’s office while it’s already occupied.
However, by saving the changes made in DB Browser and closing the software, I was able to resolve the issue. Although it took me three days to pinpoint the cause of the problem, my determination to understand and resolve it kept me focused throughout the process.



![](https://miro.medium.com/v2/resize:fit:960/format:webp/1*hQYj5lcOxouYuVwgvb4jzw.gif)



I have learnt to make sure I save all pending database queries before adding more to it.
I think I need to also change the habit of only hibernating my computer but making sure that all pending job completed before shutting down.


This whole project has thought me the power of Flask and here are the few things I learnt so far.

* Working with server and client side in one project.
* Connecting mySQLite database to Flask project.
* Opportunity to dig down more into python virtual environment.
* Integrating python libraries.


Some developers might wonder why I chose Flask over Django 😊

The reason for this is because Flask allows developers to have more control over their codebase and project structure, as it does not enforce strict conventions or include unnecessary features.

Another reason is because this project is not an heavyweight app. Flask lightweight nature also means faster startup times and lower resource consumption compared to Django, making it a preferable choice for projects with limited hardware resources or those requiring high performance.



## License
All Right Reserved © 2024


## Authors
Patrick Olumba - [Github](https://github.com/PatrickDalington) / [LinkedIn](https://www.linkedin.com/in/patrick-olumba)  

