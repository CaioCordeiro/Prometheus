import React, { Component } from "react";
import "./styles.css";


export default class Login extends Component{
    state ={
        Email: '',
        Senha: '',
        redirect: false,

    }
   
    constructor(props) {
        super(props);
        this.setState({
            inputValue: 'Bolinho4'
        });
        };
    render(){
        return (

            <div className='login'> 

                    <form>
                        <div className='forms'>
                            <div className='info'>
                                <p>Email:</p>
                                <input value={this.state.Email} onChange={evt => this.updateInputValueEmail(evt)} type="text" name="Email"/>
                                <p>Senha:</p>
                                <input value={this.state.Senha} onChange={evt => this.updateInputValueSenha(evt)} type="text" name="Senha"/>
                            </div>  
                            <div className='buttom'>
                                {/* {this.renderRedirect()} */}
                                <button onClick  ={()=>this.login(this.state)} type ="button">Login </button>
                                <button onClick ={() =>this.setRedirect("senha")} type ="button">Esqueci a senha</button>
                            </div>
                        </div>
                    </form>

            </div>
        )
    }
    updateInputValueEmail(evt) {
        this.setState({
          Email: evt.target.value
        });
      }
      updateInputValueSenha(evt) {
        this.setState({
          Senha: evt.target.value
        });
      }
}