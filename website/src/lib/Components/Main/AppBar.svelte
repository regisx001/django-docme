<script lang="ts">
	import GithubIcon from '$lib/Icons/github_icon.svelte';
	import { base } from '$app/paths';
	import { AppBar } from '@skeletonlabs/skeleton';
</script>

<AppBar>
	<svelte:fragment slot="lead">
		<a href="{base}/">
			<div class="text-2xl font-extrabold">
				<span>Django</span>
				<span class="text-primary-700">Docme</span>
			</div>
		</a>
	</svelte:fragment>
	<svelte:fragment slot="trail">
		<a class="btn hover:variant-ghost-primary font-semibold" href="{base}/"> Docs </a>
		<a class="btn hover:variant-ghost-primary font-semibold" href="{base}/"> About </a>
		<a
			class="btn-icon hover:variant-ghost-primary"
			target="_blank"
			href="https://github.com/zarqizoubir/django-docme"
		>
			<GithubIcon /></a
		>
	</svelte:fragment>
</AppBar>
