# Coding Portfolio
A <a href="https://www.djangoproject.com/">Django</a> webapp for those programmers who are lazy to do too much to setup a website for their projects.

## What does this app do?
Coding Portfolio is a simple webapp for the Django framework that provides you a ready-made website where you can post your 
projects right from the default Django administration interface.

### Features:
<ul>
  <li>Easy to setup - It should take you only a few minutes to setup your website with this app.</li>
  <li>Clean UI - Coding Portfolio uses Bootstrap & Font-Awesome for it's CSS and Icons.</li>
  <li>Mobile friendly</li>
  <li>Automatic classification of your projects based on the programming language / framework</li>
  <li>Automatic sitemap generator - The sitemap is generated automatically is available at /sitemap.xml</li>
  <li>Easy to use - If you know how to use the Django administration interface this should be a piece of cake.</li>
</ul>
and more..

## Why did you make this app?
Well to put it short - I needed to host a website where I could display my programming projects but I was too broke to afford
a good webhost or a VPS so I went for free webhosts. I setup a WordPress blog ran it for a month but it was not good enough, the
website would go down frequently, slow loading etc. So finally I decided to make a web app of my own for this purpose. The idea
was to make something <b>simple</b> (I am a lazy person) good enough to use and Coding Portfolio was born.

My website: areeb12.pythonanywhere.com

## Working
The working is straight forward, each project has a non-nullable title, description and language field and an option thumbnail
image field. As you post new projects and add new languages to the Language model the "Projects" dropdown menu gets updated
automatically and your projects are categorized based on the project's language field.

Like I said, Coding Portfolio is a simple web app for lazy programmers like me.

## Setup
Setting up coding portfolio is easy, just download it, put it's contents in your Django website folder (in a folder named `coding_portfolio`)
and add it on `INSTALLED_APP` in your website's settings file just like you add any other web app to your website.

Add a url to the `urlpatterns` of your Django website and include the `coding_portfolio.urls` file.

You will also need to copy the contents of the `media` folder to your website's `MEDIA_ROOT`.

Edit the templates `layout.html` and `index.html` (you can edit others as well) as you like.

Finally in the Django administration interface add some content in the `Abouts` model.

You're done!

For reference you can check my website: https://github.com/areebbeigh/mywebsite - www.areebbeigh.tk

## Contributing
Found a bug? typo? error? or do you have a feature that you can implement? Coding Portfolio is my first Django project and
still under development feel free to contribute to the project!

<hr>

Developer: Areeb Beigh <areebbeigh@gmail.com> <br>
Version: 1.0 <br>
GitHub Repo: https://github.com/areebbeigh/coding-portfolio <br>
