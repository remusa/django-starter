<script>
  import { testRequest } from '../utils/api';

  let testGet = 'KO';
  let testPost = 'KO';

  let promise = testRequests();

  async function testRequests() {
    const getReq = await testRequest('GET');
    console.log('getReq', getReq);
    const postReq = await testRequest('POST');

    if (getReq.ok) {
      testGet = getReq;
    }

    if (postReq.ok) {
      testPost = postReq;
    }
  }
</script>

<style>

</style>

<div>
  {#await promise}
    <p>Test GET request: ...waiting</p>
    <p>Test POST request: ...waiting</p>
  {:then value}
    <p>Test GET request: {testGet}</p>
    <p>Test POST request: {testPost}</p>
  {:catch error}
    <p style="color: red">{error.message}</p>
  {/await}
</div>
