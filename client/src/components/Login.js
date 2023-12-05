import { useState, useEffect } from "react"
function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const accessToken = sessionStorage.getItem("access_token")
  console.log(accessToken)

  function handleLogin(e){
    e.preventDefault();

    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        "email": email,
        "password": password,
      })
    }

    fetch('http://127.0.0.1:5000/login', options)
    .then((r)=>{
      if (r.status === 200) return r.json()
      else alert("There has been an error!")
    })
    .then(data =>{
      console.log("this came from the backend", data);
      sessionStorage.setItem("access_token", data.access_token)
    })
    .catch(e=>console.log(e))
  }
  return (
    <div>
      {accessToken && accessToken !=="" && accessToken!==undefined ? 
      (<h1>You are logged in, your token is {accessToken}</h1>) :
        <form onSubmit={handleLogin}>
            <h1>Log In</h1>
            <input type="email" placeholder="example@email.com" value={email} onChange={(e)=>setEmail(e.target.value)} />
            <input type="password" placeholder="Password" value={password} onChange={(e)=>setPassword(e.target.value)} />
            <input type="submit"  value="Log in" />
        </form>
    }
        
    </div>
  )
}

export default Login