# My Portofolio Page Source Code

Here this repository will store the source code of my presonal portofolio page.

## Notes for making a new blog post

1. Create an markdown file in `collections/_posts` directory.
2. Put images in `gen/blog/{DATE}` directory and run `convert_images.py` (Press F5) to generate `.webp` images.
3. Write the content.
4. Use GitHub copilot chat to generate English description.
5. Make a PR to build the page to track the modification.
6. Merge the PR to reflect the modification.

Template of a new page will be:
````
---
layout: post
title: "Migrated from my previous blog!"
date: 2022-02-13T09:49:03Z
authors: ["Kazuyuki Arimatsu"]
categories: ["Robotics", "Keyboard"]
description: My blog was migrated from the previous website hosted on blogger. Although I did not frequently post to the previous page recently, I would make a new post here if I had a chance.
thumbnail: "/assets/images/gen/blog/2022-02-13/blog-18-thumbnail.webp"
image: "/assets/images/gen/blog/2022-02-13/blog-18.webp"
comments: false
subscribe: true
---

figure

{% include framework/shortcodes/figure.html src="/assets/images/gen/content/content-1.webp" title="Steve Francia" caption="Designing in Figma" alt="Photo of designing a website in Figma" link="https://figma.com" target="\_blank" %}

image

![Design In Figma]({{ "/assets/images/gen/content/content-2.webp" | relative_url }})

```js
$(window).scroll(function () {
  // this will work when your window scrolled.
  var scroll = $(window).scrollTop();
  if (scroll > 100) {
    $(".header").addClass("header-scrolled");
  } else {
    $(".header").removeClass("header-scrolled");
  }
});
```

Gruber avoided using curly braces in Markdown to unofficially reserve them for implementation-specific extensions. Markdown Extra adds the following features to Markdown:

- markdown markup inside HTML blocks
- elements with id/class attribute
- fenced code blocks that span multiple lines of code
- tables
- definition lists
- footnotes
- abbreviations
````

## Useful Information from the original README of the theme

Jekyll Curate is a premium portfolio theme for Jekyll.

### Documentation

* Live Docs: https://www.zerostatic.io/docs/jekyll-curate
* Demo: https://jekyll-curate.netlify.app/

### Screenshot

![Jekyll Curate Theme screenshot](https://www.zerostatic.io/theme/jekyll-curate/jekyll-curate-screenshot.png)

### Install

#### Install Jekll

Make sure you have Ruby & Jekyll installed - For a step-by-step guide, read Jekyll docs [installation](https://jekyllrb.com/docs/installation/)

#### Install Theme

Extract the theme .zip file to your local computer. Navigate to the project root (it contains the README.md)

Run `bundle install` to install gems.

Then run `bundle exec jekyll serve` to start the Jekyll local development server.

To build the Jekyll site run `bundle exec jekyll build`

### Deploy

#### Netlify

This theme comes with a working `netlify.toml` which will pre-configure your Netlify deployment for Jekyll. The Netlify docs have a great guide to [creating a site with Netlify](https://docs.netlify.com/site-deploys/create-deploys/).

> 💡 If you experience bundle install issues during the Netlify deployment, deleting the Gemfile.lock can sometimes help

#### GitHub Pages

This theme is tested to work on Github Pages. Jekyll has a [guide to deploying on Github pages](https://jekyllrb.com/docs/github-pages/).

If you are creating a GitHub Pages "Project site" then your site will be in a sub-folder with a url like `http://username.github.io/repository`. You will need to update the `baseurl` and `url` in the `_config.yml` for the asset paths to work correctly.

### Credits

This theme uses open-source libraries and assets.

- **Bootstrap 5.3.2** https://unsplash.com/license
- **Font Awesome 6 Free:** https://fontawesome.com/
- **Unsplash Images** https://unsplash.com/
