# Wagtail + Vue.js

__        __          _        _ _          __     __             _
\ \      / /_ _  __ _| |_ __ _(_) |    _    \ \   / /   _  ___   (_)___
 \ \ /\ / / _` |/ _` | __/ _` | | |  _| |_   \ \ / / | | |/ _ \  | / __|
  \ V  V / (_| | (_| | || (_| | | | |_   _|   \ V /| |_| |  __/_ | \__ \
   \_/\_/ \__,_|\__, |\__\__,_|_|_|   |_|      \_/  \__,_|\___(_)/ |___/
                |___/                                          |__/

Using Vue.js with Wagtail as a headless CMS.

# What's in this talk?

- Routing for Wagtail
- Rendering Wagtail page content
- Simple page navigation

# Routing for Wagtail

____             _   _                __
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
Upon mounting our app we make a request to the Wagtail API's "find" method and pass in the URL the user requested.

    ```
    GET /api/v2/pages/find/?html_path=/
    ```

##
If Wagtail can resolve this path to an existing page than it will return a `302` redirect response to the page's detail view which in turn returns the JSON data.

    ```
    GET /api/v2/pages/find/?html_path=/ => 302
    GET /api/v2/pages/3/ => 200 JSON data
    ```

##
Right in the returned JSON data we'll find the `meta.type` key which we use to determine which component to render.

    ```
    meta: {
      type: pages.HomePage
    }
    ```

##
If Wagtail cannot resolve the URL it will return a `404` not found response and we render a "Not Found" component to inform the user.

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
Inside of StreamField blocks Wagtail usually only stores the IDs for images, document, or other pages. It's best to make a dedicated component for each of these to abstract the API logic of fetching the full details.

    ```
    Pages /api/v2/pages/<id>/
    Images /api/v2/images/<id>/
    Documents /api/v2/documents/<id>/
    ```

##
StreamField blocks can also be nested so we need a reliable way to pass data down the component tree.

# Simple page navigation


