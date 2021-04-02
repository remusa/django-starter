<script>
  let email = '';
  let password = '';
  let error = null;

  async function handleSubmit(e) {
    try {
      console.log('signing up user');
      error = null;
    } catch (error) {
      error = err.response.data.message;
    }
  }
</script>

<style>
  .error-message {
    color: hsl(0, 60%, 45%);
    font-weight: 500;
    display: block;
    text-align: center;
    padding: 10px;
  }
</style>

<svelte:head>
  <title>Signup</title>
</svelte:head>

<form on:submit|preventDefault={handleSubmit}>
  {#if error}
    <span class="error-message">{error}</span>
  {/if}

  <label for="email">Email</label>
  <input
    bind:value={email}
    name="email"
    type="email"
    placeholder="email@example.com"
    required />

  <label for="password">Password</label>
  <input
    bind:value={password}
    name="password"
    type="password"
    placeholder="*****"
    required />

  <button type="submit">Submit</button>
</form>
