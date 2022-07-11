import { useState } from "react"
import './App.css';

import { Formulario } from "./components/Formulario";


const App = () => {
  const listaColumns = ["Variável A", "Variável B", "Variável C", "Variável D", "Variável E", "Variável F"]
  const listaLinhas = ["15", "22", "82", "31", "11", "12"]

  return (
    <div className='App'>
      <div className='headerContainer'>
        <h1>Teste de Mesa</h1>
      </div>
      <main className="mainContainer">
        <Formulario />
        <div className="testeMesaContainer">
          <div className="testeMesa">
            <h4 id='resultado'>Result</h4>
            <table>
              <tbody>
                <tr>
                  {listaColumns.map(chave => (
                    <th key={chave}>{chave}</th>
                  ))}
                </tr>
                <tr>
                  {listaLinhas.map(valor => (
                    <td key={valor}>{valor}</td>
                  ))}
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </main>

    </div>
  )
}

export default App;