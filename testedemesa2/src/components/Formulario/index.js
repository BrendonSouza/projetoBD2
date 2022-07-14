import { useState } from "react";
import { publicRequest } from "../../services/api";
import "./styles.css"

export const Formulario = () => {
    const [inputs, setInputs] = useState({})

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const res = await publicRequest.post('enterCode', inputs)
            console.log(res.data)
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
        <div className="mainContent">
            <div className="container">
                <div className="codigo">
                    <h4>Código Original</h4>
                    <form>
                        <textarea name="codigoO" id="codigoO" onChange={handleChange} />
                    </form>
                </div>
                <div className="codigo">
                    <h4>Código de Produção</h4>
                    <form>
                        <textarea name="codigoP" id="codigoP" onChange={handleChange} />
                    </form>
                </div>
            </div>
            <div className="buttonContainer">
                <input type="submit" onClick={(e) => handleSubmit(e)} />
            </div>
        </div>

    )
}