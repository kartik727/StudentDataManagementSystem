import React from 'react'

const getValueAndLogin=(props:any)=>{
    const userId = (document.getElementById("userId") as HTMLInputElement)?.value
    console.log()
    const pwd = (document.getElementById("pwd") as HTMLInputElement)?.value
    props.login({userId:userId,pwd:pwd,role:props.role})
}
const LoginModal = (props:any) => {
    return <div className="login-modal-container">
        <div className="login-ins"> If you are signing up, enter your school emailid and we will send you the password to your emailid</div>
        <div className="login-modal-input-wrap">
            <div className="login-modal-input">
                <label htmlFor="user-id" className="login-input-field"> User Id:</label>
                <input name="user-id" id="userId" type="text" className="login-input-field t"/>
            </div>
            <div className="login-modal-input">
                <label htmlFor="password" className="login-input-field"> Password:</label>
                <input name="password" id="pwd" type="password" className="login-input-field t"/>
            </div>
        </div>
        <div className="login-modal-submit-button-wrap">
            <div className="login-modal-button" onClick={()=>getValueAndLogin(props)}>
                Login
            </div>
            <div className="login-modal-button">
                Cancel
            </div>
        </div>
        <div className="forgot-pwd">
            Forgot password
        </div>
    </div>
}

export default LoginModal