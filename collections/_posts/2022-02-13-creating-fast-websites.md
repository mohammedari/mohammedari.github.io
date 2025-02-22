---
layout: post
title: "Placeholder Post"
date: 2022-02-13T09:49:03Z
authors: ["Mike Vance"]
categories: ["Robotics", "Keyboard"]
description: Please be patient until a post is created soon...
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
