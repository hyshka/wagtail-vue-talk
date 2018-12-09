# Wagtail + Vue.js

__        __          _        _ _          __     __             _
\ \      / /_ _  __ _| |_ __ _(_) |    _    \ \   / /   _  ___   (_)___
 \ \ /\ / / _` |/ _` | __/ _` | | |  _| |_   \ \ / / | | |/ _ \  | / __|
  \ V  V / (_| | (_| | || (_| | | | |_   _|   \ V /| |_| |  __/_ | \__ \
   \_/\_/ \__,_|\__, |\__\__,_|_|_|   |_|      \_/  \__,_|\___(_)/ |___/
                |___/                                          |__/

Using Wagtail as a headless CMS.

- Routing
- Rendering page content
- Simple page navigation

# Routing for Wagtail

_____             _   _                __
|  _ \ ___  _   _| |_(_)_ __   __ _   / _| ___  _ __
| |_) / _ \| | | | __| | '_ \ / _` | | |_ / _ \| '__|
|  _ < (_) | |_| | |_| | | | | (_| | |  _| (_) | |
|_| \_\___/ \__,_|\__|_|_| |_|\__, | |_|  \___/|_|
                              |___/
__        __          _        _ _
\ \      / /_ _  __ _| |_ __ _(_) |
 \ \ /\ / / _` |/ _` | __/ _` | | |
  \ V  V / (_| | (_| | || (_| | | |
   \_/\_/ \__,_|\__, |\__\__,_|_|_|
                |___/

##

In Wagtail each type of page will have it's own model since they may have different types of content. This makes it easy for us to render a different component for each page type.

    ```
    class HomePage(Page):
        """A home page class."""
        ...fields for page content...
    ```

##

When a user navigates to a page we make a request to the Wagtail API's "find" method and pass in the URL the user requested.

If Wagtail can resolve this path to an existing page than it will return a `302` redirect response to the page's detail view which in turn returns the JSON data.

    ```
    User requests "http://localhost:8080/"

    GET /api/v2/pages/find/?html_path=/ => 302
    GET /api/v2/pages/3/ => 200 JSON data
    ```

TODO: Show example of page response: http://localhost:8000/api/v2/pages/3/?format=json

Right in the returned JSON data we'll find the `meta.type` key which we use to determine which component to render.

##

If Wagtail cannot resolve the URL it will return a `404` not found response and we can inform the user.

    ```
    GET /api/v2/pages/find/?html_path=/wp-login.php => 404 Not Found message
    ```

# Rendering Wagtail page content

____                _           _
|  _ \ ___ _ __   __| | ___ _ __(_)_ __   __ _
| |_) / _ \ '_ \ / _` |/ _ \ '__| | '_ \ / _` |
|  _ <  __/ | | | (_| |  __/ |  | | | | | (_| |
|_| \_\___|_| |_|\__,_|\___|_|  |_|_| |_|\__, |
                                         |___/
__        __          _        _ _
\ \      / /_ _  __ _| |_ __ _(_) |  _ __   __ _  __ _  ___
 \ \ /\ / / _` |/ _` | __/ _` | | | | '_ \ / _` |/ _` |/ _ \
  \ V  V / (_| | (_| | || (_| | | | | |_) | (_| | (_| |  __/
   \_/\_/ \__,_|\__, |\__\__,_|_|_| | .__/ \__,_|\__, |\___|
                |___/               |_|          |___/
                 _             _
  ___ ___  _ __ | |_ ___ _ __ | |_
 / __/ _ \| '_ \| __/ _ \ '_ \| __|
| (_| (_) | | | | ||  __/ | | | |_
 \___\___/|_| |_|\__\___|_| |_|\__|

##

Along with the typical methods of managing page content, Wagtail has a unique concept called "StreamField" which allows the user to intersperse different types of content, usually referred to as "blocks", which can be repeated and arranged in any order.

TODO: Show example of Wagtail StreamField content: http://localhost:8000/api/v2/pages/3/?format=json

##

These StreamField blocks can at times be tricky to work with through the API. Since they are so flexible they are commonly used in many different ways and this can cause the same block to end up outputting data differently. At times we need to add extra logic to our components to work around this.

    ```
    # ButtonBlock used inside of a "StreamBlock"
    {
        "id": "23960469-af52-41dd-a9fe-3f9bbb9593e5",
        "value": {
            "document": null,
            "text": "External link",
            "external_link": "https://www.duckduckgo.com/",
            "page": null
        },
        "type": "ButtonBlock"
    }

    # The same ButtonBlock used inside of a "ListBlock"
    {
        "document": null,
        "text": "Page link",
        "external_link": "",
        "page": 4
    }
    ```

##

Inside of StreamField blocks Wagtail usually only stores the IDs for images, documents, or other pages. It's best to make a dedicated component for each of these to abstract the API logic of fetching the full details.

    ```
    # Wagtail Endpoints
    Pages: /api/v2/pages/<id>/
    Images: /api/v2/images/<id>/
    Documents: /api/v2/documents/<id>/

    # WagtailPage component
    - Fetch a Wagtail page with the ID passed into our component.
    - Get the page's path from the "meta.html_url" property and anything else we want from the response.
    - Render a link with the path.
    ```

##

Which StreamField blocks are available can differ between page types and they can be nested inside of one another so we need a reliable way to pass data down the component tree.

Again, we chose to abstract this out into a separate component which accepts any type of StreamField block and renders the specific component we've made for that block type. This allows us to loop through the StreamField content on any page or nested StreamField content inside of a StreamField block.

    ```
    # HomePage component
    - Loop through blocks in content field.
    - For each block pass block data to StreamField component.

    # StreamField component
    - Register all available StreamField block components.
    - Render StreamField block component matching the current block's "type" property.

    # StreamField block component
    - This is where all your code for a specific StreamField block will go. Templating, styles, extra scripting, etc.
    - If you're using nested StreamFields you can re-use that component here and even re-use other StreamField block components entirely.
    ```

# Simple page navigation

 ____  _                 _
/ ___|(_)_ __ ___  _ __ | | ___   _ __   __ _  __ _  ___
\___ \| | '_ ` _ \| '_ \| |/ _ \ | '_ \ / _` |/ _` |/ _ \
 ___) | | | | | | | |_) | |  __/ | |_) | (_| | (_| |  __/
|____/|_|_| |_| |_| .__/|_|\___| | .__/ \__,_|\__, |\___|
                  |_|            |_|          |___/
                   _             _   _
 _ __   __ ___   _(_) __ _  __ _| |_(_) ___  _ __
| '_ \ / _` \ \ / / |/ _` |/ _` | __| |/ _ \| '_ \
| | | | (_| |\ V /| | (_| | (_| | |_| | (_) | | | |
|_| |_|\__,_| \_/ |_|\__, |\__,_|\__|_|\___/|_| |_|
                     |___/

...or: How I Learned to Stop Worrying and Love the API

## Specifying fields

The first thing I'll show you is how to restrict which fields the Wagtail API returns when making a request. If we're just building a menu we don't need the page content bloating our requests.

    ```
    GET /api/v2/pages/?fields=_,html_url,title
    ```

This request will return a list of all pages on the site with only the `html_url` and `title` for each. The `_` here is a special character and tells the Wagtail API to hide all fields by default, this gives us a clean slate to start with.

## Limiting

If we got a thousand pages on the site we don't want all of those showing up in the menu. You can quickly limit the number of returned pages by tacking on the `limit` query parameter.

    ```
    GET /api/v2/pages/?fields=_,html_url,title&limit=5
    ```

## Filtering

We're getting close now, but what if we want more control over what pages are in the menu? By default Wagtail pages have a boolean field called `show_in_menus`. We might as well use that and the Wagtail API makes this easy for us, simple add the field as a query parameter and assign the value we need.

    ```
    GET /api/v2/pages/?fields=_,html_url,title&limit=5?show_in_menus=true
    ```

## I want more...

This is all we need for our purposes right now but with the Wagtail API you can do a lot more out of the box which can also be useful, just to name a few:

- Pagination
- Ordering
- Filtering (field, page type, tree position, etc.)
- Search

For details on these, and more, check out the docs: https://docs.wagtail.io/en/latest/advanced_topics/api/v2/usage.html
