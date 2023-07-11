<script lang="ts">
	import { base } from '$app/paths';
	import Docs from '$lib/Components/Docs/Docs.svelte';
	import { dataUrl, current_title } from '$lib/stores';
	// import { onMount } from 'svelte';

	$: loading = false;
	let data: any;
	$: {
		fetch(base + '/Content/' + $dataUrl).then(async (res) => {
			loading = true;
			data = await res.text();
			loading = false;
		});
	}
</script>

<svelte:head>
	<title>{$current_title} | Django docme Docs</title>
</svelte:head>

<!-- {loading} -->

{#if !loading}
	<Docs {data} />
{/if}
