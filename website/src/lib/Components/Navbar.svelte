<script lang="ts">
	import { AppBar, LightSwitch } from '@skeletonlabs/skeleton';
	import { drawerStore } from '@skeletonlabs/skeleton';
	import type { DrawerSettings } from '@skeletonlabs/skeleton';

	const settings: DrawerSettings = { id: 'nav', width: 'w-96' };
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
		<h2 class="h2 font-semibold">
			<span class="text-primary-700 font-black">DRF</span>
			Docs
		</h2>
	</svelte:fragment>

	<div class="hidden lg:flex justify-center items-center gap-2">
		<input placeholder="Search ... " class="input max-w-md rounded" type="text" />
		<button class="btn rounded variant-filled-primary">Search</button>
	</div>
	<svelte:fragment slot="trail">
		<LightSwitch />
	</svelte:fragment>
</AppBar>
