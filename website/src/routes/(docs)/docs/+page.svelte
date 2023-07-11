<script lang="ts">
	import { base } from '$app/paths';
	import Docs from '$lib/Components/Docs/Docs.svelte';
	import { introduction } from '$lib/Content/introduction';
	import { dataUrl, current_title } from '$lib/stores';
	import { onMount } from 'svelte';

	let data: any;
	$: {
		fetch(base + '/Content/' + $dataUrl).then(async (res) => {
			data = await res.text();
		});
	}
</script>

<svelte:head>
	<title>{$current_title} | Django docme Docs</title>
</svelte:head>

<Docs {data} />
