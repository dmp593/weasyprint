# WeasyPrint Service Docker Image
WebServer for WeasyPrint with FastAPI.

## Endpoints
* GET `/health` -- returns a JSON response ```{ "healthy": true }```
* POST `/pdf` or `/pdf?filename=xyz.pdf` -- (with a html body of Content-type of `text/html`) returns a PDF response.
If no filename is specified, `document.pdf` will be the default Content-Disposition filename.

### If you want to change the Page Size and/or Orientation, just add a style to change the page (media query)
For example:

```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>@page { size: A1 landscape; }</style>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

Will render a page with A1 size and with landscape orientation with the text "Hello, World".