import React, { Component } from "react";
import "./styles.css";
import { Link } from "react-router-dom";
import axios from "axios";

export default class Main extends Component {
  state = {
    inputValue: "",
    funcs: [],
    hasToken: sessionStorage.getItem("session_id")
  };
  componentDidMount() {
    this.loadfuncs();
  }
  loadfuncs = async () => {
    const response = [
      {
        _id: 11,
        Name: "TESTE1",
        Email: "TESTE1@TESTE1.COM",
        link: "https://2mffgbup77.execute-api.us-east-2.amazonaws.com/Alpha"
      },
      {
        _id: 12,
        Name: "TESTE2",
        Email: "TESTE2@TESTE2.COM",
        link: "https://2mffgbup77.execute-api.us-east-2.amazonaws.com/Alpha"
      },
      {
        _id: 13,
        Name: "TESTE3",
        Email: "TESTE3@TESTE3.COM",
        link: "https://2mffgbup77.execute-api.us-east-2.amazonaws.com/Alpha"
      },
      {
        _id: 13,
        Name: "TESTE3",
        Email: "TESTE3@TESTE3.COM",
        link: "https://2mffgbup77.execute-api.us-east-2.amazonaws.com/Alpha"
      }
    ]; // <- RECEBE UM ARRAY COM AS FUNÇÕES POSSIVEIS
    this.setState({ funcs: response });
  };
  constructor(props) {
    super(props);
    this.setState({
      inputValue: "Bolinho4"
    });
  }
  findOnBd = async param => {
    let response;
    if (param == "") {
      param = "FAIL";
    }
    response = []; //<- RECEBE UM ARRAY COM AS FUNÇÕES POSSIVEIS

    const backState = [
      {
        _id: 11,
        Name: "TESTEBack1",
        Email: "TESTEBack1@TESTEBack1.COM",
        link: "https://2mffgbup77.execute-api.us-east-2.amazonaws.com/Alpha"
      },
      {
        _id: 12,
        Name: "TESTE2Back",
        Email: "TESTE2@TESTEBack2.COM",
        link: "https://2mffgbup77.execute-api.us-east-2.amazonaws.com/Alpha"
      }
    ];
    if (response) {
      Array.isArray(response)
        ? this.setState({ funcs: response })
        : this.setState({ funcs: [response] });
    } else {
      this.setState({ funcs: backState });
    }
  };

  render() {
    if (this.state.hasToken) {
      return (
        <div className="funcs-list">
          <div className="top">
            <input
              value={this.state.inputValue}
              onChange={evt => this.updateInputValue(evt)}
              placeholder="Insert search"
            />
            <button onClick={() => this.findOnBd(this.state.inputValue)}>
              Procurar
            </button>
            <button onClick={() => this.findOnBd("")}> Back</button>
            {/* <a className="plus" href="http://localhost:3000/cadastro">
              +
            </a> */}
          </div>
          {this.state.funcs.map(func => (
            <article key={func._id}>
              <div className="Upper">
                <img src={func.link} />
                <strong>{func.Name}</strong>
              </div>
              <p>{func.Email}</p>
              {/* <Link to={`/notes/${func._id}`}>Notes</Link> */}
            </article>
          ))}
        </div>
      );
    } else {
      return <div>Loga ai mano</div>;
    }
  }
  updateInputValue(evt) {
    this.setState({
      inputValue: evt.target.value
    });
  }
}
