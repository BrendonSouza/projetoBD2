import './App.css';

const App = () => {
  return (
    <div className='App'>
      <div className='headerContainer'>
        <h1>Teste de Mesa</h1>
      </div>
      <div className='container'>
        <div className="codigoPrincipal">
          <h4>Código Principal</h4>
          <form action="#">
            <textarea name="codigoPrincipal" id="codigoPrincipal"></textarea>
          </form>
        </div>
        <div className="codigoSecundario">
          <h4>Código Secundário</h4>
          <form action="#">
            <textarea name="codigoSecundario" id="codigoSecundario"></textarea>
          </form>
        </div>
      </div>
      <div className="testeMesaContainer">
        <div className="testeMesa">
          <h4 id='resultado'>Resultado</h4>
          <table>
            <tr>
              <th>Variável A</th>
              <th>Variável B</th>
              <th>Variável C</th>
              <th>Variável D</th>
              <th>Variável E</th>

            </tr>
            <tr>
              <td>15</td>
              <td>22</td>
              <td>83</td>
              <td>83</td>
              <td>83</td>
            </tr>
            <tr>
              <td>11</td>
              <td>88</td>
              <td>47</td>
              <td>47</td>
              <td>47</td>
            </tr>
          </table>
        </div>
      </div>

    </div>
  )
}

export default App;