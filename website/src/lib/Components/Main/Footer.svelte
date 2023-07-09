<script lang="ts">
	import { onMount } from 'svelte';
	export let version: string;
	$: is_ready = false;
	onMount(async () => {
		is_ready = true;
	});
</script>

<section class="w-full h-16 flex flex-row bg-surface-800">
	{#if is_ready}
		<div class="flex justify-center items-center h-full w-full">Version {version}</div>
	{/if}
	<div class="w-full" />
</section>

<!-- <pre class="pre">
	{JSON.stringify(version, null, 2)}
</pre> -->
