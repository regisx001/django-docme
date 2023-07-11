# /docme/{slug}/

`{slug} : string params` 
<hr/>

# 1- Request :  

### GET request to `/docme/{slug}/` route .

this endpoint get a specific post using the params slug .<br/>


and return this **response :**

```json

{
    "header": "header example",
    "body": "# this is the body",
    "slug": "some-slug"
}
```
<hr/>

# 2- Reponse Types : 

## 1. Post : 
- `header (string): The Title of the post .`
- `body (string of Markdown) : The Body of the post it's written and proccessed as markdown .`
- `slug (string) :  a unique slug for the post .`
