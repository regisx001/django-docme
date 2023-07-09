export const DocsUrl = 'http://127.0.0.1:8000/docme/';



export async function getReleases(token: string) {
    let data = await (
        await fetch('https://api.github.com/repos/zarqizoubir/django-docme/releases/latest', {
            headers: {
                Accept: 'application/vnd.github+json',
                Authorization: `Bearer ${token}`,
                'X-GitHub-Api-Version': '2022-11-28'
            }
        })
    ).json();

    return data;
}