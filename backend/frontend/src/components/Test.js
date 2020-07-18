import React, { useState, useEffect } from 'react'
import { testRequest, API_HOST } from './api'

const Test = () => {
  const [testGet, setTestGet] = useState('KO')
  const [testPost, setTestPost] = useState('KO')

  useEffect(() => {
    async function testRequests() {
      const getReq = await testRequest('GET')
      const postReq = await testRequest('POST')

      setTestGet(getReq)
      setTestPost(postReq)
    }

    testRequests()
  }, [])

  return (
    <div>
      <p>Test GET request: {testGet}</p>
      <p>Test POST request: {testPost}</p>
    </div>
  )
}

export default Test
