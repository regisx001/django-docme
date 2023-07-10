<script lang="ts">
	import Navigation from '$lib/Components/Docs/Navigation.svelte';
	import Navbar from '$lib/Components/Docs/Navbar.svelte';
	import { AppShell, Drawer, drawerStore } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';

	$: is_ready = false;
	onMount(async () => {
		is_ready = true;
	});

	const navUrls = [
		{
			title: 'Introduction',
			posts: [
				{ header: 'Introduction', slug: 'introduction', body: 'introduction/introduction.md' },
				{ header: 'Get Started', slug: 'get-started', body: 'introduction/get-started.md' }
			]
		}
	];
	// const navUrls = [
	// 	{
	// 		title: 'Introduction',
	// 		posts: [
	// 			{
	// 				header: 'Introduction',
	// 				slug: 'introduction',
	// 				file: 'introduction',
	// 				data_url: 'introduction'
	// 			},
	// 			{
	// 				header: 'Get Started',
	// 				slug: 'get-started',
	// 				file: 'introduction',
	// 				data_url: 'get_started'
	// 			}
	// 		]
	// 	}
	// ];
</script>

{#if is_ready}
	<AppShell>
		<svelte:fragment slot="header">
			<Navbar />
		</svelte:fragment>
		<svelte:fragment slot="sidebarLeft">
			<Navigation {navUrls} />
		</svelte:fragment>
		<slot />
	</AppShell>
{/if}
