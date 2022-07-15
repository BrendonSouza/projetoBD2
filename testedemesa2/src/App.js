import React, { useEffect, useState } from "react"
import './App.css';

import { publicRequest } from "./services/api";


const App = () => {
  const [data, setData] = useState(false)
  let listaLinhas = [{ "id": 350, "variavel_o": "arr0", "valor_hexa_o": "5", "variavel_p": "arr0", "valor_hexa_p": "5", "linha_p": "var arr = [5, 4, 3, 2, 1];", "id_teste_de_mesa": 31, "linha_o": "var arr = [5, 4, 3, 2, 1];" }, { "id": 351, "variavel_o": "arr1", "valor_hexa_o": "4", "variavel_p": "arr1", "valor_hexa_p": "4", "linha_p": "var arr = [5, 4, 3, 2, 1];", "id_teste_de_mesa": 31, "linha_o": "var arr = [5, 4, 3, 2, 1];" }, { "id": 352, "variavel_o": "arr2", "valor_hexa_o": "3", "variavel_p": "arr2", "valor_hexa_p": "3", "linha_p": "var arr = [5, 4, 3, 2, 1];", "id_teste_de_mesa": 31, "linha_o": "var arr = [5, 4, 3, 2, 1];" }, { "id": 353, "variavel_o": "arr3", "valor_hexa_o": "2", "variavel_p": "arr3", "valor_hexa_p": "2", "linha_p": "var arr = [5, 4, 3, 2, 1];", "id_teste_de_mesa": 31, "linha_o": "var arr = [5, 4, 3, 2, 1];" }, { "id": 354, "variavel_o": "arr4", "valor_hexa_o": "1", "variavel_p": "arr4", "valor_hexa_p": "1", "linha_p": "var arr = [5, 4, 3, 2, 1];", "id_teste_de_mesa": 31, "linha_o": "var arr = [5, 4, 3, 2, 1];" }, { "id": 355, "variavel_o": "items", "valor_hexa_o": "4,5,3,2,1", "variavel_p": "items", "valor_hexa_p": "4,5,3,2,1", "linha_p": "function bubbleSort(items) {", "id_teste_de_mesa": 31, "linha_o": "function bubbleSort(items) {" }, { "id": 356, "variavel_o": "length", "valor_hexa_o": "5", "variavel_p": "length", "valor_hexa_p": "5", "linha_p": "var length = items.length;", "id_teste_de_mesa": 31, "linha_o": "var length = items.length;" }, { "id": 357, "variavel_o": "i", "valor_hexa_o": "0", "variavel_p": "i", "valor_hexa_p": "0", "linha_p": "for (var i = 0; i < length; i++) {", "id_teste_de_mesa": 31, "linha_o": "for (var i = 0; i < length; i++) {" }, { "id": 358, "variavel_o": "j", "valor_hexa_o": "0", "variavel_p": "j", "valor_hexa_p": "0", "linha_p": "for (var j = 0; j < (length - i - 1); j++) {", "id_teste_de_mesa": 31, "linha_o": "for (var j = 0; j < (length - i - 1); j++) {" }, { "id": 359, "variavel_o": "tmp", "valor_hexa_o": "5", "variavel_p": "tmp", "valor_hexa_p": "5", "linha_p": "var tmp = items[j];", "id_teste_de_mesa": 31, "linha_o": "var tmp = items[j];" }, { "id": 360, "variavel_o": "items0", "valor_hexa_o": "4", "variavel_p": "items0", "valor_hexa_p": "4", "linha_p": "items[j] = items[j+1];", "id_teste_de_mesa": 31, "linha_o": "items[j] = items[j+1];" }, { "id": 361, "variavel_o": "items1", "valor_hexa_o": "4", "variavel_p": "items1", "valor_hexa_p": "4", "linha_p": "items[j] = items[j+1];", "id_teste_de_mesa": 31, "linha_o": "items[j] = items[j+1];" }, { "id": 362, "variavel_o": "items2", "valor_hexa_o": "3", "variavel_p": "items2", "valor_hexa_p": "3", "linha_p": "items[j] = items[j+1];", "id_teste_de_mesa": 31, "linha_o": "items[j] = items[j+1];" }, { "id": 363, "variavel_o": "items3", "valor_hexa_o": "2", "variavel_p": "items3", "valor_hexa_p": "2", "linha_p": "items[j] = items[j+1];", "id_teste_de_mesa": 31, "linha_o": "items[j] = items[j+1];" }, { "id": 364, "variavel_o": "items4", "valor_hexa_o": "1", "variavel_p": "items4", "valor_hexa_p": "1", "linha_p": "items[j] = items[j+1];", "id_teste_de_mesa": 31, "linha_o": "items[j] = items[j+1];" }, { "id": 365, "variavel_o": "items0", "valor_hexa_o": "4", "variavel_p": "items0", "valor_hexa_p": "4", "linha_p": "items[j+1] = tmp;", "id_teste_de_mesa": 31, "linha_o": "items[j+1] = tmp;" }, { "id": 366, "variavel_o": "items1", "valor_hexa_o": "5", "variavel_p": "items1", "valor_hexa_p": "5", "linha_p": "items[j+1] = tmp;", "id_teste_de_mesa": 31, "linha_o": "items[j+1] = tmp;" }, { "id": 367, "variavel_o": "items2", "valor_hexa_o": "3", "variavel_p": "items2", "valor_hexa_p": "3", "linha_p": "items[j+1] = tmp;", "id_teste_de_mesa": 31, "linha_o": "items[j+1] = tmp;" }, { "id": 368, "variavel_o": "items3", "valor_hexa_o": "2", "variavel_p": "items3", "valor_hexa_p": "2", "linha_p": "items[j+1] = tmp;", "id_teste_de_mesa": 31, "linha_o": "items[j+1] = tmp;" }, { "id": 369, "variavel_o": "items4", "valor_hexa_o": "1", "variavel_p": "items4", "valor_hexa_p": "1", "linha_p": "items[j+1] = tmp;", "id_teste_de_mesa": 31, "linha_o": "items[j+1] = tmp;" }]
  const [inputs, setInputs] = useState({})

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      // const res = await publicRequest.post('/enterCode', inputs)
      // console.log(res.data)
      console.log(listaLinhas)
      setData(true)

      
    } catch (error) {
      console.log(error)
    }

  }

  const handleChange = (e) => {
    setInputs(prev => {
      return {
        ...prev,
        [e.target.name]: e.target.value
      }
    })
  }

  return (
    <div className='App'>
      <div className='headerContainer'>
        <h1>Teste de Mesa</h1>
      </div>
      <main className="mainContainer">
        <div className="mainContent">
          <div className="apelidoContainer">
            <h4>Nome do teste de mesa</h4>
            <input name="apelido" id="apelido" onChange={handleChange} />
          </div>
          <div className="container">
            <div className="codigo">
              <h4>Código Original</h4>
              <form>
                <textarea name="programao" id="programao" onChange={handleChange} />
              </form>
            </div>
            <div className="codigo">
              <h4>Código de Produção</h4>
              <form>
                <textarea name="programap" id="programap" onChange={handleChange} />
              </form>
            </div>
          </div>
          <div className="buttonContainer">
            <input type="submit" onClick={(e) => handleSubmit(e)} />
          </div>
        </div>
        { data && (
        <div className="testeMesaContainer">
          <div className="testeMesa">
            <h4 id='resultado'>Result</h4>
            <table>
              <tbody>
                <tr>
                    <th>id</th>
                    <th>Variavel Original</th>
                    <th>Valor O</th>
                    <th>linha O</th>
                    <th>Variavel P</th>
                    <th>Valor P</th>
                    <th>linha P</th>
                </tr>
                  {listaLinhas.map(valor => (
                    <tr>
                    <td >{valor.id}</td>
                    <td >{valor.variavel_o}</td>
                    <td >{valor.valor_hexa_o}</td>
                    <td >{valor.linha_o}</td>
                    <td >{valor.variavel_p}</td>
                    <td >{valor.valor_hexa_p}</td>
                    <td >{valor.linha_p}</td>
                  </tr>
                  ))}
              </tbody>
            </table>
          </div>
        </div>

        )}
      </main>

    </div>
  )
}

export default App;