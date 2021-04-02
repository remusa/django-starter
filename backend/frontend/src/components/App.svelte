<script>
  import { API_HOST } from '../utils/api';
  import Layout from './_layout.svelte';
  import Signup from './Signup.svelte';

  export let name;

  let promise = test();
  let links = [];
  let promiseErrors = '';

  async function test() {
    const res = await fetch(`${API_HOST}/api/v1/links`).catch(
      (e) => (promiseErrors = e)
    );

    if (res.ok) {
      const json = await res.json();
      links = json;
    }
  }
</script>

<svelte:head>
  <title>Django + Svelte starter</title>
</svelte:head>

<Layout>
  <h1>Hello {name}!</h1>

  {#await promise}
    <p>Test GET request: ...waiting</p>
  {:then value}
    <div>
      <p>Test GET request:</p>
      <ul>
        {#each links as link (link.id)}
          <li>{link.title}</li>
        {/each}
      </ul>
    </div>
  {:catch error}
    <p style="color: red">{error.message}</p>
    <p style="color: red">{promiseErrors}</p>
  {/await}

  <Signup />
</Layout>
