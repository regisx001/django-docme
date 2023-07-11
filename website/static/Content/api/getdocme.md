# /docme

<hr/>

# 1- Request :  

### GET request to `/docme` route .

this endpoint  list of all created PostGroup with the posts .<br/>


and return this **response :**

```json
[
    {
        "id": 1,
        "posts": [
            {
                "header": "header",
                "body": "# Something",
                "slug": "some-slug"
            },
        ],
        "title": "title"
    },
    {
        "id": 2,
        "posts": [
            {
                "header": "header",
                "body": "# Something",
                "slug": "some-slug"
            },
        ],
        "title": "title"
    }
]
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
