<script lang="ts">
	import { current_page, current_header, current_title, title } from '$lib/stores';

	export let navUrls: any;
	$: current_query = $current_page;

	$: classesActive = (slug: string) => (slug === current_query ? '!bg-primary-500' : '');
</script>

<section class="flex h-full flex-row">
	<nav class="list-nav hidden px-4 lg:flex lg:flex-col w-96">
		{#each navUrls as navUrl}
			<h1 class="h3 font-bold px-4 my-4">{navUrl.title}</h1>
			<ul class="w-full my-2">
				{#each navUrl.posts as post}
					<li>
						<button
							on:click={() => {
								$current_page = post.slug;
								$title = `${post.header} | Skeleton UI`;
								$current_header = navUrl.title;
								$current_title = post.header;
							}}
							class="btn w-full items-start {classesActive(post.slug)}"
						>
							<span class="flex-auto">{post.header}</span>
						</button>
					</li>
				{/each}
			</ul>
			<hr />
		{/each}
		<!-- <pre class="">
				{JSON.stringify(navUrls, null, 2)}
			</pre> -->
	</nav>
	<span class="divider-vertical h-full" />
</section>
