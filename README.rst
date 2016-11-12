================
Coding Portfolio
================
A Django webapp for settings up your coding portoflio.

What's new?
-----------

- New project fields - Platform and Website
- A new project summary display
- Support for vector images (SVGs)
- Expanded the scope of search keywords
- A more efficient way to manage images/thumbnails

What does this app do?
----------------------
Coding Portfolio is a simple webapp for the Django framework that provides you a ready-made website where you can post your 
projects right from the default Django administration interface.

Features:
---------

- Easy to setup - It should take you only a few minutes to setup your website with this app.
- Clean UI - Coding Portfolio uses Bootstrap & Font-Awesome for it's CSS and Icons.
- Mobile friendly
- Automatic classification of your projects based on the programming language / framework
- Automatic sitemap generator - The sitemap is generated automatically is available at /sitemap.xml
- Easy to use - If you know how to use the Django administration interface this should be a piece of cake.

and more..

Why did you make this app?
--------------------------

Well to put it short - I needed to host a website where I could display my programming projects but I was too broke to afford
a good webhost or a VPS so I went for free webhosts. I setup a WordPress blog ran it for a month but it was not good enough, the
website would go down frequently, slow loading etc. (after all it was a free webhost) So finally I decided to make a web app of my own for this purpose. The idea
was to make something <b>simple</b> and <b>light</b> (I am a lazy person) good enough to use and Coding Portfolio was born.

My website: `Areeb Beigh <http://areeb12.pythonanywhere.com>`_

Setup
-----
Setting up coding portfolio is easy, just download it, put it's contents in your Django website folder (in a folder named ``coding_portfolio``)
and add it to the ``INSTALLED_APPS`` in your website's settings file just like you add any other web app to your website.

Add a url to the ``urlpatterns`` of your Django website and include the ``coding_portfolio.urls`` file.

You will also need to copy the contents of the ``media`` folder to your website's ``MEDIA_ROOT``.

Edit the templates ``layout.html`` and ``index.html`` to change the default text.

Finally in the Django administration interface add some content in the ``Abouts`` model.

You're done!

For reference you can check my `website <https://github.com/areebbeigh/mywebsite>`_ source.

Contributing
------------
Found a bug? typo? error? or do you have a feature that you can implement? Coding Portfolio is my first Django project feel free to use or expand the project! I'll be waiting for your pull requests!

<hr>

| Developer: Areeb Beigh <areebbeigh@gmail.com>
| Version: 1.0
| GitHub Repo: https://github.com/areebbeigh/coding-portfolio
