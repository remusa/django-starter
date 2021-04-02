<script>
  import Signup from './Signup.svelte';

  // your script goes here
</script>

<style>
  nav {
    display: flex;
    justify-content: space-between;
  }
</style>

<nav>
  <div class="left">
    <a href="/">Home</a>
  </div>

  <div class="right">

    <a href="/login">Signup</a>
    <a href="/signup">Login</a>
  </div>
</nav>
