<script lang="ts">
	import Code from '$lib/Code.svelte';
	import { current_title, current_header } from '$lib/stores';
	import SvelteMarkdown from 'svelte-markdown';
	export let data: any = '# This is Just for test';
</script>

<article class="mx-[10%] mt-5 mb-10 prose dark:prose-invert max-w-full">
	<ol class="breadcrumb">
		<li class="crumb"><span class="underline text-primary-500">{$current_header}</span></li>
		<li class="crumb-separator" aria-hidden>&rsaquo;</li>
		<li>{$current_title}</li>
	</ol>

	<SvelteMarkdown
		source={data}
		renderers={{
			code: Code
		}}
	/>
</article>
