<script>
	import { CodeBlock } from '@skeletonlabs/skeleton';

	export let lang;
	export let text;
</script>

<!-- <pre class={lang}><code>{text}</code></pre> -->

<CodeBlock text={'text-lg'} rounded="rounded-xl" lineNumbers={true} language={lang} code={text} />
