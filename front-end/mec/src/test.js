import React from "react";
import { useState } from "react";

const Test = () => {
    const [userName, setUserName] = useState("")
    const [password, setPassword] = useState("")

    const testSubmit = (e) => {
        e.preventDefault()
        console.log("Username and Password submitted")
    }

    return(
        <div>
            <form onSubmit={testSubmit}>
                <input name="user" placeholder="Username" onChange={(e) => setUserName(e.target.value)} />
                <input name="password" placeholder="Password"  onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default Test;