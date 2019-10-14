import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Login from "./pages/login";
import Upload from "./pages/upload";
import Func from "./pages/func_selec";
class App extends Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Route path="/login" exact component={Login} />
          <Route path="/upload" exact component={Upload} />
          <Route path="/func" exact component={Func} />
        </div>
      </Router>
    );
  }
}
export default App;
