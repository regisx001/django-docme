<script lang="ts">
	import { AppShell, Drawer, drawerStore } from '@skeletonlabs/skeleton';
	import Navbar from '$lib/Components/Navbar.svelte';
	import Navigation from '$lib/Components/Navigation.svelte';
	import NavigationDrawer from '$lib/Components/NavigationDrawer.svelte';
	import { onMount } from 'svelte';
	import { DocsUrl } from '$lib/utils';
	import { docsSettings } from '$lib/stores';

	let navUrls: any;
	let is_fetched = false;
	onMount(async () => {
		navUrls = await (await fetch(DocsUrl)).json();
		is_fetched = true;
	});
</script>

{#if is_fetched}
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

<Drawer>
	{#if $drawerStore.id === 'nav'}
		<NavigationDrawer {navUrls} />
	{:else}
		<!--  -->
	{/if}
</Drawer>
