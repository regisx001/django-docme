import { writable, type Writable } from "svelte/store";

type DocsSettings = {
    theme: string
}

export let title: Writable<string> = writable("API Docs | Skeleton UI")

export let current_page: Writable<string> = writable("introduction")



export let current_header: Writable<string> = writable("Introduction")
export let current_title: Writable<string> = writable("Introduction")


export let docsSettings: Writable<DocsSettings> = writable({ theme: "skeleton" })