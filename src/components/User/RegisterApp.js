import React from 'react'
import ErrorMsg from './ErrorMsg'
import RegisterForm from './RegisterForm'

const RegisterApp = ({
  handleSubmit,
  errorMsg
}) => (
  <div className="row">
    <h1>Register</h1>
    <div className="col s6 offset-s3">
      <ErrorMsg errorMsg={errorMsg} />
      <RegisterForm />
    </div>
  </div>
)

export default RegisterApp
