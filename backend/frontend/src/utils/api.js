export const API_HOST = 'http://localhost:8000';

let _csrfToken = null;

async function getCsrfToken() {
  if (_csrfToken === null) {
    const response = await fetch(`${API_HOST}/csrf/`, {
      credentials: 'include',
    });

    const data = await response.json();
    _csrfToken = data.csrfToken;
  }

  return _csrfToken;
}

export async function testRequest(method) {
  const response = await fetch(`${API_HOST}/ping/`, {
    method: method,
    headers: method === 'POST' ? { 'X-CSRFToken': await getCsrfToken() } : {},
    credentials: 'include',
  });

  const data = await response.json();
  return data.result;
}
