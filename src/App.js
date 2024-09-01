import React from 'react'
import { Route, Routes } from 'react-router-dom'

function App() {
  return (
    <div>
      <h1>Welcome to Professional Photography</h1>
      <Routes>
        <Route path="/" element={<div>Home</div>} />
        <Route path="/services" element={<div>Services</div>} />
        <Route path="/contacts" element={<div>Contacts</div>} />
      </Routes>
    </div>
  )
}

export default App
