import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Login from "./pages/login";
import Upload from "./pages/upload";
class App extends Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Route path="/login" exact component={Login} />
          <Route path="/upload" exact component={Upload} />
        </div>
      </Router>
    );
  }
}
export default App;
