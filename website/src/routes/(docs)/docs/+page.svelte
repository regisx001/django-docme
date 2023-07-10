<script lang="ts">
	import Docs from '$lib/Components/Docs/Docs.svelte';
	import { dataUrl, current_title } from '$lib/stores';
	import { onMount } from 'svelte';

	let data: any;
	$: {
		fetch('/Content/' + $dataUrl).then(async (res) => {
			data = await res.text();
		});
	}
</script>

<svelte:head>
	<title>{$current_title} | Django docme Docs</title>
</svelte:head>

<!-- <Docs {data} /> -->

{data}
