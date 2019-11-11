import React, { Component } from "react";
import "./styles.css";
import axios from "axios";
import { Redirect } from 'react-router-dom'

export default class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedFile: null,
      hasToken: sessionStorage.getItem("session_id"),
      redirect: false
 
    };
  }
  setRedirect = () => {
    this.setState({
      redirect: true
    })
  }
  renderRedirect = () => {
    if (this.state.redirect) {
      return <Redirect to='/func' />
    }
  }
  render() {
    if (this.state.hasToken) {
      return (
        <div className="upload">
          {this.renderRedirect()}
          <div className="horizonta">
            <div className="input">
              <label for="selecao-arquivo">Selecionar um arquivo</label>
              <input
                type="file"
                name="file"
                id="selecao-arquivo"
                onChange={this.onChangeHandler}
              />
            </div>
            <div>
              <button
                type="button"
                className="upload_button"
                onClick={this.onClickHandler}
              >
                Upload
              </button>
            </div>
          </div>
        </div>
      );
    } else {
      return <div>Loga ai mano</div>;
    }
  }
  onChangeHandler = event => {
    this.setState({
      selectedFile: event.target.files[0],
      loaded: 0
    });
  };
  onClickHandler = () => {
    const data = new FormData();
    data.append("file", this.state.selectedFile);
    axios
      .post("http://localhost:3001/upload", data, {
        // receive two    parameter endpoint url ,form data
      })
      .then(res => {
        // then print response status
        console.log(res.statusText);
        this.setRedirect();
      });
  };
}
