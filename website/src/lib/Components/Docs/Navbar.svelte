<script lang="ts">
	import { base } from '$app/paths';
	import { AppBar, LightSwitch, popup, type PopupSettings } from '@skeletonlabs/skeleton';
	import { drawerStore } from '@skeletonlabs/skeleton';
	import type { DrawerSettings } from '@skeletonlabs/skeleton';

	import GithubIcon from '$lib/Icons/github_icon.svelte';
	import DotsIcon from '$lib/Icons/dots_icon.svelte';

	export let version: string = '';

	const settings: DrawerSettings = { id: 'nav', width: 'w-96' };
	const popupCombobox: PopupSettings = {
		event: 'focus-click',
		target: 'popupCombobox',
		placement: 'bottom',
		closeQuery: '.listbox-item'
	};
</script>

<AppBar>
	<svelte:fragment slot="lead">
		<div class="flex lg:hidden mr-2">
			<button
				on:click={() => {
					drawerStore.open(settings);
				}}
				class="mr-2 btn m-0 p-0"
			>
				<i class="ti ti-menu-2 text-3xl" />
			</button>
		</div>
		<a href="{base}/">
			<div class="text-2xl font-extrabold">
				<span>Django</span>
				<span class="text-primary-700">Docme</span>
			</div>
		</a>
	</svelte:fragment>
	<svelte:fragment slot="trail">
		<div class="hidden md:flex flex-row justify-center items-center">
			<a class="btn hover:variant-ghost-primary font-semibold" href="{base}/docs"> Docs </a>
			<a class="btn hover:variant-ghost-primary font-semibold" href="{base}/"> About </a>
			<span class="mx-2 text-sm text-gray-500">Version {version}</span>
			<a
				class="btn-icon hover:variant-ghost-primary"
				target="_blank"
				href="https://github.com/zarqizoubir/django-docme"
			>
				<GithubIcon />
			</a>
		</div>
		<div class="md:hidden" use:popup={popupCombobox}>
			<button class="btn-icon hover:variant-ghost-primary">
				<DotsIcon />
			</button>
			<nav class="list-nav card shadow-xl p-4 w-44" data-popup="popupCombobox">
				<ul>
					<li>
						<a class="btn hover:variant-ghost-primary font-semibold" href="{base}/docs"> Docs </a>
					</li>
					<li>
						<a class="btn hover:variant-ghost-primary font-semibold" href="{base}/"> About </a>
					</li>
					<li>
						<a
							class="btn hover:variant-ghost-primary font-semibold"
							target="_blank"
							href="https://github.com/zarqizoubir/django-docme"
						>
							github
						</a>
					</li>
					<li class="text-center">
						<span class="text-sm text-gray-500">Version {version}</span>
					</li>
				</ul>
				<div class="arrow bg-surface-100-800-token" />
			</nav>
		</div>
		<LightSwitch />
	</svelte:fragment>
</AppBar>
