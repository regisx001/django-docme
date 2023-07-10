<script>
	import { base } from '$app/paths';
</script>

<main class="h-full p-4 lg:p-10">
	<div class="relative rounded-xl bg-[url('/bg_home.svg')] bg-cover bg-no-repeat h-full">
		<div
			class="
		card card-hover w-full max-w-xl
		absolute top-[40%] left-[50%] lg:left-[30%] translate-x-[-50%] translate-y-[-50%]
		"
		>
			<header class="card-header m-4">
				<h2 class="h2 text-center font-extrabold">
					<span>Django</span>
					<span class="text-primary-800">Docme</span>
				</h2>
			</header>
			<section class="p-8 m-4 flex flex-col gap-2">
				<span class="text-lg">
					A <span class="font-bold text-lg">django</span>
					package that let you create your docs not coding it .
				</span>
				<br />
				<blockquote class="blockquote">
					<span class="text-gray-600 italic">
						with django docme you build documentation faster that ever , you focus only on the
						content that you provide, the hard thing on us .
					</span>
				</blockquote>
			</section>
			<footer class="card-footer flex gap-2 m-4">
				<a class="btn variant-filled-secondary rounded-lg font-semibold w-full" href="{base}/">
					Get Started
				</a>
				<a class="btn variant-filled-tertiary rounded-lg font-semibold w-full" href="{base}/">
					About
				</a>
			</footer>
		</div>
	</div>
</main>
