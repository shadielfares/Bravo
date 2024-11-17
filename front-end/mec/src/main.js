import React from "react";
import { useState } from "react";
import './main.css';
import Background from "./background.mp4";
import Typewriter from 'typewriter-effect';
import axios from "axios";

const Main = () => {

    const [inputLink, setInputLink] = useState("");
    const [loading, setLoading] = useState(false); 

    const linkSubmit = async (e) => {
        e.preventDefault()
        try{
            var result = await axios.post('https://localhost:4000/create_report',
                { link: inputLink },
                { responseType: 'blob' }
            )
    
            if (result.status === 200 || result.data.status == "ok"){
                console.log("Link sent successfully!!")

                const blob = new Blob([result.data], { type: 'application/pdf' });
                const url = window.URL.createObjectURL(blob);

                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'generated_report.pdf');
                document.body.appendChild(link);
                link.click();
                link.parentNode.removeChild(link);

                // Clean up URL object
                window.URL.revokeObjectURL(url);
                //DOWNLOAD THE PDF HERE
            } else {
                console.log("failed to send link")
            }
        } catch (error) {
            console.log(error.message)
        }
    }
    return(
        <div className="App">
            <div className="Content">
                <video autoPlay loop muted className="backgroundVideo">
                    <source src={Background} type="video/mp4" />
                </video>
                <div className="Welcome">
                    <div className="box">
                    <h1 style={{display: "flex", justifyContent: "center"}}>
                        Welcome to
                        <span style={{ color: '#149414', marginLeft: "1%" }}>
                        <Typewriter
                        onInit={(typewriter) => {
                        typewriter.typeString('HackMe').start();
                        }}
                        />
                        </span>
                    </h1>
                    <div>
                        <form className="input-form" onSubmit={linkSubmit}>
                            <input placeholder="Insert your link here..." className="link-input" onChange={(e) => setInputLink(e.target.value)}/>
                            <button type="Submit" className="link-submit">{loading ? <>Generating Report...</> : <>Submit</>}</button>
                        </form>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Main;