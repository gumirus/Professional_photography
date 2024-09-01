import React from 'react'
import { Route, Switch } from 'react-router-dom'

function App() {
  return (
    <div>
      <h1>Welcome to Professional Photography</h1>
      <Switch>
        <Route exact path="/" component={() => <div>Home</div>} />
        <Route path="/services" component={() => <div>Services</div>} />
        <Route path="/contacts" component={() => <div>Contacts</div>} />
      </Switch>
    </div>
  )
}

export default App
