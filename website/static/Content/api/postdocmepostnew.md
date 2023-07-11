# /docme

<hr/>

# 1- Request :  

### POST request to `/docme/posts/new` route .

this endpoint  Create  related  to a already existing post group.<br/>

## request body : 

```json
    {
        "header": "header 1",
        "body": "# Something",
        "group":"post group title"
    }
```
**group** it's the group title this post related to .
**slug** propretie is set automaticly by slugify the header .


and return this **response :**

```json
    {
        "id": 'id',
        "posts": [
            {
                "header": "header",
                "body": "# Something",
                "slug": "some-slug"
            },
        ],
        "title": "title"
    }
```
<hr/>

# 2- Reponse Types : 

## 1. Post Group :
- `id (number) : The id of Post Group .`
- `title (string) : The title of Post Group .`
- `posts (list): List of the post related to this Post Group .`
## 2. Post : 
- `header (string): The Title of the post .`
- `body (string of Markdown) : The Body of the post it's written and proccessed as markdown .`
- `slug (string) :  a unique slug for the post .`
